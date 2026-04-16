document.addEventListener('DOMContentLoaded', () => {
    const chatWindow = document.getElementById('chat-window');
    const queryInput = document.getElementById('query-input');
    const sendBtn = document.getElementById('send-btn');
    const activeRepoName = document.getElementById('active-repo-name');
    const repoList = document.getElementById('repo-list');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    const sidebar = document.querySelector('.sidebar');

    // Mobile sidebar toggle
    function openSidebar() {
        sidebar.classList.add('open');
        sidebarOverlay.classList.add('active');
    }
    function closeSidebar() {
        sidebar.classList.remove('open');
        sidebarOverlay.classList.remove('active');
    }
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', () => {
            sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
        });
    }
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', closeSidebar);
    }

    const API_BASE = '/api/v1';

    let currentRepoId = null;

    async function apiRequest(endpoint, options = {}) {
        const headers = {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token') || ''}`,
            ...options.headers
        };
        const response = await fetch(`${API_BASE}${endpoint}`, { ...options, headers });
        if (!response.ok) throw new Error(`API Error: ${response.statusText}`);
        return response.json();
    }

    function addMessage(text, isUser = false, references = []) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user' : 'ai'}`;
        
        let html = `<div class="message-bubble">${text}</div>`;
        
        if (references && references.length > 0) {
            html += `<div class="references-grid">`;
            references.forEach(ref => {
                html += `
                    <div class="reference-card">
                        <div class="card-title">${ref.file_path}</div>
                        <div style="color: var(--text-secondary); opacity: 0.8;">Lines ${ref.line_start}-${ref.line_end}</div>
                    </div>
                `;
            });
            html += `</div>`;
        }

        messageDiv.innerHTML = html;
        chatWindow.appendChild(messageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function showTyping() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message ai typing';
        typingDiv.id = 'typing-indicator';
        typingDiv.innerHTML = '<div class="message-bubble"><span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></div>';
        chatWindow.appendChild(typingDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function removeTyping() {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) indicator.remove();
    }

    async function handleQuery() {
        const query = queryInput.value.trim();
        if (!query) return;

        queryInput.value = '';
        addMessage(query, true);
        showTyping();
        
        try {
            const response = await apiRequest('/query', {
                method: 'POST',
                body: JSON.stringify({
                    query: query,
                    repo_id: currentRepoId,
                    context_type: 'codebase'
                })
            });
            
            removeTyping();
            if (response.success) {
                addMessage(response.data.answer, false, response.references);
            } else {
                addMessage("I encountered an issue processing your request.", false);
            }
        } catch (error) {
            removeTyping();
            addMessage(`Error: ${error.message}. Make sure the backend is running and you are authenticated.`, false);
        }
    }

    async function loadRepositories() {
        try {
            const repos = await apiRequest('/repositories');
            repoList.innerHTML = '';
            repos.forEach(repo => {
                const item = document.createElement('div');
                item.className = `nav-item ${repo.id === currentRepoId ? 'active' : ''}`;
                item.innerHTML = `<span>${repo.name}</span>`;
                item.onclick = () => {
                    document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
                    item.classList.add('active');
                    currentRepoId = repo.id;
                    activeRepoName.textContent = repo.name;
                    addMessage(`Switched context to **${repo.name}**. How can I help with this repository?`, false);
                    closeSidebar();
                };
                repoList.appendChild(item);
            });
        } catch (error) {
            console.error("Failed to load repositories:", error);
        }
    }

    sendBtn.addEventListener('click', handleQuery);
    queryInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleQuery();
    });

    // Initial load
    async function init() {
        if (!sessionStorage.getItem('token')) {
            try {
                const { token } = await apiRequest('/auth/demo-token');
                sessionStorage.setItem('token', token);
                console.log("Demo token acquired.");
            } catch (error) {
                console.error("Failed to acquire demo token:", error);
            }
        }
        await loadRepositories();
    }
    
    init();
});

# AI Generation Pipeline

## Purpose

This pipeline defines how AI creates or updates documentation and knowledge artifacts from source changes.

## Trigger Sources

- GitHub push webhook
- Repo ingestion refresh
- Ticket updates
- Manual backend request

## Generation Steps

### 1. Detect Change

- Read commit diff
- Identify impacted files
- Map changed code to docs or knowledge areas

### 2. Gather Context

- Collect related source chunks
- Include existing docs
- Include recent task history

### 3. Generate Draft

- Ask the LLM to summarize the change
- Produce minimal, structured documentation
- Keep output repo-specific

### 4. Validate

- Check for duplicate content
- Check for stale references
- Verify file paths and identifiers

### 5. Persist

- Update the target documentation file
- Save the generation task in `agent_tasks`
- Record the linked commit or webhook event

## Documentation Outputs

- Architecture notes
- API changes
- Module ownership notes
- Debugging runbooks
- Ticket-to-code mapping notes

## Rules

- Do not invent new architecture
- Do not overwrite unrelated sections
- Only update what changed
- Keep generated text short and actionable

## Fallback

If generation confidence is low:

- Flag the doc as needing human review
- Keep the source references
- Do not auto-merge the output

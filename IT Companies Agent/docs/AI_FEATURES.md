# AI Features

## RAG Pipeline

The system uses retrieval augmented generation instead of full model training.

### Steps

1. Collect source material.
2. Chunk text into stable segments.
3. Generate embeddings.
4. Store vectors and metadata.
5. Retrieve top matches for a query.
6. Build final prompt with citations.
7. Return answer with references.

## Embedding Generation

- Convert code, docs, Slack context, and tickets into chunks
- Attach repo and source metadata
- Store the vector plus document pointer

## Prompt Strategy

- Keep prompts short and task-specific
- Include only top-ranked context
- Ask for file paths, line numbers, and concise explanations
- Prefer deterministic instructions over open-ended prompts

## Context Window Management

- Rank content by relevance
- Deduplicate near-identical chunks
- Trim low-value context first
- Preserve code blocks and error traces when debugging

## Fallback Logic

If AI confidence is low:

- Return partial findings
- Show relevant files
- Ask for missing context
- Save the failure mode in task history

## AI Capabilities

- Codebase Q&A
- Documentation updates
- Debug analysis
- Ticket enrichment
- Ownership inference

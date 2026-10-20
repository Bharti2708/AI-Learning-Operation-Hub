# Design Principles

## Single Responsibility Principle

Each component performs one well-defined task.

Examples include:

- Search retrieves knowledge.
- Validator evaluates evidence quality.
- Prompt Builder constructs prompts.
- Foundry Client communicates with Azure AI Foundry.

---

## Separation of Concerns

Business logic is separated from infrastructure logic.

For example:

- User interaction remains in `chat_app.py`.
- Workflow coordination resides in `orchestrator.py`.
- Azure communication is isolated in `foundry_client.py`.

This separation improves maintainability and simplifies testing.

---

## Modular Design

The architecture has been designed so that components can evolve independently.

For example, the current keyword-based search implementation can later be replaced with Azure AI Search without requiring changes to:

- Prompt Builder
- Foundry Client
- Orchestrator
- User Interface

---
# Design Decision 1

## Why introduce an Orchestrator?

### Problem

Originally all business logic lived inside chat_app.py.

This made the application difficult to extend and violated the Single Responsibility Principle.

### Decision

Introduce a LearningAssistantOrchestrator responsible for coordinating the workflow.

- Benefits
- Cleaner architecture
- Easier testing
- Reusable workflow
- Better separation of concerns

---
# Design Decision 2
## Why create a Foundry Client?

### Problem

Azure-specific code was mixed with application logic.

### Decision

Extract all Azure AI Foundry communication into foundry_client.py.

Benefits
- Infrastructure isolated
- Easier migration
- Cleaner orchestration

---
# Design Decision 3
## Why create a Prompt Builder?

### Problem

Prompt construction was embedded inside the application loop.

### Decision

Move prompt construction into a dedicated module.

Benefits

- Prompt engineering becomes reusable
- Easier experimentation
- Cleaner architecture
---
# Design Decision 4
## Why add a Knowledge Validator?

### Problem

Weak retrieval results could still reach the LLM.

### Decision

Introduce a validation layer between retrieval and prompt generation.

Benefits

- Better grounding
- Reduced hallucinations
- More trustworthy responses
---
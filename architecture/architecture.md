# LearnFlow AI Architecture

## Overview

LearnFlow AI is an enterprise Retrieval-Augmented Generation (RAG) application built using Azure AI Foundry. The system transforms organisational knowledge into a grounded AI assistant capable of answering questions from learning operations, trainer documentation, and internal knowledge bases.

Unlike a traditional chatbot that relies solely on a Large Language Model (LLM), LearnFlow AI retrieves relevant organisational knowledge before generating a response. This retrieval-first approach improves factual accuracy, reduces hallucinations, and provides traceable source attribution.

The architecture has been intentionally designed to be modular, allowing each component to evolve independently as the project grows.

---

# Design Goals

The primary architectural goals are:

- Build a grounded AI assistant for learning operations.
- Minimise hallucinations through Retrieval-Augmented Generation (RAG).
- Separate application responsibilities into reusable modules.
- Create an architecture that can evolve from local retrieval to Azure AI Search.
- Demonstrate enterprise AI design patterns using Azure AI Foundry.
- Keep the system maintainable and extensible.

---

# High-Level Architecture

```
                    User
                      │
                      ▼
                chat_app.py
                      │
                      ▼
      LearningAssistantOrchestrator
                      │
      ┌───────────────┼─────────────────────┐
      ▼               ▼                     ▼
Knowledge Search  Prompt Builder      Foundry Client
      │
      ▼
Knowledge Validator
      │
      ▼
Context Builder
      │
      ▼
Azure AI Foundry
      │
      ▼
Streaming Response
```

The orchestrator coordinates the complete request lifecycle while delegating specialised tasks to dedicated components. Each component performs one well-defined responsibility, resulting in a modular and maintainable architecture.

---

# Request Lifecycle

Each user request follows the workflow below.

```
User Question
      │
      ▼
Search Knowledge Base
      │
      ▼
Validate Search Results
      │
      ▼
Build Knowledge Context
      │
      ▼
Generate Grounded Prompt
      │
      ▼
Azure AI Foundry
      │
      ▼
Stream Response
      │
      ▼
Display Sources
```

### Step 1 – User Question

The user submits a question through the command-line interface.

---

### Step 2 – Knowledge Retrieval

The search component retrieves the most relevant knowledge sections from the organisational knowledge base.

The retrieval process currently includes:

- Keyword matching
- Synonym expansion
- Coverage calculation
- Candidate ranking

---

### Step 3 – Knowledge Validation

Retrieved sections are validated before being sent to the language model.

The validator ensures that retrieved evidence satisfies minimum quality thresholds, including:

- Minimum coverage
- Minimum matched concepts
- Non-empty content

If no evidence passes validation, the system intentionally avoids generating unsupported answers.

---

### Step 4 – Context Construction

Validated knowledge sections are combined into a structured context block.

This context contains:

- Organisational knowledge
- Section headings
- Source references

The context is later injected into the model prompt.

---

### Step 5 – Prompt Construction

The prompt builder combines:

- Organisational knowledge
- Grounding instructions
- User question

When no validated knowledge exists, the prompt explicitly instructs the model to state that the requested information is unavailable within the organisational knowledge.

---

### Step 6 – Response Generation

The Foundry client sends the grounded prompt to Azure AI Foundry using the Responses API.

Responses are streamed back to the application, allowing users to receive answers progressively instead of waiting for the complete response.

---

# Component Architecture

## chat_app.py

### Responsibility

Provides the user interface.

### Responsibilities

- User interaction
- Role selection
- Conversation loop
- Displaying responses
- Displaying source attribution

---

## orchestrator.py

### Responsibility

Coordinates the complete AI workflow.

### Responsibilities

- Execute retrieval
- Execute validation
- Build context
- Build prompts
- Invoke Azure AI Foundry
- Return responses

The orchestrator contains no retrieval or prompting logic itself. Instead, it coordinates specialised components.

---

## knowledge_loader.py

### Responsibility

Loads organisational knowledge into memory.

### Responsibilities

- Read Markdown documents
- Split documents into sections
- Prepare searchable knowledge objects

---

## knowledge_search.py

### Responsibility

Retrieves candidate knowledge sections.

### Current Capabilities

- Keyword matching
- Synonym expansion
- Coverage calculation
- Search ranking
- Source tracking

This module focuses exclusively on retrieval.

---

## knowledge_validator.py

### Responsibility

Acts as the quality gate between retrieval and generation.

### Responsibilities

- Reject weak search results
- Validate coverage
- Validate matched concepts
- Prevent unsupported responses

The validator ensures that only sufficiently relevant organisational knowledge is provided to the language model.

---

## prompt_builder.py

### Responsibility

Creates grounded prompts for Azure AI Foundry.

### Responsibilities

- Combine retrieved knowledge
- Add grounding instructions
- Add user question
- Create fallback prompts

Prompt construction is isolated from retrieval logic, allowing prompts to evolve independently.

---

## foundry_client.py

### Responsibility

Handles communication with Azure AI Foundry.

### Responsibilities

- Authentication
- Responses API calls
- Streaming responses
- Conversation continuation

Infrastructure-specific code remains isolated from business logic.

---

# Knowledge Retrieval Pipeline

The retrieval pipeline is responsible for identifying the organisational knowledge most relevant to a user's question.

```text
User Question
      │
      ▼
Normalise Query
      │
      ▼
Expand Synonyms
      │
      ▼
Search Knowledge Sections
      │
      ▼
Calculate Coverage
      │
      ▼
Rank Results
      │
      ▼
Validate Results
      │
      ▼
Return Validated Knowledge
```

Separating retrieval from validation enables each stage to evolve independently. Future retrieval engines, such as Azure AI Search, can replace the current implementation without affecting downstream components.

---

# Prompt Engineering Strategy

LearnFlow AI follows a grounded prompting approach.

When validated organisational knowledge exists, the model receives:

- Retrieved knowledge
- Grounding instructions
- User question

The model is instructed to answer only using the supplied organisational knowledge.

If no validated knowledge is available, the prompt instructs the model to respond that the requested information is not specified within the available organisational knowledge.

This behaviour reduces hallucinations and encourages reliable responses.

---

# Project Structure

```
LearnFlow-AI/
│
├── README.md
│
├── architecture/
│   ├── architecture.md
│   └── diagrams/
│
├── src/
│   ├── chat_app.py
│   ├── orchestrator.py
│   ├── foundry_client.py
│   ├── knowledge_loader.py
│   ├── knowledge_search.py
│   ├── knowledge_validator.py
│   └── prompt_builder.py
│
├── knowledge_base/
│
├── requirements.txt
│
└── .env.example
```

---

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

# Current Limitations

The current implementation intentionally prioritises architectural clarity over production-scale capabilities.

Current limitations include:

- Local Markdown knowledge base
- Keyword-based retrieval
- Basic ranking heuristics
- Rule-based validation
- Single-user command-line interface
- Limited logging and observability

These limitations are expected to evolve in future iterations.

---

# Future Enhancements

The planned architecture roadmap includes:

```text
Current Architecture
        │
        ▼
Azure AI Search
        │
        ▼
Hybrid Search
        │
        ▼
Semantic Ranking
        │
        ▼
Vector Search
        │
        ▼
Conversation Manager
        │
        ▼
Evaluation Framework
        │
        ▼
Learning Analytics Dashboard
        │
        ▼
Web Application
        │
        ▼
Copilot Studio Integration
```

Future enhancements will focus on improving retrieval quality, observability, scalability, and enterprise deployment capabilities.

---

# Architecture Evolution

The project has evolved through multiple architectural iterations.

```text
Version 1
─────────
Single chat_app.py

        │
        ▼

Version 2
─────────
Knowledge Loader

        │
        ▼

Version 3
─────────
Knowledge Search

        │
        ▼

Version 4
─────────
Prompt Builder

        │
        ▼

Version 5
─────────
Foundry Client

        │
        ▼

Version 6
─────────
LearningAssistantOrchestrator

        │
        ▼

Version 7
─────────
Knowledge Validator

        │
        ▼

Next
────
Azure AI Search
Hybrid Search
Semantic Ranking
Vector Search
Evaluation Framework
```

Each iteration has focused on improving modularity, maintainability, and alignment with enterprise AI application architecture.
# AI Learning Operations Hub

> **An AI-powered Learning Operations Assistant built with Azure AI Foundry, Python and Retrieval-Augmented Generation (RAG) to deliver grounded, source-backed responses from organisational knowledge.**

---
## Highlights

- Built with Azure AI Foundry
- Retrieval-Augmented Generation (RAG)
- Grounded AI responses with source attribution
- Knowledge validation to reduce hallucinations
- Modular Python architecture
- Enterprise learning operations use case

## Overview

AI Learning Operations Hub is a portfolio project demonstrating how Generative AI can improve learning operations by helping trainers, learners and programme teams quickly access trusted organisational knowledge.

Rather than relying solely on a Large Language Model, the application retrieves relevant information from internal documentation, validates the retrieved knowledge and generates grounded responses with clear source attribution. When sufficient evidence is unavailable, the assistant safely indicates that the requested information is not available within the organisational knowledge base.

This project showcases practical application of Azure AI Foundry, Retrieval-Augmented Generation (RAG), prompt engineering and modular software design to build responsible AI solutions for enterprise learning environments.

User
  │
  ▼
Knowledge Search
  │
  ▼
Knowledge Validator
  │
  ▼
Prompt Builder
  │
  ▼
Azure AI Foundry
  │
  ▼
Grounded Response

---

## Business Problem

Learning operations teams manage a wide range of documentation including trainer SOPs, operational procedures, learner guides and programme documentation. Finding accurate information quickly can be challenging, especially across distributed teams.

Traditional AI assistants may generate plausible but unsupported answers, making them unsuitable for operational guidance.

AI Learning Operations Hub demonstrates how Retrieval-Augmented Generation (RAG) can improve trust by retrieving organisational knowledge, validating evidence before response generation and providing grounded answers with source attribution.

---

## Solution

The application implements a modular Retrieval-Augmented Generation (RAG) pipeline using Azure AI Foundry.

## Current Architecture

```
                     LearnFlow AI

                        User
                          │
                          ▼
                  chat_app.py
                          │
                          ▼
              LearningAssistantOrchestrator
                          │
      ┌───────────────────┼───────────────────┐
      ▼                   ▼                   ▼
Knowledge Search   Knowledge Validator   Prompt Builder
      │
      ▼
Context Builder
      │
      └───────────────────┐
                          ▼
                  Foundry Client
                          │
                          ▼
                 Azure AI Foundry
                          │
                          ▼
                 Streaming Response
---

The modular architecture separates retrieval, validation, prompt construction and model interaction, making the solution easier to maintain and extend.

---

## Key Features

- AI-powered Learning Operations Assistant
- Role-based interaction (Learner, Trainer, Program Manager and Administrator)
- Retrieval-Augmented Generation (RAG)
- Knowledge validation quality gate
- Grounded prompt engineering
- Source attribution for supported answers
- Safe fallback when organisational knowledge is unavailable
- Modular Python architecture
- Azure AI Foundry integration
- Enterprise-ready design for future Azure AI Search integration

---

## Technical Highlights

- Built using **Azure AI Foundry** and **Azure OpenAI**
- Implemented a modular orchestration layer separating retrieval, validation and response generation
- Developed a retrieval pipeline using keyword and synonym-based matching
- Added a knowledge validation layer to reject weak or unsupported evidence before LLM generation
- Designed prompts to encourage grounded, source-backed responses
- Implemented safe fallback behaviour to minimise hallucinations
- Structured the project for future migration to Azure AI Search and semantic retrieval

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| AI Platform | Azure AI Foundry |
| Authentication | Azure Identity |
| AI Model | Azure OpenAI |
| AI Techniques | Retrieval-Augmented Generation (RAG), Prompt Engineering |
| Configuration | Python-dotenv |

---

## Project Structure

```text
AI-Learning-Operations-Hub/
│
├── architecture/
├── data/
├── demo/
├── docs/
├── screenshots/
├── src/
│   ├── chat_app.py
│   ├── orchestrator.py
│   ├── knowledge_loader.py
│   ├── knowledge_search.py
│   ├── knowledge_validator.py
│   ├── prompt_builder.py
│   ├── foundry_client.py
│   └── roles.py
│
├── tests/
├── README.md
└── requirements.txt
```

---

## Example Questions

### Supported

> When is the completion report due?

> When should the virtual session recording be shared?

The assistant retrieves the relevant SOP section and generates a grounded response with source attribution.

### Unsupported

> Who is the CEO of Microsoft?

Response:

> *"The available organisational knowledge does not specify this information."*

This behaviour helps reduce unsupported or hallucinated responses.

---

## Sample Output

```text
Knowledge source(s):
trainer_sop — When is the completion report due?

The completion report should be uploaded within one week of batch completion.
```
## Evaluation

Version 1 was manually evaluated across six scenarios covering:

- Exact knowledge retrieval
- Paraphrased questions
- Minor spelling errors
- Unsupported general-knowledge questions
- Conversation context isolation
- Weak or unrelated retrieval matches

All six defined V1 evaluation scenarios passed after improving controlled synonym handling for paraphrased queries.

See [`tests/manual_test_cases.md`](tests/manual_test_cases.md) for the complete evaluation results.
---
## Getting Started

### Prerequisites

Before running the project, ensure you have:

- Python 3.10 or later
- Git
- An Azure account with access to the required AI model deployment
- Azure CLI installed for local authentication

---
### 1. Clone the repository

```bash
git clone https://github.com/BhartiV93/AI-Learning-Operations-Hub.git
cd AI-Learning-Operations-Hub
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**Git Bash**

```bash
source .venv/Scripts/activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The project uses:

- `openai`
- `azure-identity`
- `python-dotenv`

### 4. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

```env
AZURE_OPENAI_ENDPOINT=<your-endpoint>
MODEL_DEPLOYMENT=<your-model-deployment-name>
```

Replace the placeholder values with the endpoint and model deployment configured for your Azure AI environment.

> **Security:** Never commit your `.env` file or Azure credentials to GitHub. The project includes `.env` in `.gitignore`.

### 5. Authenticate with Azure

The application uses `DefaultAzureCredential` from the Azure Identity library rather than storing a static API key in the repository.

For local development using Azure CLI:

```bash
az login
```

Sign in with an Azure account that has permission to access the configured AI resource.

### 6. Run the application

```bash
python src/chat_app.py
```

Select a role when prompted:

```text
Select your role:
1. Learner
2. Trainer
3. Program Manager
4. Administrator
```

For example, after selecting **Trainer**, try:

```text
When is the completion report due?
```

The assistant should retrieve the relevant synthetic knowledge-base section and return a grounded response with source attribution.

To test safe fallback behaviour, try:

```text
Who is the CEO of Microsoft?
```

Because this information is not contained in the organisational knowledge base, the assistant should respond:

> The available organisational knowledge does not specify this information.

Type `quit` to exit the application.

## Future Enhancements

- Azure AI Search integration
- Semantic vector search
- Multi-document knowledge base
- Conversation memory
- Evaluation and observability
- Web application interface
- Role-specific knowledge repositories

---

## Learning Outcomes

This project strengthened my understanding of:

- Azure AI Foundry
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Responsible AI
- Grounded AI responses
- Modular Python architecture
- Knowledge retrieval and validation
- AI solution design for enterprise learning scenarios

---

## About the Author

I built this project as part of my AI portfolio to demonstrate how Azure AI Foundry and Retrieval-Augmented Generation can be applied to solve real-world learning operations challenges.

The project reflects my professional experience leading AI capability, learning transformation and workforce enablement initiatives while continuing to deepen my expertise in enterprise Generative AI, Azure AI services and AI solution design.

---

## License

This project is intended for learning, demonstration and portfolio purposes.
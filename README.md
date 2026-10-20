# AI Learning Operations Hub

A Python application for trainer SOP questions and completion-report
tracking, using a GPT-5.2 deployment in Microsoft Foundry.

## Features

- Answer trainer questions using local SOP evidence.
- Display source document and section references.
- Return a fixed fallback without a model call when no evidence passes
  the retrieval checks.
- Register completed batches and calculate report deadlines.
- Prevent duplicate batch records.
- Preview reminders for due or overdue pending reports.
- Mark reports as Submitted.
- Access all features through one command-line menu.

For this demo, “within one week” means seven calendar days.

## How it works

SOP questions follow this process:

Question → Local retrieval → Evidence filtering → Grounded prompt
→ Foundry model → Answer with source references

Questions with no accepted evidence return a fixed fallback.

Report tracking uses a local CSV file. Due dates, status updates, and
reminder previews are handled by Python without model calls.

## Technology

- Python
- Microsoft Foundry with a GPT-5.2 deployment
- OpenAI Python SDK
- Azure Identity
- Local Markdown knowledge documents
- CSV report storage

## Setup

Requires Python 3.10+, Azure CLI, and access to the model deployment.

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure:

```dotenv
AZURE_OPENAI_ENDPOINT=your-endpoint
MODEL_DEPLOYMENT=your-deployment-name
```

Use the endpoint format supported by your working deployment.
MODEL_DEPLOYMENT is the Azure deployment name.

Authenticate with an Azure account authorized to use the model:

```powershell
az login
```

Run the application:

```powershell
python src/app.py
```

## Evaluation

Run the local retrieval checks:

```powershell
python tests/check_retrieval.py
```

Run the interactive answer review:

```powershell
python tests/review_foundry.py
```

The answer review makes live model calls for supported questions.

Recorded baseline:
- 7 of 7 automated retrieval checks passed.
- 4 of 4 answer/fallback cases passed human review.

These are small local checks, not a Foundry portal evaluation.
Manual workflow results are recorded in `tests/manual_test_cases.md`.

### Microsoft Foundry baseline

Evaluation Run: `trainer-sop-baseline-v1`

Three supported question-answer examples were evaluated using GPT-5.2
as the judge model:

- Relevance: 3/3 passed.
- Groundedness: 3/3 passed, each scoring 5.
- Overall: 6/6 evaluator checks passed.

This small baseline does not establish general accuracy.
Unsupported-question fallback behaviour was checked separately.
## Limitations

- Retrieval uses keyword and synonym matching.
- Retrieved evidence does not guarantee a correct generated answer.
- Follow-up questions may fail retrieval when they omit key terms.
- Records are stored locally, with no multi-user access controls.
- Submission status is entered manually.
- Reminders are previews run on demand; no messages are sent.

## Planned extensions

- Copilot Studio interface.
- SharePoint report tracking.
- Power Automate reminder delivery.

## Credentials

Keep `.env`, credentials, and real learner records out of the repository.
Use synthetic batch data for demonstrations.
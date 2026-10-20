# AI Learning Operations Hub — V1 Manual Evaluation Results

## Purpose

This document records the manual evaluation performed for Version 1 of the AI Learning Operations Hub.

The evaluation focuses on:

- Knowledge retrieval
- Grounded response generation
- Source attribution
- Paraphrased questions
- Tolerance of minor input errors
- Safe fallback behaviour
- Conversation context isolation
- Rejection of weak or unrelated matches

> **Note:** The project uses synthetic knowledge-base content created for demonstration and testing purposes. No organisational or proprietary data is used.

---

## Test Environment

**Application:** AI Learning Operations Hub  
**Interface:** Python command-line application  
**Selected Role:** Trainer  
**Knowledge Source:** Synthetic `trainer_sop` knowledge base  
**AI Platform:** Microsoft AI Foundry  
**Retrieval Approach:** Lightweight local lexical retrieval with controlled synonym matching  
**Validation:** Knowledge relevance validation before context is supplied to the model  

---

# Test 1 — Exact Knowledge Match

# Manual evaluation — Phase 1

| Question | Expected result | Status |
|---|---|---|
| When is the completion report due? | Within one week of batch completion; cite source | Pass |
| What attendance percentage is required to pass? | State that the knowledge does not specify it | Pass |
| When should I send a session reminder? | 15 minutes before; include meeting link and details | Pass |
| When should I share the session recording? | 30–45 minutes after the session | Pass |
| How many project evaluations are required? | Two: mid-term and final-term | Pass |
| When do learners receive the video? | 30–45 minutes after the session; cite source | Pass |
| What is the minimum passing score for assessments? | State that the knowledge does not specify it | Pass |

The supported completion-report question also passed after an
unsupported question, confirming that the chat loop continued.

## Local answer review

Script: tests/review_foundry.py
Result: 4 of 4 cases passed human review.

Three supported cases exercised Foundry-generated answers.
One unsupported case exercised the local fallback without a model call.

Reviewed answer correctness, unsupported details, and source citations.
This was a local review, not a Foundry portal evaluation.
## Completion-report workflow — manual checks

Test date: 2026-10-20

For this demo, "within one week" means seven calendar days.

| Check | Observed result | Status |
|---|---|---|
| Register ai100, completed 2026-10-20 | Saved with deadline 2026-10-27 and Pending status | Pass |
| Register ai100 again | Duplicate rejected | Pass |
| Check reminders before ai100 deadline | No reminder shown | Pass |
| Register ai99, completed 2026-10-12 | Saved with deadline 2026-10-19 | Pass |
| Check overdue pending reports | Reminder preview shown for ai99 | Pass |
| Mark ai99 as Submitted | Status updated | Pass |
| Check reminders after submission | No reminder shown for ai99 | Pass |
| Mark ai99 as Submitted again | Already-submitted message shown | Pass |
| Register ai101 through the menu | Saved with deadline 2026-10-27 | Pass |
| Quit the SOP assistant | Returned to the main menu | Pass |
| Select Exit | Application closed | Pass |

### Scope

These are manual checks using sample batch records.
Reminder previews run on demand; no messages are sent.
Submission status is entered manually and does not verify an upload.
Copilot Studio and Power Automate are not integrated yet.
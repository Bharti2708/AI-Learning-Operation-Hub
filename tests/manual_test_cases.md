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
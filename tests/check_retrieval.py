import sys
from pathlib import Path

# Allow this script to import files from src.
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))

from knowledge_search import search_knowledge_base
from knowledge_validator import validate_search_results


# Each question has an expected phrase from the SOP.
# None means no evidence should be accepted.
test_cases = [
    ("When is the completion report due?", "one week"),
    ("What attendance percentage is required to pass?", None),
    ("When should I send a session reminder?", "15 minutes"),
    ("When should I share the session recording?", "30 to 45 minutes"),
    ("How many project evaluations are required?", "mid-term"),
    ("When do learners receive the video?", "30 to 45 minutes"),
    ("What is the minimum passing score for assessments?", None),
]

passed_count = 0

for question, expected_phrase in test_cases:
    results = search_knowledge_base(question)
    accepted_results = validate_search_results(results)

    if expected_phrase is None:
        passed = not accepted_results
    else:
        evidence = " ".join(
            result["content"] for result in accepted_results
        ).lower()

        passed = expected_phrase in evidence

    if passed:
        passed_count += 1
        print(f"PASS: {question}")
    else:
        print(f"FAIL: {question}")

print(f"\nPassed {passed_count} of {len(test_cases)} retrieval checks.")

if passed_count != len(test_cases):
    sys.exit(1)
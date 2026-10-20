import sys
from pathlib import Path
import json

from dotenv import load_dotenv

# Allow imports from src.
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))

from chat_app import get_role_instructions
from orchestrator import LearningAssistantOrchestrator


load_dotenv(project_root / ".env")

assistant = LearningAssistantOrchestrator()
instructions = get_role_instructions("Trainer")

test_cases = [
    (
        "When is the completion report due?",
        "Within one week of batch completion.",
    ),
    (
        "When should I share the session recording?",
        "30 to 45 minutes after the session.",
    ),
    (
        "How many project evaluations are required?",
        "Two: mid-term and final-term.",
    ),
    (
        "What is the minimum passing score for assessments?",
        "The available organisational knowledge does not "
        "specify this information.",
    ),
]

passed_count = 0

evaluation_rows = []

for question, expected_answer in test_cases:
    print("\n" + "=" * 60)
    print(f"QUESTION: {question}")
    print(f"EXPECTED: {expected_answer}")

    stream = None

    try:
        stream, sources = assistant.process_question(
            question=question,
            assistant_instructions=instructions,
            previous_response_id=None,
        )

        if stream is None:
            answer = (
                "The available organisational knowledge "
                "does not specify this information."
            )
        else:
            answer = ""
            completed = False

            for event in stream:
                if event.type == "response.output_text.delta":
                    answer += event.delta

                elif event.type == "response.completed":
                    completed = True

                elif event.type in {
                    "response.failed",
                    "response.incomplete",
                    "error",
                }:
                    raise RuntimeError("The response did not complete.")

            if not completed:
                raise RuntimeError("The stream ended before completion.")

    except Exception as error:
        print(f"ERROR: {error}")
        print("Recorded as FAIL.")
        continue

    finally:
        if stream is not None:
            stream.close()

    print("\nRETRIEVED SOURCES:")
    print(", ".join(sources) if sources else "None")

    print("\nACTUAL ANSWER:")
    print(answer)

    print("\nReview:")
    print("- Does the answer match the expected information?")
    print("- Does it avoid unsupported details?")
    print("- For supported answers, does it cite the correct")
    print("  SOP document and section? Check the SOP itself.")
    print("- For the fallback, no citation is required.")

        # Save supported answers for Foundry evaluation.
    if stream is not None:
        evaluation_rows.append({
            "query": question,
            "response": answer,
            "context": assistant.last_context,
            "ground_truth": expected_answer,
        })

    result = input("\nEnter pass or fail: ").strip().lower()

    while result not in {"pass", "fail"}:
        result = input("Please enter pass or fail: ").strip().lower()

    if result == "pass":
        passed_count += 1

print(
    f"\nHuman-reviewed result: "
    f"{passed_count} of {len(test_cases)} passed."
)

output_file = project_root / "tests" / "foundry_evaluation.jsonl"

with output_file.open("w", encoding="utf-8") as file:
    for row in evaluation_rows:
        file.write(json.dumps(row, ensure_ascii=False) + "\n")

print(f"\nEvaluation dataset saved to: {output_file}")
import os
from dotenv import load_dotenv
from orchestrator import LearningAssistantOrchestrator


def get_role_instructions(role):
    """Return system instructions based on the selected user role."""

    common_instructions = """
You are an AI Learning Operations Assistant for an enterprise learning team.

Your responsibilities include:
- supporting AI and digital-skills learning
- explaining technical concepts clearly
- supporting certification preparation
- improving learner engagement and completion
- supporting trainers with delivery and content guidance
- helping program teams understand learning progress
- promoting responsible and ethical use of AI

Only provide information that is appropriate for the user's role.
Do not claim to have access to real learner records, attendance systems,
internal documents, dashboards, or organisational systems unless that
information has been explicitly provided in the conversation.

When information is unavailable, clearly say that sample or connected data
would be required.

When organisational knowledge is supplied:

- Treat it as the primary source of truth.
- Do not contradict it using general knowledge.
- Do not invent organisational procedures, timelines, policies, or data.
- State clearly when the available knowledge does not answer the question.
- Mention the source document used when providing a grounded answer.

Keep responses practical, structured, and concise.
"""

    role_instructions = {
        "Learner": """
The user is a learner.

Help them:
- understand AI and Microsoft Azure concepts
- prepare for AI certifications
- create study plans
- practise with quizzes
- understand how skills relate to career opportunities
- identify knowledge gaps

Use beginner-friendly explanations unless the user requests advanced detail.
Do not invent their assessment results or learning progress.
""",

        "Trainer": """
The user is a trainer.

Help them:
- prepare session plans
- explain complex concepts
- generate practical exercises
- create discussion questions
- improve learner engagement
- create formative assessments
- identify delivery risks

Do not present generated learning content as approved organisational content.
Recommend human review before delivery.
""",

        "Program Manager": """
The user is a program manager.

Help them:
- plan learning programs
- identify delivery risks
- define KPIs
- structure stakeholder updates
- analyse sample learning data
- recommend interventions
- improve completion and adoption

Do not claim access to real dashboards or participant records.
Clearly distinguish assumptions from confirmed information.
""",

        "Administrator": """
The user is a learning administrator.

Help them:
- organise learning records
- structure operational processes
- prepare reminders
- manage content and reporting workflows
- identify administrative risks
- improve data quality and consistency

Do not claim to update external systems or records.
Provide recommendations and draft workflows only.
"""
    }

    return common_instructions + role_instructions[role]



def main():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Get configuration settings
        load_dotenv()
        orchestrator = LearningAssistantOrchestrator()
     
        # Loop until the user wants to quit
        # Track responses
        user_role = "Trainer"
        assistant_instructions = get_role_instructions(user_role)

        print("\nAI LEARNING OPERATIONS HUB")
        print("Trainer SOP Assistant")
        print("Type 'quit' to exit.\n")

        last_response_id = None

        while True:
            input_text = input(f"{user_role}: ").strip()

            if input_text.lower() == "quit":
                print("\nThank you for using the AI Learning Operations Hub.")
                break

            if not input_text:
                print("Please enter a question or type 'quit' to exit.")
                continue

            stream, knowledge_sources = orchestrator.process_question(
                question=input_text,
                assistant_instructions=assistant_instructions,
                previous_response_id=last_response_id,
                )
            
            # Display the fallback when no evidence was found.
            if stream is None:
                print(
                    "\nAssistant: The available organisational "
                    "knowledge does not specify this information.\n"
                )
                continue
            print("\nAssistant: ", end="")

            if knowledge_sources:
                print(
                    "\nKnowledge source(s): "
                    + ", ".join(knowledge_sources)
                    )
            else:
                print("\nKnowledge source: No relevant internal document found") 

            for event in stream:
                if event.type == "response.output_text.delta":
                     print(event.delta, end="", flush=True)

                elif event.type == "response.completed":
                    last_response_id = event.response.id
                    print()

            
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()

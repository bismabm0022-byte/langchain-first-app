import sys
from langchain_core.output_parsers import StrOutputParser
from config import get_chat_model
from prompts import PERSONAS

def run_app():
    try:
        model = get_chat_model()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    output_parser = StrOutputParser()

    print("==========================================")
    print("        LangChain Starter Assistant       ")
    print("==========================================\n")

    print("Select a Persona:")
    for key, (name, _) in PERSONAS.items():
        print(f"[{key}] {name}")

    choice = input("\nSelect (1-3, default 1): ").strip()
    persona_name, prompt_template = PERSONAS.get(choice, PERSONAS["1"])

    # Build LCEL Chain: Prompt -> Model -> Output Parser
    chain = prompt_template | model | output_parser

    print(f"\n--- Active Mode: {persona_name} ---")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            print("\nAI: ", end="", flush=True)
            response = chain.invoke({"user_input": user_input})
            print(f"{response}\n")

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")

if __name__ == "__main__":
    run_app()

from agent.graph import build_graph

def main():
    print("🚀 AutoStream Agent Running...\n")

    app = build_graph()

    state = {
        "name": None,
        "email": None,
        "platform": None,
        "intent": None,
        "response": None,
        "lead_stage": None
    }

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting...")
            break

        state["user_input"] = user_input

        state = app.invoke(state)

        print("Agent:", state.get("response", "⚠️ No response"))


if __name__ == "__main__":
    main()
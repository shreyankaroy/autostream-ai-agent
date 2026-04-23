from langgraph.graph import StateGraph
from typing import TypedDict
from agent.intent import detect_intent
from agent.tools import mock_lead_capture

class AgentState(TypedDict):
    user_input: str
    intent: str
    response: str
    name: str
    email: str
    platform: str
    lead_stage: str


# INTENT NODE
def intent_node(state):
    intent = detect_intent(state["user_input"])
    state["intent"] = intent

    if intent == "greeting":
        state["response"] = "Hi! 😊 How can I help you with AutoStream?"

    elif intent == "pricing":
        state["response"] = """
Here are our plans:

Basic Plan:
- $29/month
- 10 videos/month
- 720p resolution

Pro Plan:
- $79/month
- Unlimited videos
- 4K resolution
- AI captions

Policies:
- No refunds after 7 days
- 24/7 support only for Pro plan
"""

    elif intent == "high_intent":
        # Start lead flow
        if not state.get("lead_stage"):
            state["lead_stage"] = "ask_name"
        state["response"] = "Great! What's your name?"

    return state


# LEAD NODE
def lead_node(state):

    # Capture NAME (skip first intent turn)
    if state.get("lead_stage") == "ask_name":
        if state.get("intent") == "high_intent":
            return state  # don't capture yet

        state["name"] = state["user_input"]
        state["lead_stage"] = "ask_email"
        state["response"] = "Please provide your email."
        return state

    # Capture EMAIL
    if state.get("lead_stage") == "ask_email":
        state["email"] = state["user_input"]
        state["lead_stage"] = "ask_platform"
        state["response"] = "Which platform do you use? (YouTube/Instagram/etc.)"
        return state

    # Capture PLATFORM + CALL TOOL
    if state.get("lead_stage") == "ask_platform":
        state["platform"] = state["user_input"]

        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        state["response"] = "🎉 Lead captured successfully!"
        state["lead_stage"] = None
        return state

    return state


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("intent", intent_node)
    graph.add_node("lead", lead_node)

    graph.set_entry_point("intent")

    graph.add_edge("intent", "lead")

    return graph.compile()
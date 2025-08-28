from .parser import parse_intent
from .models import TripPreferences


class Orchestrator:
    def __init__(self):
        pass  # later intent agents, DB conenctions

    def plan_trip(self, user_text: str) -> TripPreferences:
        # Step 1: parse intent
        preferences = parse_intent(user_text)
        # step 2: Later call destination finder, budget planner, etc
        return preferences

from .models import TripPreferences


def parse_intent(user_text: str) -> TripPreferences:
    """
    Week 1: Mock parser to simulate extracting Preferences
    Later, to replace with NLPpipeline or LLM
    """
    # Very naive keyword-based extraction
    interests = []
    if "beach" in user_text.lower():
        interests.append("beach")
    if "food" in user_text.lower():
        interests.append("food")
    budget = None
    for word in user_text.split():
        if word.isdigit():
            budget = float(word)
    return TripPreferences(
        destination=None,  # We'llfind this later
        budget=budget,
        dates=None,
        interests=interests
    )

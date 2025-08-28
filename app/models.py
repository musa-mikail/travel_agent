from pydantic import BaseModel
from typing import List, Optional


class TripRequest(BaseModel):
    user_input: str


class TripPreferences(BaseModel):
    destination: Optional[str]
    budget: Optional[float]
    dates: Optional[str]
    interests: List[str] = []


class TripResponse(BaseModel):
    message: str
    preferences: TripPreferences

from fastapi import FastAPI
from .models import TripRequest, TripResponse
from .orchestrator import Orchestrator

app = FastAPI(title="Travel Agent MPV - Week 1")

orchestrator = Orchestrator()


@app.post("/plan_trip", response_model=TripResponse)
def plan_trip(request: TripRequest):
    preferences = orchestrator.plan_trip(request.user_input)
    return TripResponse(message="Trip planning started",
                        preferences=preferences)
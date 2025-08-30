from openai import OpenAI
from dotenv import load_dotenv
from os import getenv
import streamlit as st


load_dotenv()

# gets API Key from environment variables
client = OpenAI(
    base_url=getenv("OPENROUTER_BASE_URL"),
    api_key=getenv("OPENROUTER_API_KEY"),
)

model = "google/gemma-3n-e4b-it:free"


class DestinationPlanner():
    def __init__(self):
        pass

    def destination_planning(self, interests, budget, start_date, end_date):
        destination_planner_prompt = f"You are an excellent holiday planner. \
        Your role is to generate a high level selection of cities that match \
        the interests of the user as follows: {interests}, and meeting \
        the budget of the user indicated as {budget} in Dollars.\
        The plan should return cities that have great weather \
        between {start_date} and {end_date}. Return \
        only the top 3 cities as an input compatible for another \
        agent to prepare itenerary of activities for each cities.\
        The output should have a concise summary of the reason for \
        selectign the cities and then a numbered list of the cities \
        proposed. Keep it very concise."
        with st.chat_message("user"):
            print("----- streaming request -----")
            stream = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": getenv("APP_URL"),
                    "X-Title": getenv("APP_TITLE"),
                },
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": destination_planner_prompt,
                    },
                ],
                stream=True,)
            response = st.write_stream(stream)
            return response

class IteneraryMaker():
    def __init__(self):
        pass

    def itenerary_maker(self, list_of_cities, interests, budget, start_date, end_date):
        itenerary_maker_prompt = f"You are an excellent holiday planner. \
        Your role is to generate an itenerary for the cities as \
        folowws: {list_of_cities} to identify ket interests and destinations \
        meeting the interests of the user as folowws: {interests}.\
        first unpack the list of the cities and for each city create an itenerary within \
        thge budget {budget} in Dollars.\
        the itenerary should be planned between {start_date} and {end_date}.\
        add some fun and rexation into the itenerary"
        with st.chat_message("user"):
            print("----- streaming request -----")
            stream = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": getenv("APP_URL"),
                    "X-Title": getenv("APP_TITLE"),
                },
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": itenerary_maker_prompt,
                    },
                ],
                stream=True,)
            response = st.write_stream(stream)
            return response

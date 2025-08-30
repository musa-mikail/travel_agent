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


def destination_planning(interests, budget, start_date, end_date):
    destination_planner_prompt = f"You are an excellent holiday planner.\
    Your role is to generate a high level selection of cities that match\
    the interests of the user as follows: {interests}, and meeting the budget\
    of the user indicated as {budget} in Dollars. The plan should\
    return cities that have great weather between {start_date} and {end_date}.\
    return only the top 3 cities as an input compatible for another agent\
    to prepare itenerary of activities for each cities."
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

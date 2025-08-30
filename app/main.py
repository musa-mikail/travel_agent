import streamlit as st
from agents import DestinationPlanner, IteneraryMaker

DestinationPlanner = DestinationPlanner()
IteneraryMaker = IteneraryMaker()
st.session_state.messages = []
st.title(":green[_My first Streamlit Application_]:rocket:")
st.write("This is a simple application build by :blue[Musa Mikail] that help \
         You plan a holiday using an AI agent.\
          Provide your preferences below and allow the agent to serve you.")
interests = st.text_input("Enter your interests (e.g food,beaches, culture,\
                           etc) here separated by comma:")
budget = st.text_input("Enter your budget here in USD:")
dates_start = st.date_input("Enter your travel start date here:")
dates_end = st.date_input("Enter your travel end date here:")
st.write("Once you are done inputing your data, Please click button below to\
          begin....")

if st.button("Lets begin"):
    st.write(":blue[I will start by identifying cities relevant\
              to your interests...]")
    response = DestinationPlanner.destination_planning(interests, budget, dates_start, dates_end)
    st.session_state.messages.append({"role": "user", "content": response})
    st.write(":blue[Now I will generate iteniraries for you to \
             make the best of your stay at each location...]")
    response = None
    response = IteneraryMaker.itenerary_maker(response, interests, budget, dates_start, dates_end)
    st.session_state.messages.append({"role": "user", "content": response})
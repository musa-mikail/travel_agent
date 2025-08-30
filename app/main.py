import streamlit as st
from .agents import destination_planning


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
    st.write("Planning your holiday now....")
    st.write(":Blus[Starting with Planning the whole trip ....]")
    response = destination_planning(interests, budget, dates_start, dates_end)
    st.session_state.messages.append({"role": "user", "content": response})
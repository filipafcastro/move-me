import openai
import streamlit as st

import credentials

st.title("WOD Generator")

experience = st.selectbox(
    'For how many years have you been doing crossfit?',
    ('less than 2', 'between 2 and 5', 'more than 5'))

type = st.selectbox(
    'What do you prefer to work today?',
    ('cardio', 'strength'))

mode = st.selectbox(
    'AMRAP or for time?',
    ('AMRAP', 'For time'))

# Set the API key for the OpenAI API
openai.api_key = credentials.openai_api_key

# Set the model to use
model_engine = "text-davinci-002"

if st.button('Give me a WOD'):
    # Set the prompt for the model
    prompt = f"Give me a crossfit {type} wod focused on {type} given that I have {experience} years experience in crossfit"

    # Generate a response from the model
    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)

    # Print the response
    st.write(response.choices[0].text)


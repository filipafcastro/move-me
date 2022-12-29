import openai
import streamlit as st

st.title("WOD Generator")

type = st.selectbox(
    'What do you prefer to work today?',
    ('cardio', 'strength'))

mode = st.selectbox(
    'AMRAP or for time?',
    ('AMRAP', 'for time'))

# Set the API key for the OpenAI API
openai.api_key = st.secrets["openai_api_key"]

# Set the model to use
model_engine = "text-davinci-002"

if st.button('Give me a WOD'):
    # Set the prompt for the model
    prompt = f"Recommend me a crossfit workout of the day of type {mode} focused on {type}"

    # Generate a response from the model
    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)

    # Print the response
    st.write(response.choices[0].text)


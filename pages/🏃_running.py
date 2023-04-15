import openai
import streamlit as st

st.title("Running training plan")

distance = st.selectbox(
    'How much do you want to run?',
    ('5 km', '10 km', 'half-marathon', 'marathon'))

time = st.selectbox(
    'How many months do you have to prepare?',
    ('1', '2', '3', '4', '6', '8', '10', '12'))

# Set the API key for the OpenAI API
openai.api_key = st.secrets["openai_api_key"]

# Set the model to use
model_engine = "text-davinci-002"

if st.button('Give me a training plan'):
    # Set the prompt for the model
    prompt = f"I wish to be able to run {distance} in {time} months' time. Outline a running plan for me to follow each month in order to achieve this"
    st.write(prompt)

    # Generate a response from the model
    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)

    # Print the response
    st.write(response.choices[0].text)
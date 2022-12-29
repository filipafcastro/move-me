import openai
import streamlit as st

st.title("Yoga Practice")

type = st.selectbox(
    'What type of yoga do you prefer?',
    ('hatha', 'vinyasa', 'power'))

time = st.selectbox(
    'How much time do you have (minutes)?',
    ('10', '20', '30', '45', '60'))

# Set the API key for the OpenAI API
openai.api_key = st.secrets["openai_api_key"]

# Set the model to use
model_engine = "text-davinci-002"

if st.button('Give me a yoga workout'):
    # Set the prompt for the model
    prompt = f"Recommend me a workout to practice {type} yoga during {time} minutes"
    st.write(prompt)

    # Generate a response from the model
    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)

    # Print the response
    st.write(response.choices[0].text)
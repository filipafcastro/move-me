# 🏃‍♀️ MOVE ME

## 🔥 Motivation

I'm passionate and enthusiastic about both sports and AI. When [ChatGPT](https://openai.com/blog/chatgpt) was announced in November 2022, and later the API, I immediately started to ideate how such technology could expand my experience with sports. The thing I love the most about crossfit is how different is it everyday. So, what if anyone who is at home can experience the same? One click, less excuses not to move

## 👩‍💻 Implementation

As a data scientist, I work with Python everyday, so the choice became easy. I also wanted to test some new features of Streamlit, such as the multipage and hosting a dashboard in Streamlit Cloud. ChatGPT has shown us that the UI is key for people to actually use and benefit from the techonology, then Streamlit makes even more sense. Let's go 🚀

## 🤖 Features

### 🏋️ Crossfit
generate your workout of the day. "For time" means you need to complete the workout in the minimum amount of time. "AMRAP" = "As many repetitions as possible" means you have a fixed amount of time and need to complete as many rounds and/or repetitions possible.

### 🏃‍♀️ Running
generate a training plan for a specific distance and calendar

### 🧘 Yoga
generate a yoga workout by choosing your favorite type of yoga and the ideal time frame

## 🏃‍♀️ (literally) running it

### Local Setup
1. Clone the repo
`git clone https://github.com/filipafcastro/move-me.git`

2. Create a virtual environment

```
python -m venv env
```

3. Activate your virtual environment

```
# Linux:

source env/bin/activate

# Windows

env\Scripts\activate.bat
```
4. Install the requirements
`pip install -r requirements.txt`

5. Fill the file `.streamlit/credentials.toml` with your own OpenAI API Key

6. Run streamlit
`streamlit run 🏋️_crossfit.py`

### Streamlit Cloud
1. Fork the repo to your github account

2. Follow the steps to create a Community Cloud account in Streamlit and connect it to your GitHub: https://docs.streamlit.io/streamlit-community-cloud/get-started

3. Set up the OpenAI API Key in the Cloud app: https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management

4. Launch the app 🚀

## 📈 Improvements

- Prompt engineering to get better answers
- Finetuning on known wods
- Additional sports

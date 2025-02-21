import streamlit as st
from transformers import pipeline

# Page Configuration
st.set_page_config(page_title="AI Study Planner", page_icon="📘")

# Add Logo
st.image("logo bud.jpg", width=100)

# Title and Introduction
st.title("AI Study Planner")
st.write("Welcome to your AI-powered study planner! This tool helps you create a personalized study schedule tailored to your goals and available time.")

# Load Hugging Face Models
st.write("Loading AI models...")
if 'study_model' not in st.session_state:
    st.session_state['study_model'] = pipeline("text-generation", model="gpt2")
if 'chat_model' not in st.session_state:
    st.session_state['chat_model'] = pipeline("text2text-generation", model="t5-small")
st.success("Models loaded successfully!")

# User Input for Study Plan
st.header("Create Your Study Plan")
subjects = st.text_input("Enter the subjects you want to study (comma-separated):", placeholder="e.g., Math, Science, History,programming language")
goal = st.text_area("What is your study goal?", placeholder="e.g., Prepare for finals, learn a new topic, etc.")
available_hours = st.slider("How many hours can you study per day?", 1, 12, 4)

generate_plan = st.button("Generate Study Plan")

# Generate Study Plan
if generate_plan:
    if subjects and goal:
        input_text = f"Create a study plan for the subjects: {subjects}. The goal is: {goal}. Available hours per day: {available_hours}."
        with st.spinner("Generating your study plan..."):
            study_plan = st.session_state['study_model'](input_text, max_length=200, num_return_sequences=1)[0]['generated_text']
        st.subheader("Your Personalized Study Plan")
        st.write(study_plan)
    else:
        st.warning("Please fill in all the fields to generate your study plan.")

# AI Chat Box
st.header("AI Chat Bot")
st.write("Ask any question and get instant answers from the AI bot.")
user_question = st.text_input("Enter your question:", placeholder="e.g., What is the best way to study math?")
ask_bot = st.button("Ask AI Bot")

if ask_bot:
    if user_question:
        with st.spinner("AI is thinking..."):
            bot_response = st.session_state['chat_model'](user_question, max_length=100, num_return_sequences=1)[0]['generated_text']
        st.subheader("AI Bot Response")
        st.write(bot_response)
    else:
        st.warning("Please enter a question to ask the AI bot.")

# Footer
st.write("---")
st.write("Developed using Streamlit and Hugging Face Transformers.")

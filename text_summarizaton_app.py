pip install streamlit transformers torch
import streamlit as st
from transformers import pipeline

# Load the summarization model from Hugging Face
summarizer = pipeline("summarization")

# Set up the Streamlit app
st.title("Text Summarization App")
st.markdown("*Developed by Fatima*")
st.write("Enter the text you want to summarize below:")
# Text input from the user
text_input = st.text_area("Text Input", height=300)

# Button to trigger summarization
if st.button("Summarize"):
    if text_input:
        # Perform summarization
        summary = summarizer(text_input, max_length=150, min_length=30, do_sample=False)
        # Display the summary
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter some text to summarize.")

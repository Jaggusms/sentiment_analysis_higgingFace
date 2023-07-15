import streamlit as st
from transformers import pipeline
 # 👈 Add the caching decorator
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

query = st.text_input("Your query")
if query:
    result = model(query)[0]  # 👈 Classify the query text
    st.write(result["label"])

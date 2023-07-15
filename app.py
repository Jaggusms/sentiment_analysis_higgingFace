import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch
 # 👈 Add the caching decorator
@st.cache(allow_output_mutation=True)
def get_model():
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained("ProsusAI/finbert")
    return tokenizer,model
#model = load_model()

query = st.text_input("Your query")
if query:
    #result = model(query)[0]  # 👈 Classify the query text
    #st.write(result["label"])
    st.write("hi")

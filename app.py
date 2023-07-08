import streamlit as st
from transformers import pipeline,logging
logging.set_verbosity_error()
classifier=pipeline("text-classification")
with st.form("form",clear_on_submit=True):
    comments=st.text_area(label="Sentiment analysis of the Comments")
    out=st.form_submit_button("Submit")
    if out:
        res=classifier(comments)
        st.success("response: "+res[0]['label']+" confidence: "+str(int(float(res[0]['score'])*100))+"% comment:  "+ comments)
import streamlit as st
from transformers import BertForSequenceClassification, BertTokenizer

model = BertForSequenceClassification.from_pretrained("pelle112112/ResumeLabelBert")
tokenizer = BertTokenizer.from_pretrained("pelle112112/ResumeLabelBert")



st.title("Select model for resume screening")

st.write(
    "This is a simple app to select the model for resume screening. Please select the model you want to use."
)

inputText = st.text_area("Enter the text to be classified:")
if st.button("Classify"):
    inputs = tokenizer(inputText, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()
    st.write(f"Predicted class: {predicted_class}")
    



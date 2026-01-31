import streamlit as st
import pickle
import re
import string

# Load the trained model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Text cleaning function (same as training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

st.title("Fake News Detection System")

news_text = st.text_area("Enter News Text")

if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter some text")
    else:
        cleaned = clean_text(news_text)
        vect = vectorizer.transform([cleaned])
        pred = model.predict(vect)[0]
        prob = model.predict_proba(vect)[0]

        if pred == 1:
            st.success(f"Real News ({round(prob[1]*100,2)}%)")
        else:
            st.error(f"Fake News ({round(prob[0]*100,2)}%)")

import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

def transform_text(text):
    ps = PorterStemmer()

    text=text.lower()
    text=nltk.word_tokenize(text)
    ans=[]
    for i in text:
        if i.isalnum():
            ans.append(i)
    text=ans[:]
    ans.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            ans.append(i)
    text=ans[:]
    ans.clear()
    for i in text:
        ans.append(ps.stem(i))
    return " ".join(ans)




st.title("Email and SMS Spam classifier")

input_sms=st.text_area("Please enter the email/sms want to verify")
v = pickle.load(open('vectorizer1.pkl','rb'))
model = pickle.load(open('model1.pkl','rb'))

if st.button("Verify"):
    # preprocess
    transform_sms=transform_text(input_sms)

    # vectorize
    vector_input= v.transform([transform_sms])

    # model run
    result= model.predict(vector_input)[0]

    if result == 1:
        st.header("SPAM")
    else:
        st.header("NOT A SPAM")
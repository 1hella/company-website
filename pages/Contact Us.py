import streamlit as st
import pandas

from send_email import send_email

df = pandas.read_csv('topics.csv')
print(df['topic'])
print(type(df['topic']))
topics = []

for index, row in df.iterrows():
    topics.append(row['topic'])


with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    topic = st.selectbox("What topic do you want to discuss?", topics)
    text = st.text_area("Text")
    button = st.form_submit_button("Submit")
    if button:
        message = f"""Subject: New email from {user_email}

        From: {user_email}
        Topic {topic}
        {text}
        """
        send_email(message)


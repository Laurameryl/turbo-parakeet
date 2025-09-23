import streamlit as st
from chatbot import chatbot_response
from speech_utlis import transcribe_speech

st.title("🎤 Speech-Enabled Chatbot")

st.write("You can chat using **text** or **voice input**.")

# User input mode
mode = st.radio("Choose input method:", ("Text", "Speech"))

if mode == "Text":
    user_input = st.text_input("Type your message here:")
    if st.button("Send"):
        if user_input:
            response = chatbot_response(user_input)
            st.success(f"🤖 Bot: {response}")

elif mode == "Speech":
    st.write("Click the button and start speaking...")
    if st.button("🎙️ Record Speech"):
        text = transcribe_speech()
        st.info(f"🗣️ You said: {text}")
        response = chatbot_response(text)
        st.success(f"🤖 Bot: {response}")


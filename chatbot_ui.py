import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the model
model = ChatOpenAI()

# Set up the Streamlit page app title
st.title("🤖 LangChain Chatbot")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# React to user input
if user_input := st.chat_input("Say something..."):
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.write(user_input)
        
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response from the LangChain model
    # Note: Fixed the bug in your original code where 'user_input' was a string literal
    response = model.invoke(user_input)
    ai_response = response.content

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.write(ai_response)
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

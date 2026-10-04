import streamlit as st

st.set_page_config(
    page_title="Course AI Chatbot",
    page_icon="🎓"
)

st.title("🎓 Course AI Chatbot")

st.write("Welcome! Your Streamlit app is working.")

st.success("Streamlit is working correctly!")

subject = st.selectbox(
    "Choose a subject:",
    [
        "Python",
        "Java",
        "DBMS",
        "Data Structures",
        "Operating Systems",
        "Computer Networks",
        "Artificial Intelligence"
    ]
)

st.write("Selected subject:", subject)

question = st.text_input("Ask your question:")

if question:
    st.write("Your question:", question)
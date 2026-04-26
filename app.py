import streamlit as st

st.set_page_config(page_title="AI Writing Assistant")

st.title("AI Writing Assistant")
st.write("Paste text and choose how you want it itransformed.")

user_text = st.text_area("Enter text here", height = 200)

task = st.selectbox( "Choose a task", 
    [
        "Rewrite for clarity",
        "summarize",
        "Make more formal",
        "Make more informal",
    ])

if st.button("Generate"):
    if not user_text.strip():
        st.warning("Please enter some text to transform.")
    else:
        st.subheader("Result")
        st.write(f"**Task:** {task}")
        st.write("This is where AI response will go.")
import streamlit as st
import os
from dotenv import load_dotenv
from cerebras.cloud.sdk import Cerebras

load_dotenv()

cerebras_key = os.getenv("CEREBRAS_API_KEY")

if not cerebras_key:
    st.error("CEREBRAS_API_KEY not found in .env file.")
    st.stop()
client = Cerebras(api_key=cerebras_key)

st.set_page_config(page_title="AI Writing Assistant")

st.title("AI Writing Assistant")
st.write("Paste text and choose how you want it transformed.")

user_text = st.text_area("Enter text here", height = 200)

task = st.selectbox( "Choose a task", 
    [
        "Rewrite for clarity",
        "Summarize",
        "Make more formal",
        "Make more informal",
    ]
)

def build_prompt(task, text):
    prompts = {
        "Rewrite for clarity": f"Rewrite the following text for clarity:\n\n{text}",
        "Summarize": f"Summarize the following text:\n\n{text}",
        "Make more formal": f"Make the following text more formal:\n\n{text}",
        "Make more informal": f"Make the following text more informal:\n\n{text}",
    }
    return prompts[task]

if st.button("Generate"):
    if not user_text.strip():
        st.warning("Please enter some text to transform.")
    elif not cerebras_key:
        st.error("API key not found. Please set your CEREBRAS_API_KEY in the environment variables.")
    else:
        try:
            prompt = build_prompt(task, user_text)

            with st.spinner("Generating..."):
                response = client.chat.completions.create(
                    model="gpt-oss-120b",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1024,
                    temperature=0.2
                )
            result = response.choices[0].message.content

            st.subheader("Transformed Text")
            st.write(result)

        except Exception as e:
            st.error(f"An error occurred: {e}")
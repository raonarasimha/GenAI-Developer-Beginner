import streamlit as st

class GenAIChatBot:
    def ask(self, prompt):
        return f"[Mocked OpenAI reply to: '{prompt}']"

if __name__ == "__main__":
    st.title("GenAI Chatbot")
    prompt = st.text_input("Enter your prompt:")
    if st.button("Ask"):
        response = GenAIChatBot().ask(prompt)
        st.write(response)

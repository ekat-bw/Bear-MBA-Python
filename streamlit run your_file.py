import openai
import streamlit as st


# Function to generate a suggestion
def get_suggestion(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=1.0,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()

st.title("Ask OpenAI's GPT-3")

# Main program loop
user_input = st.text_input("Define for me: ")
if st.button("Ask"):
    prompt = "Define this as accurately as possible: " + user_input + "\nChatGPT:"
    suggestion = get_suggestion(prompt)
    st.write("ChatGPT:", suggestion)

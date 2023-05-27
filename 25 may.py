import openai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to generate a suggestion
def get_suggestion(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()

# Main program loop
while True:
    user_input = input("I want to do something new: ")
    prompt = "I am bored. What should I do next?" + user_input + "\nChatGPT:"
    suggestion = get_suggestion(prompt)
    print("ChatGPT:", suggestion)

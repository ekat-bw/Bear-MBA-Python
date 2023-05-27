import openai

# Set up your OpenAI API key
openai.api_key = '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'

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

# Main program loop
while True:
    user_input = input("Define for me: ")
    prompt = "Define this as accurately as possible?" + user_input + "\nChatGPT:"
    suggestion = get_suggestion(prompt)
    print("ChatGPT:", suggestion)

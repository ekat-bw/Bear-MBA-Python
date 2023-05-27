Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import openai
... 
... # Set up your OpenAI API key
... openai.api_key = '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'
... 
... # Function to generate a suggestion
... def get_suggestion(prompt):
...     response = openai.Completion.create(
...         engine='text-davinci-003',
...         prompt=prompt,
...         max_tokens=50,
...         temperature=0.7,
...         n=1,
...         stop=None,
...         timeout=10
...     )
...     return response.choices[0].text.strip()
... 
... # Main program loop
... while True:
...     user_input = input("I want to do something new: ")
...     prompt = "I am bored. What should I do next?" + user_input + "\nChatGPT:"
...     suggestion = get_suggestion(prompt)
...     print("ChatGPT:", suggestion)

import google.generativeai as genai

genai.configure(api_key='AIzaSyDSLFSxUP1yfA3cKjRy4B7Dp0v0a9cjqBQ')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)
#testing gui
# while True:
#     user_input = input('You : ')
#     if user_input.lower() in ['quit', 'exit', 'bye']:
#         break
#     response = chat_session.send_message(user_input)
#     print(response.text)
#     print('\n \n')


def chatRequest(user_input):
    response = chat_session.send_message(user_input)
    return response.text
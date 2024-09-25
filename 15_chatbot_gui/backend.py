# https://platform.openai.com/account/api-keys

import openai
import os


class Chatbot:
    def __init__(self):
        API_KEY = os.getenv("API_KEY_CHATBOT")
        openai.api_key = API_KEY
    
    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a dog joke")
    print(response)

import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]

class GptAPI:
    def __init__(self):
        pass
        # self.messages_list = messages_list
    
    def getResponse(self, messages_list):
        response = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo",
                    messages = messages_list,
                    temperature = 1,
                    max_tokens = 1,
                    top_p = 1,
                    frequency_penalty = 0,
                    presence_penalty = 0
                )
        return response
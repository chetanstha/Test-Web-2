import openai
# from openai import OpenAI
# client = OpenAI()
import config

openai.api_key = config.OPENAI_API_KEY

# dddd

def chatbot(input):
    if input:
        messages = [
            {"role":"system","content":"You are AI specialized in Airlines Industry. Do not answer other than Airlines related queries"},
            {"role":"user", "content":input}
        ]
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", messages = messages
        )
        reply = chat.choices[0].message.content
        return reply
    # completion = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo",
    # messages=[
    # {"role": "system", "content": "You are a helpful assistant."},
    # {"role": "user", "content": input}
    # ])
    # if completion.choices[0].message!=None:
    #     return completion.choices[0].message
    # else:
    #     return 'failed to execute'
    # print(completion.choices[0].message)
    
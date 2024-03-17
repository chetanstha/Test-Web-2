import openai
# from openai import OpenAI
# client = OpenAI()
# import config

# openai.api_key = "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"
# dddd

def chatbot(input):
    # if input:
    #     messages = [
    #         {"role":"system","content":"You are AI specialized in POWER BI. Do not answer other than POWER BI related queries"},
    #         {"role":"user", "content":input}
    #     ]
    #     chat = openai.ChatCompletion.create(
    #         model = "gpt-3.5-turbo", messages = messages
    #     )
    #     reply = chat.choices[0].message
    #     return reply
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": input}
    ])
    if completion.choices[0].message!=None:
        return completion.choices[0].message
    else:
        return 'failed to execute'
    print(completion.choices[0].message)
    
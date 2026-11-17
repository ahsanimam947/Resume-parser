import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha h bhai")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"
# 3 prompts
prompt1="hi"
prompt2="explain time travel in detail"
prompt3="write a 1000 word essay on machine learning"

# make a list
prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
        "role":role,
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages)

# prompt="Explain python in s imple words"
# message={
#     "role":role,
#     "content":prompt
# }
# messages=[message]

# response=client.chat.completions.create(model=model, messages=messages)
# print(response)

# print("###############################")
# answer=response.choices[0].message.content
# print(answer)
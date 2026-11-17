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
prompt="suggest a name for my food compony"
message_system={
    "role":"system",
    "content":"you are a brand manager who suggests name for my food compony. name should be in words"
    # "content":"you are my loving girlfreind "
    # "content": "you are my strict collegue who is also my office colleage
}
message={
    "role":role,
    "content":prompt
}
messages=[message_system,message]

response=client.chat.completions.create(model=model, messages=messages)
# print(response)

print("###############################")
answer=response.choices[0].message.content
print(answer)
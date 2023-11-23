import telegram
import asyncio
from openai import OpenAI

client = OpenAI(
  api_key="{my_gpt_api_key}"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "너는 지금부터 훌륭한 소설가야."},
    {"role": "user", "content": " 짧은 동화 하나 써줘. json"}
  ],
  response_format={"type": "json_object"}
)

token = "{my_token}"
bot = telegram.Bot(token=token)
chat_id = "{my_chat_id}"
text = completion.choices[0].message.content
print(text)
asyncio.run(bot.sendMessage(chat_id=chat_id, text=text))


print(completion.choices[0].message.content)
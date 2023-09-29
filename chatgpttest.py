import os
import openai
from dotenv import load_dotenv #.envファイルから読み取る方法だが適応されていない気がする
load_dotenv()

openai.organization = "org-YUPK4NI7XPStw9x9n6GAxRpe"
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.Model.list()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
print(response)
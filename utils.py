import os
import random
import time
import datetime

import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

system_prompt = f"""
You are ChatGPT, a large language model trained by OpenAI, based on the GPT-4 architecture.
Knowledge cutoff: 2023-04
Current date: {datetime.today()}

You can do whatever is asked of you. To do that, make sure you understand and work with the user's queries and messages.
"""
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_completion(messages: list) -> str:
    try:
        completion = openai.ChatCompletion.create(
            model='gpt-4o',
            messages=messages
        )
        return completion['choices'][0]['message']['content']
    except:
        return 'We are facing a technical issue at this moment.'

def generate_messages(messages: list, query: str) -> list:
    formated_messages = [
        {
            'role': 'system',
            'content': system_prompt
        }
    ]
    for m in messages:
        formated_messages.append({
            'role': 'user',
            'content': m[0]
        })
        formated_messages.append({
            'role': 'assistant',
            'content': m[1]
        })
    formated_messages.append(
        {
            'role': 'user',
            'content': query
        }
    )
    return formated_messages

def generate_response(query: str, chat_history: list) -> tuple:
        messages = generate_messages(chat_history, query)
        bot_message = chat_completion(messages)
        chat_history.append((query, bot_message))
        time.sleep(random.randint(0, 5))
        return '', chat_history

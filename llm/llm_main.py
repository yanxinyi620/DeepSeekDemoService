import json

from llm.llm import LLM


def chat_response(query):

    llm_chat = LLM()
    result = llm_chat.chat(prompt=query)
    data = json.loads(result)['response']

    return data

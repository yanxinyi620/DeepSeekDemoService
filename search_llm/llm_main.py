import json

from search_llm.llm_query import LLMQuery


def get_llm_result(query):

    llm_query = LLMQuery()
    result = llm_query.query(prompt=query)
    data = json.loads(result)['response']

    return data.replace('<think>\n\n', '').replace('</think>\n\n', '')

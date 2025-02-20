import requests
import json


BASE_URL="http://localhost:11434/api/generate"


class LLMQuery:

    def __init__(self, query=None, query_id=0, query_type=None, query_time=None, base_url=BASE_URL):
        self.prompt = query
        self.query_id = query_id
        self.query_type = query_type
        self.query_time = query_time
        self.base_url = base_url

        if self.prompt is not None:
            result = self.query(prompt=self.prompt)
            return result

    def query(self, prompt=None, model='deepseek-r1:1.5b', stream=False):
        """
        向DeepSeek API发送查询请求。
        
        :param prompt: 要发送给模型的提示文本
        :param model: 要使用的模型名称，例如"deepseek-r1:1.5b"
        :param stream: 是否以流的方式接收响应，默认为False
        :return: API响应的内容（JSON格式）
        """
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }
        
        response = requests.post(self.base_url, headers=headers, data=json.dumps(data))
        
        # 检查响应状态码
        if response.status_code == 200:
            # return response.json()
            result = response.json()
            if 'response' in result:
                response_text = result['response']
                # 打印response字段，确保中文能够正确显示
                return json.dumps({"response": response_text}, indent=2, ensure_ascii=False)
            else:
                print("响应中没有找到'response'字段")
                return json.dumps(result, indent=2, ensure_ascii=False)  # 打印整个响应以调试

        else:
            response.raise_for_status()  # 如果状态码不是200，则抛出HTTPError异常


# 使用示例
if __name__ == "__main__":
    llm_query = LLMQuery()
    result = llm_query.query(prompt="你是谁?", model="deepseek-r1:1.5b")
    # print(json.dumps(result, indent=2))
    data = json.loads(result)['response']
    print(data.replace('<think>\n\n', '').replace('</think>\n\n', ''))

import requests
import json


BASE_URL="http://localhost:11434/api/"


class LLM:

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def chat(self, prompt=None, model='deepseek-r1:1.5b', dialogue=[], role='user', stream=False):
        """
        向DeepSeek API发送chat请求。
        
        :param prompt: 要发送给模型的提示文本
        :param model: 要使用的模型名称，例如"deepseek-r1:1.5b"
        :param stream: 是否以流的方式接收响应，默认为False
        :return: API响应的内容（JSON格式）
        """
        headers = {
            'Content-Type': 'application/json'
        }
        messages = dialogue + [{
            "role": role,
            "content": prompt,
            "images": []
            }]

        data = {
        "model": model,
        "options": {},
        "messages": messages,
        "stream": stream
        }

        response = requests.post(self.base_url + 'chat', headers=headers, data=json.dumps(data))
        
        # 检查响应状态码
        if response.status_code == 200:
            # return response.json()
            result = response.json()
            if 'message' in result:
                response_text = result['message']
                # 打印response字段，确保中文能够正确显示
                return json.dumps({"response": response_text}, indent=2, ensure_ascii=False)
            else:
                print("响应中没有找到'message'字段")
                return json.dumps(result, indent=2, ensure_ascii=False)  # 打印整个响应以调试

        else:
            response.raise_for_status()  # 如果状态码不是200，则抛出HTTPError异常


# 使用示例
if __name__ == "__main__":
    llm = LLM()
    # 单轮对话
    result = llm.chat(prompt="你是谁?", model="deepseek-r1:1.5b")
    data = json.loads(result)['response']
    print(data['content'].replace('<think>\n\n', '').replace('</think>\n\n', ''))

    # 多轮对话
    dialogue = [{"role": 'user', "content": '你是谁?'}] + [data]
    result2 = llm.chat(prompt="你能做什么?", dialogue=dialogue)
    data2 = json.loads(result2)['response']
    print(data2['content'].replace('<think>\n\n', '').replace('</think>\n\n', ''))

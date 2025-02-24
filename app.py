from flask import Flask, render_template, request, jsonify
import random
import time

from llm.llm_main import chat_response


app = Flask(__name__)


def generate_results(query):
    """生成模拟搜索结果"""
    time.sleep(random.random())  # 模拟处理延迟
    
    chat_result = chat_response(query)
    chat_result = chat_result['content'].replace('<think>\n\n', '').replace('</think>\n\n', '')

    # 添加动态内容
    dynamic_results = [{
        "title": f"{query} - deepseek",
        "url": f"https://chat.deepseek.com/",
        "description": f"{chat_result}"
    }]

    return dynamic_results  # 返回1个结果


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('q', '').strip()
    if not query:
        return jsonify({"error": "搜索内容不能为空"}), 400
    
    results = generate_results(query)
    return jsonify({"results": results})


if __name__ == '__main__':
    app.run(debug=True, port=5000)

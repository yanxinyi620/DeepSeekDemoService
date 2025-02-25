from flask import Flask, render_template, request, jsonify
import random
import time

from llm.llm_main import chat_response, format_response


app = Flask(__name__)


def generate_results(query):
    """生成模拟搜索结果"""
    time.sleep(random.random())  # 模拟处理延迟
    
    # chat_response 耗时较长
    chat_result = chat_response(query)
    if chat_result is None:
        return [{"title": f"无产品推荐", 
                 "url": "", 
                 "description": f"未找到关于{query}的任何信息，无法进行产品推荐，请确认后再次搜索。"}]

    # 格式化 chat_response 结果
    query_result = format_response(chat_result)

    # 添加动态内容
    dynamic_results = []
    for product in query_result['recommended_products']:
        dynamic_results.append({
            "title": f"{product['产品名称']}",
            "url": f"推荐理由: {product['推荐理由']}",
            "description": f"金融封控点: {product['金融封控注意事项']}",
        })
    
    return dynamic_results


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
    # app.run(debug=True, port=5000)
    app.run(port=5000)

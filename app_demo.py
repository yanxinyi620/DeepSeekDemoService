from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

# 模拟搜索数据库
sample_results = [
    {
        "title": "Python 官方文档",
        "url": "https://www.python.org",
        "description": "欢迎来到 Python 官方网站！在这里您可以下载最新版本的 Python..."
    },
    {
        "title": "Flask 框架文档",
        "url": "https://flask.palletsprojects.com",
        "description": "Flask 是一个轻量级的 WSGI Web 应用框架。它旨在使..."
    },
    {
        "title": "GitHub 代码托管平台",
        "url": "https://github.com",
        "description": "GitHub 是使用 Git 版本控制系统的互联网托管服务..."
    }
]

def generate_results(query):
    """生成模拟搜索结果"""
    time.sleep(0.5)  # 模拟处理延迟
    
    # 随机排序并添加相关性分数
    results = sample_results.copy()
    random.shuffle(results)
    
    # 添加动态内容
    dynamic_results = [{
        "title": f"{query} - 知乎专栏",
        "url": f"https://zhihu.com/search?q={query}",
        "description": f"在知乎上关于 {query} 的讨论，超过 1000 条相关回答..."
    }, {
        "title": f"{query} 技术博客",
        "url": f"https://blog.example.com/{query}",
        "description": f"最新关于 {query} 的技术文章分享，包含实战案例解析..."
    }]
    
    return dynamic_results + results[:3]  # 返回5个结果

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
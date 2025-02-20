## 背景

### 简介

- Ollama（框架）
  - Ollama是一个专为在本地机器上便捷部署和运行大型语言模型（LLM）而设计的开源框架。Ollama允许用户在自己的本地设备上运行语言模型，从而提高了数据隐私性，因为用户的输入和模型处理过程都在本地环境，不会将敏感数据发送到外部服务器。
- deepseek（模型）
  - DeepSeek是一款由杭州深度求索人工智能基础技术研究有限公司打造的先进AI应用。它集自然语言处理（NLP）、计算机视觉（CV）、语音识别等多个领域的先进技术于一体，为用户提供了高效、便捷的AI模型训练、部署和应用服务。
- Open WebUI（网页UI）
  - Open WebUI（前身为Ollama WebUI）是一个可扩展的、功能丰富的、用户友好的自托管Web界面，设计用于完全离线运行。它支持各种LLM（大型语言模型）运行器，包括Ollama和兼容OpenAI的API。
- Page Assist（网页UI，谷歌拓展）
  - A Web UI for Local AI Models（本地 AI 模型的 Web UI）

### 功能

Ollama、DeepSeek和Open WebUI 组合使用可以实现一个功能强大的本地化AI应用开发和部署平台，具体可以实现以下功能：

**1. 本地化AI模型部署和推理:**

- **Ollama:**  作为本地化大模型部署工具，可以将DeepSeek等大模型部署到本地服务器或个人电脑上，无需依赖云端服务，保障数据隐私和安全。
- **DeepSeek:**  作为强大的大语言模型，提供自然语言理解、文本生成、代码生成等能力，为应用提供智能核心。
- **Open WebUI:**  作为开源的可视化界面框架，可以快速构建用户友好的Web界面，方便用户与本地部署的AI模型进行交互。

**2. 定制化AI应用开发:**

- 利用Ollama和DeepSeek的组合，开发者可以根据特定需求对模型进行微调，开发出适用于不同场景的定制化AI应用，例如：
  - **智能客服:**  基于本地知识库，提供更精准、高效的客户服务。
  - **个性化推荐:**  根据用户历史数据和偏好，提供个性化的产品、服务或内容推荐。
  - **智能写作助手:**  帮助用户进行文本创作、翻译、摘要生成等。
  - **代码生成和辅助:**  根据自然语言描述生成代码，或辅助开发者进行代码调试和优化。

**3. 数据隐私和安全保障:**

- 所有数据和模型都运行在本地环境中，无需上传到云端，有效保障数据隐私和安全，特别适合处理敏感数据的应用场景。

**4. 开源和可定制:**

- Ollama、DeepSeek和Open WebUI 都是开源项目，开发者可以根据自身需求进行修改和定制，构建更符合自身业务需求的AI应用。

**具体应用场景举例:**

- **企业内部知识库问答系统:**  将企业内部文档和数据导入Ollama，利用DeepSeek模型构建智能问答系统，员工可以通过自然语言查询快速获取所需信息。
- **个人电脑上的智能写作助手:**  在个人电脑上部署Ollama和DeepSeek，利用Open WebUI构建简洁易用的写作界面，帮助用户进行邮件撰写、文案创作等。
- **教育领域的个性化学习平台:**  利用Ollama和DeepSeek构建个性化学习平台，根据学生的学习进度和知识掌握情况，提供个性化的学习内容和辅导。

**总结:**

Ollama、DeepSeek和Open WebUI 的组合为开发者提供了一个强大、灵活、安全的本地化AI应用开发和部署平台，可以应用于各种场景，推动AI技术的普及和应用。

## 本地部署(windows)

### ollama

- 官方下载[ollama](https://ollama.com/download) (下载太慢可以复制下载连接到迅雷中下载)
  - [ollama下载连接](https://objects.githubusercontent.com/github-production-release-asset-2e65be/658928958/f8b959cd-f1c8-44be-a6cc-c08edea754ea?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20250217%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250217T080653Z&X-Amz-Expires=300&X-Amz-Signature=c0bc60d4bc3b06f50488bf1505390cc3a77bdd081ea272dc614ea21780343d47&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3DOllamaSetup.exe&response-content-type=application%2Foctet-stream)

- 安装ollama
  - 默认安装C盘
  - 浏览器查看是否启动：`http://127.0.0.1:11434/`

- 修改环境变量
  - 系统变量中新增（新增后确定并重启电脑）
    - 变量：`OLLAMA_HOST`
    - 值：`0.0.0.0:11434`

### 模型

- ollama官网搜索[模型](https://ollama.com/search)
  - 选择 [deepseek-r1](https://ollama.com/library/deepseek-r1:1.5b)

- copy 运行模型命令: `ollama run deepseek-r1:1.5b`
  - 在终端管理员模式中运行上述命令即可自动下载并运行模型
  - 模型默认保存：`C:\Users\yanxi\.ollama\models`

- ollama 命令
  - 查看已有模型：`ollama list`
  - 启动ollama：`ollama serve`
  - 运行模型：`ollama run`
  - 加载官方下载模型：`ollama create`
  
  ```bash
  PS C:\Users\yanxi> ollama

  Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command
  ```

### Open WebUI

- 安装python3.11
  - 本机已有conda, git, pip环境（没有git，可以用终端）
  - git bash 运行 `conda create -n webui python=3.11`
  - git bash 运行 `conda env list`
  - git bash 运行 `conda activate webui`
  - webui 默认目录 `C:\Users\yanxi\anaconda3\envs\webui`

- 安装Open WebUI
  - git bash 运行 `pip install open-webui`
  - packages 目录 `C:\Users\yanxi\anaconda3\envs\webui\Lib\site-packages\open_webui`
  - 启动文件 `C:\Users\yanxi\anaconda3\envs\webui\Scripts\open-webui`

  ```python
  '''
  Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
  Collecting open-webui
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/3b/ff/343f33bb53b8dca936a95f3954941c4a57c3346d6a648d1d695e29efbc55/open_webui-0.5.12-py3-none-any.whl (130.9 MB)
  '''
  ```

- 启动Open WebUI
  - git bash 运行 `open-webui serve`

- 使用Open WebUI
  - 浏览器：127.0.0.1:8080

### Page Assist

- 谷歌应用商店安装Page Assist

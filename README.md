# DeepSeekDemoService

基于DeepSeek和ollama框架开发的本地大模型Demo Service

1. **本DemoService的核心是DeepSeek和ollama，web UI用户可以选择使用现有的Open WebUI（开源工具）或者Page Assist（谷歌拓展）。**
2. **本项目将不使用现有的WebUI，而是开发一个自定义的python版本服务，包含前后端服务，WebUI，通过api接口调用ollama框架的LLM（DeepSeek或者其他模型）**。

功能项完成度：

- [x] **部署安装**
- [x] **Web页面**
- [x] **问答服务**
  - [x] **单轮问答**
  - [ ] **多轮对话**
- [ ] **构建提示词**
- [ ] **构建知识库**
- [ ] **网络连接**

## 简介

- Ollama（框架）
  - Ollama是一个专为在本地机器上便捷部署和运行大型语言模型（LLM）而设计的开源框架。Ollama允许用户在自己的本地设备上运行语言模型，从而提高了数据隐私性，因为用户的输入和模型处理过程都在本地环境，不会将敏感数据发送到外部服务器。
- deepseek（模型）
  - DeepSeek是一款由杭州深度求索人工智能基础技术研究有限公司打造的先进AI应用。它集自然语言处理（NLP）、计算机视觉（CV）、语音识别等多个领域的先进技术于一体，为用户提供了高效、便捷的AI模型训练、部署和应用服务。

**总结:**

Ollama、DeepSeek和WebUI 的组合为开发者提供了一个强大、灵活、安全的本地化AI应用开发和部署平台，可以应用于各种场景，推动AI技术的普及和应用。

## 部署

[ollama & DeepSeek本地部署（windows）文档](./doc/install_windows.md)
[ollama & DeepSeek私有化部署（linux）文档](./doc/install_linux.md)

## 环境

[python 环境](./doc/install_env.md)
[数据库环境](./doc/install_env.md)

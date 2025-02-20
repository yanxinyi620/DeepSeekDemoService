## 服务器部署(linux)

```bash
# ollama
curl -fsSL https://ollama.com/install.sh | sh

# >>> Installing ollama to /usr/local
# >>> Downloading Linux amd64 bundle
# ######################################################################## 100.0%
# >>> Creating ollama user...
# >>> Adding ollama user to render group...
# >>> Adding ollama user to video group...
# >>> Adding current user to ollama group...
# >>> Creating ollama systemd service...
# >>> Enabling and starting ollama service...
# Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
# >>> The Ollama API is now available at 127.0.0.1:11434.
# >>> Install complete. Run "ollama" from the command line.
# WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.

# deepseek
ollama run deepseek-r1:1.5b
# /usr/share/ollama/.ollama/models/

# 启动deepseek
ollama run deepseek-r1:1.5b
```

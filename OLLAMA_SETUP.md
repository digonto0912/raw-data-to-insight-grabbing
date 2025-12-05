# Setup Guide: Run AI Agent Locally with Ollama (CPU-Only)

## Step 1: Install Ollama

### Windows:
1. Download Ollama from: https://ollama.com/download
2. Run the installer
3. Ollama will start automatically as a background service

### Verify Installation:
Open PowerShell and run:
```powershell
ollama --version
```

## Step 2: Download a Model

Choose ONE of these models (start with the smallest):

```powershell
# Option 1: Phi-3 (Fastest, ~2GB) - RECOMMENDED for CPU
ollama pull phi3

# Option 2: Llama 3.2 3B (Good balance, ~2GB)
ollama pull llama3.2:3b

# Option 3: Mistral 7B (Better quality, slower, ~4GB)
ollama pull mistral

# Option 4: Llama 3.1 8B (Best quality, slowest, ~4.7GB)
ollama pull llama3.1:8b
```

## Step 3: Test the Model

```powershell
ollama run phi3
```

Type a question and press Enter. Type `/bye` to exit.

## Step 4: Install LangChain Ollama Package

```powershell
pip install langchain-ollama
```

## Step 5: Update Your Agent

The agent code needs to be modified to use Ollama instead of Groq.

## Performance Expectations (Core i5 CPU)

| Model | Speed | Quality | RAM Needed |
|-------|-------|---------|------------|
| Phi-3 | ⚡⚡⚡ Fast | ⭐⭐⭐ Good | 4-8 GB |
| Llama 3.2 3B | ⚡⚡ Medium | ⭐⭐⭐⭐ Very Good | 6-8 GB |
| Mistral 7B | ⚡ Slow | ⭐⭐⭐⭐⭐ Excellent | 8-16 GB |
| Llama 3.1 8B | 🐌 Very Slow | ⭐⭐⭐⭐⭐ Excellent | 8-16 GB |

**Note:** On CPU, expect 1-5 tokens/second (vs 50-100 on GPU). Each post analysis may take 2-10 minutes depending on the model and number of comments.

## Troubleshooting

### Ollama not starting:
```powershell
# Check if Ollama is running
curl http://localhost:11434

# If not, start it manually (Windows)
# Ollama should auto-start, but you can restart your computer
```

### Out of memory:
- Use a smaller model (phi3 or llama3.2:3b)
- Close other applications
- Upgrade RAM if possible

## Next Steps

After installation, I'll update the agent code to use Ollama instead of Groq.

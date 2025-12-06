# ⚡ Speed Optimization Guide (CPU Only)

If the analysis is taking too long on your local computer (Core i5), you can switch to a faster model.

## 🚀 The Solution: Switch to Llama 3.2 (3B)

**Llama 3.2** is a smaller, more efficient model optimized for speed.
- **Speed:** ~3x faster than Mistral
- **Quality:** ~85% of Mistral (still very good for this task)
- **RAM Usage:** ~2GB (vs 4GB for Mistral)

### Step 1: Download the Faster Model
Open PowerShell and run:
```powershell
ollama pull llama3.2
```

### Step 2: Update the Code
1. Open `agent_ollama.py`
2. Find line 18:
   ```python
   MODEL_NAME = "mistral"
   ```
3. Change it to:
   ```python
   MODEL_NAME = "llama3.2"
   ```

### Step 3: Run as Normal
```powershell
python main.py
```

## 📊 Performance Comparison (Core i5)

| Model | Time per Post | Quality | Recommendation |
|-------|---------------|---------|----------------|
| **Mistral 7B** | 5-10 mins | ⭐⭐⭐⭐⭐ | Use for final deep dives |
| **Llama 3.2 3B** | 1-3 mins | ⭐⭐⭐⭐ | **Use for testing & large datasets** |
| **Phi-3.5** | 2-4 mins | ⭐⭐⭐⭐ | Good alternative |

## 💡 Pro Tip
You can use **Llama 3.2** to process the bulk of your data (989 posts), and then use **Mistral** to re-analyze the top 10 most interesting posts for maximum depth.

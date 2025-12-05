# Reddit Analysis AI Agent - Elite Market Intelligence
## 🎯 Overview
This AI agent acts as an **Elite Anthropologist & Market Intelligence Expert**. It performs a **forensic deconstruction** of Reddit threads to extract hidden value, psychological triggers, and unmet market needs with extreme precision.

It goes beyond simple summarization to identify **root causes**, **implicit desires**, and **commercial opportunities** that others miss.

## 📊 Analysis Output Structure

The agent follows a **comprehensive 17-section template** that extracts:

### Core Analysis
1. **Post Metadata** - ID, URL, timestamp, score, comments count, subreddit, age
2. **Classification** - Topic category, post type, user intent, confidence score
3. **Emotion Analysis** - Primary emotions, strength, comment emotions, clusters
4. **Pain Points** - Specific struggles, exact pain sentences, clusters, frequency
5. **Triggers** - Root causes, system limitations, environmental factors, emotional drivers

### User Insights
6. **Desires** - Explicit/implicit wants, direction of desire, exact desire sentences
7. **Behaviors** - Current tools, workarounds, failed attempts, search patterns
8. **Keywords** - High-frequency phrases, pain/desire phrases, topic keywords
9. **User Archetypes** - User types, motivations, identity indicators

### Market Opportunities
10. **Opportunities** - Market gaps, unmet needs, feature requests, manual hacks
11. **Community Consensus** - Recurring advice/complaints, myths, debates, norms
12. **Risks** - Fears, doubts, risk perceptions, edge cases
13. **Contradictions** - Conflicting viewpoints and positions

### Scoring & Context
14. **Opportunity Score** - 7 metrics (1-10 each) + final score
15. **Context** - Sarcasm detection, political context, references, sensitivity
16. **Source Evaluation** - Credibility score, bias indicators, fact-check needs
17. **Action Signals** - Willingness to pay, tool requests, calls for action

### Summary
18. **High-Level Summary** - Comprehensive actionable summary

## 🚀 Usage

### Option 1: Local (Ollama - Free, Unlimited)
```python
# In main.py, set:
USE_OLLAMA = True

# Then run:
python main.py
```

### Option 2: Cloud (Groq - Fast, Rate Limited)
```python
# In main.py, set:
USE_OLLAMA = False

# Then run:
python main.py
```

## 📁 Output Format

Each post generates a JSON file in `analysis_results/` directory:
- Filename: `analysis_{post_id}.json`
- Structure: Follows `template.json` exactly
- Contains: All 18 sections with deep insights

## 🎯 Key Features

### Deep Analysis
- ✅ Extracts **exact sentences** as evidence
- ✅ Identifies **root causes**, not just symptoms
- ✅ Detects **subtle patterns** and contradictions
- ✅ Finds **hidden pain points** in comment threads
- ✅ Calculates **opportunity scores** based on real signals

### Comprehensive Coverage
- ✅ Analyzes **every comment** carefully
- ✅ Extracts **keywords and phrases**
- ✅ Identifies **user behaviors** and workarounds
- ✅ Detects **spending signals** and willingness to pay
- ✅ Finds **market gaps** and unmet needs

## 📊 Opportunity Scoring

Each post gets scored on 7 dimensions (1-10):
1. **Pain Intensity** - How severe is the pain?
2. **Pain Frequency** - How often does it occur?
3. **Market Size** - How many people affected?
4. **Competition Gap** - How underserved is the market?
5. **Desire Strength** - How badly do they want a solution?
6. **Workaround Effort** - How much effort do workarounds require?
7. **Spending Signals** - Evidence of willingness to pay

**Final Score** = Sum of all 7 (max 70 points)

## 🔍 What Makes This Different

### Traditional Analysis
- Summarizes posts
- Lists general themes
- Misses subtle signals

### This Agent
- ✅ Extracts **exact quotes** as evidence
- ✅ Identifies **root causes** and triggers
- ✅ Finds **spending signals** and willingness to pay
- ✅ Detects **contradictions** and debates
- ✅ Calculates **objective opportunity scores**
- ✅ Provides **actionable business insights**

## 📈 Performance

### Ollama (Local - Mistral 7B)
- **Speed**: 3-10 minutes per post
- **Quality**: 85-90% of Groq
- **Cost**: $0 forever
- **Limit**: None

### Groq (Cloud - Llama 3.3 70B)
- **Speed**: 30-60 seconds per post
- **Quality**: Excellent (100%)
- **Cost**: Free tier
- **Limit**: 100k tokens/day

## 📝 Example Output

See `template.json` for the complete output structure.

Each analysis includes:
- **Evidence-based insights** with exact quotes
- **Quantified opportunity scores**
- **Actionable recommendations**
- **Market gap identification**
- **User behavior patterns**

## 🎯 Use Cases

1. **Product Development** - Find feature requests and unmet needs
2. **Market Research** - Identify market gaps and opportunities
3. **Customer Discovery** - Understand pain points and desires
4. **Competitive Analysis** - See what existing solutions lack
5. **Content Strategy** - Understand community norms and debates
6. **Pricing Strategy** - Detect willingness to pay signals

## 🔧 Configuration

Edit `main.py`:
- `USE_OLLAMA`: True for local, False for cloud
- `DATA_FILE`: "test_sample.json" or full dataset
- `OUTPUT_DIR`: Where to save results

## 📚 Files

- `models.py` - Pydantic models matching template structure
- `agent.py` - Groq cloud agent
- `agent_ollama.py` - Ollama local agent
- `main.py` - Main execution script
- `data_loader.py` - Data loading utilities
- `template.json` - Output format template

## 💡 Tips

1. **Start with test_sample.json** (5 posts) to verify setup
2. **Use Ollama for unlimited analysis** (free, local)
3. **Review opportunity scores** to prioritize insights
4. **Look for spending signals** in action_signals section
5. **Check contradictions** for market positioning opportunities

---

**Quality over speed** - This agent prioritizes deep, accurate insights over fast processing.

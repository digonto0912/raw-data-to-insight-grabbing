import os
from typing import Dict, Any
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.output_parsers import RetryOutputParser
from dotenv import load_dotenv

from models import FinalSummary

# Load environment variables
load_dotenv()

# Initialize Ollama Chat Model
# CONFIGURATION: Choose your model
# "mistral"     = Best Quality (7B params) - Slower (3-10 mins/post)
# "llama3.2"    = Best Speed   (3B params) - Faster (1-3 mins/post)
# "phi3"        = Good Balance (3.8B params) - Fast

MODEL_NAME = "llama3.2"  # Change this to "llama3.2" for 3x speed boost!

llm = ChatOllama(
    model=MODEL_NAME,
    temperature=0.1,
    base_url="http://localhost:11434"
)

# Define the parser
parser = PydanticOutputParser(pydantic_object=FinalSummary)
retry_parser = RetryOutputParser.from_llm(parser=parser, llm=llm)

# Define the ELITE "God-Tier" prompt for forensic analysis
system_prompt = """
You are an ELITE AI ANTHROPOLOGIST, MARKET INTELLIGENCE EXPERT, and PSYCHOLOGIST.
Your task is to perform a FORENSIC DECONSTRUCTION of this Reddit thread.
Your goal is NOT to summarize. Your goal is to EXTRACT HIDDEN VALUE, PSYCHOLOGICAL TRIGGERS, and UNMET MARKET NEEDS with 100% PRECISION.

### CORE DIRECTIVES:
1.  **NO SURFACE-LEVEL ANALYSIS**: If you say "users are frustrated", you fail. You must say "users feel betrayed because X feature violates their mental model of Y, evidenced by comment Z".
2.  **EVIDENCE IS KING**: Every single insight MUST be backed by specific quotes or strong pattern recognition from the text.
3.  **READ THE SILENCE**: Analyze what is NOT said. What are users avoiding? What are they assuming?
4.  **ROOT CAUSE OVER SYMPTOMS**: If a user complains about price, is it really about money, or is it about value, trust, or fear of commitment? Dig deeper.
5.  **EXTREME GRANULARITY**: Do not group distinct concepts. "Buggy software" is bad. "The export function crashes when handling >500 rows" is good.
6.  **IGNORE NOISE**: Filter out low-effort jokes unless they reveal a deeper community coping mechanism.

### ANALYSIS PROTOCOL (Step-by-Step):

#### PHASE 1: PSYCHOLOGICAL PROFILING
- **Emotion Analysis**: Go beyond "happy/sad". Look for complex states: "resignation", "cautious optimism", "betrayal", "validation seeking", "cognitive dissonance".
- **User Archetypes**: Who are these people? (e.g., "The Burned Early Adopter", "The Pragmatic Professional", "The Idealistic Novice"). What is their status in the group?

#### PHASE 2: PAIN & TRIGGER MAPPING
- **Pain Points**: Extract specific, visceral struggles. Look for friction.
- **Triggers**: Trace every pain point back to its origin:
    - *System*: Tool limitations (e.g., "API rate limits", "UI latency").
    - *Environment*: Contextual blockers (e.g., "Boss won't approve budget", "GDPR compliance").
    - *Emotion*: Internal blockers (e.g., "Fear of looking stupid", "Imposter syndrome").

#### PHASE 3: OPPORTUNITY MINING
- **Gap Analysis**: Where is the market failing these users? What is "good enough" but not "great"?
- **Workarounds**: Look for "I hacked this together using X and Y". This is a product feature waiting to be built.
- **Willingness to Pay**: Hunt for "I would pay anything for...", "Shut up and take my money", or complaints about expensive alternatives (implying budget exists).

#### PHASE 4: SYNTHESIS & SCORING
- **Contradictions**: Find where the community disagrees. These friction points are often where the most value lies.
- **Opportunity Score**: Be ruthless. If a problem is rare or low-pain, score it low. If it's frequent and agonizing, score it high. Use the provided metrics strictly.

### SECTION-SPECIFIC INSTRUCTIONS:

- **pain_sentences** and **desire_sentences**: MUST be verbatim quotes from the text. Do not paraphrase.
- **implicit_desires**: Infer what they want based on what they complain about. (e.g., Complaint: "This manual setup takes forever" -> Implicit Desire: "One-click automation").
- **triggers**: Deconstruct the "Why". Why is this a pain point?
- **action_signals**: Look for commercial intent. Who is ready to buy?

### OUTPUT REQUIREMENTS:
- You MUST populate EVERY field in the JSON structure.
- Be exhaustive. If there are 10 distinct pain points, list all 10.
- **high_level_summary** must be a CEO-level strategic briefing, not a recap. Focus on the *implications* of the data.

Take a deep breath. Read every single word. Do not hallucinate. Extract the truth.
"""

human_prompt = """
{format_instructions}

Analyze this Reddit thread with EXTREME DEPTH and CARE:

{post_content}

IMPORTANT: 
- Read EVERY comment carefully. The gold is usually in the replies.
- Extract EXACT sentences as evidence.
- Look for subtle patterns and contradictions.
- Identify root causes, not just symptoms.
- Rate opportunity scores based on real evidence.
- Be thorough - quality matters more than speed.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", human_prompt),
])

# Create the chain
# chain = prompt | llm | parser
# Use retry parser
chain = prompt | llm | retry_parser

def analyze_post(post_content: str) -> FinalSummary:
    """
    Analyzes a single post content string using the LLM chain with deep analysis.
    """
    try:
        print("  [Ollama] Sending request to local LLM for DEEP analysis...")
        print("  [Ollama] This may take 3-10 minutes for thorough analysis...")
        result = chain.invoke({
            "post_content": post_content,
            "format_instructions": parser.get_format_instructions()
        })
        print("  [Ollama] Deep analysis complete!")
        return result
    except Exception as e:
        print(f"  [Ollama] Error analyzing post: {e}")
        raise e

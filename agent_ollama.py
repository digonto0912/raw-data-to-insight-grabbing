import os
from typing import Dict, Any
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

from models import FinalSummary

# Load environment variables
load_dotenv()

# Initialize Ollama Chat Model
# Available models: phi3, llama3.2:3b, mistral, llama3.1:8b
# Smaller models = faster on CPU, larger models = better quality
llm = ChatOllama(
    model="mistral",  # Using Mistral 7B for best quality/speed balance on CPU
    temperature=0,
    base_url="http://localhost:11434"  # Default Ollama URL
)

# Define the parser
parser = PydanticOutputParser(pydantic_object=FinalSummary)

# Define the prompt
system_prompt = """
You are an expert market researcher and data analyst specializing in Reddit community analysis.
Your goal is to extract deep insights, pain points, and opportunities from a Reddit post and its comments.
You must follow a strict 10-step pipeline to ensure no signal is missed.

The 10 Steps are:
1. INPUT: Analyze the provided post title, body, and all comments.
2. CLASSIFY: Determine topic, post type, and user intent.
3. EXTRACT EMOTION: Identify primary emotions, strengths, and emotional clusters in comments.
4. PAIN POINT DISCOVERY: Find specific struggles, "can't do", "hates", "needs". Most pain is in the comments.
5. DESIRES: Identify explicit ("I wish") and implicit desires.
6. OPPORTUNITY & GAP MAPPING: Find market gaps, unmet needs, feature requests, and manual hacks.
7. USER ARCHETYPE DISCOVERY: Identify user types (beginner, expert, etc.) and motivations.
8. COMMUNITY CONSENSUS: Find recurring advice, complaints, myths, and norms.
9. RISK & BLOCKERS: Identify fears, doubts, and trust issues.
10. FINAL SUMMARY: Aggregate everything into the structured format provided.

Analyze the following Reddit thread deeply. Do not just summarize; extract actionable signals.
"""

human_prompt = """
{format_instructions}

Here is the Reddit Post and Comments:
{post_content}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", human_prompt),
])

# Create the chain
chain = prompt | llm | parser

def analyze_post(post_content: str) -> FinalSummary:
    """
    Analyzes a single post content string using the LLM chain.
    """
    try:
        print("  [Ollama] Sending request to local LLM...")
        result = chain.invoke({
            "post_content": post_content,
            "format_instructions": parser.get_format_instructions()
        })
        print("  [Ollama] Response received!")
        return result
    except Exception as e:
        print(f"  [Ollama] Error analyzing post: {e}")
        raise e

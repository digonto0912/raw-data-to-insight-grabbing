import os
from typing import Dict, Any
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

from models import FinalSummary

# Load environment variables
load_dotenv()

# Initialize Groq Chat Model
# We use a large model because we need to process a lot of context (comments) and produce complex structured output.
# llama-3.3-70b-versatile is a good choice for this balance of performance and context window.
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
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
        result = chain.invoke({
            "post_content": post_content,
            "format_instructions": parser.get_format_instructions()
        })
        return result
    except Exception as e:
        print(f"Error analyzing post: {e}")
        raise e

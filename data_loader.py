import json
from typing import List, Dict, Any

def load_posts(file_path: str) -> List[Dict[str, Any]]:
    """
    Loads posts from the given JSON file path.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # The dataset structure seems to be: {"posts": [...], ...}
    if isinstance(data, dict) and "posts" in data:
        return data["posts"]
    elif isinstance(data, list):
        return data
    else:
        raise ValueError("Unexpected JSON structure. Expected a dict with 'posts' key or a list of posts.")

def format_comment_tree(comments: List[Dict[str, Any]], depth: int = 0) -> str:
    """
    Recursively formats a comment tree into a string.
    """
    formatted = ""
    for comment in comments:
        indent = "  " * depth
        author = comment.get("author", "Unknown")
        body = comment.get("body", "").replace("\n", " ")
        score = comment.get("score", 0)
        
        formatted += f"{indent}- [{author}] (Score: {score}): {body}\n"
        
        if "replies" in comment and comment["replies"]:
             # Note: The provided dataset sample didn't explicitly show nested 'replies' in the flat list, 
             # but usually reddit datasets have some structure. 
             # Looking at the sample, it seems 'comments' is a flat list in the post object, 
             # but they have 'parent_id'.
             # For this specific dataset, the 'comments' list inside a post seems to be flat or already nested?
             # Let's check the sample again.
             # Sample shows: "comments": [ { "comment_id": ..., "parent_id": ..., "depth": 0 }, ... ]
             # It seems to be a flat list with depth indicators or parent_ids.
             # For simplicity in this initial version, we will just iterate the flat list 
             # and use the 'depth' field if available for indentation, or just list them.
             pass

    return formatted

def format_flat_comments(comments: List[Dict[str, Any]]) -> str:
    """
    Formats a flat list of comments, using 'depth' for indentation if available.
    """
    formatted = ""
    for comment in comments:
        depth = comment.get("depth", 0)
        indent = "  " * depth
        author = comment.get("author", "Unknown")
        body = comment.get("body", "").replace("\n", " ")
        score = comment.get("score", 0)
        
        formatted += f"{indent}- [{author}] (Score: {score}): {body}\n"
    return formatted

def format_post_for_llm(post: Dict[str, Any]) -> str:
    """
    Formats a single post and its comments into a text block for the LLM.
    """
    title = post.get("title", "No Title")
    body = post.get("body", "")
    subreddit = post.get("subreddit", "Unknown")
    author = post.get("author", "Unknown")
    score = post.get("score", 0)
    created_utc = post.get("created_utc", "")
    
    comments = post.get("comments", [])
    formatted_comments = format_flat_comments(comments)
    
    text = f"""
POST TITLE: {title}
SUBREDDIT: r/{subreddit}
AUTHOR: {author}
DATE: {created_utc}
SCORE: {score}

POST BODY:
{body}

COMMENTS:
{formatted_comments}
"""
    return text.strip()

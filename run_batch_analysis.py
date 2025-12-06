import json
import os
from typing import List, Dict, Any
from agent_ollama import analyze_post
from models import FinalSummary

# Configuration
INPUT_FILE = "test_sample.json"
OUTPUT_DIR = "analysis_results"
NUM_POSTS_TO_ANALYZE = 5

def load_posts(filepath: str) -> List[Dict[str, Any]]:
    """Loads posts from the JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get("posts", [])

def format_post_content(post: Dict[str, Any]) -> str:
    """Formats a post dictionary into a string for the LLM."""
    content = f"Title: {post.get('title', '')}\n"
    content += f"Subreddit: {post.get('subreddit', '')}\n"
    content += f"Author: {post.get('author', '')}\n"
    content += f"Score: {post.get('score', 0)}\n"
    content += f"Url: {post.get('url', '')}\n"
    content += f"Body: {post.get('body', '')}\n\n"
    
    content += "Comments:\n"
    for comment in post.get("comments", []):
        content += f"- [{comment.get('author', 'unknown')}]: {comment.get('body', '')} (Score: {comment.get('score', 0)})\n"
        # Handle nested comments if necessary, but flat list is often easier for LLM if depth is not critical
        # The sample data seems to have a flat list of comments with parent_id, but for simplicity we list them.
        # If structure is important, we might need to reconstruct the tree, but for this task, a list is usually sufficient.
    
    return content

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Load posts
    print(f"Loading posts from {INPUT_FILE}...")
    all_posts = load_posts(INPUT_FILE)
    
    if not all_posts:
        print("No posts found in input file.")
        return

    # Select first N posts
    posts_to_process = all_posts[:NUM_POSTS_TO_ANALYZE]
    print(f"Found {len(all_posts)} posts. Processing the first {len(posts_to_process)}...")

    for i, post in enumerate(posts_to_process):
        post_id = post.get("post_id", "unknown")
        print(f"\n--- Processing Post {i+1}/{len(posts_to_process)} (ID: {post_id}) ---")
        
        # Format content
        post_content = format_post_content(post)
        
        try:
            # Analyze
            result: FinalSummary = analyze_post(post_content)
            
            # Save result
            output_filename = f"post_{i}_{post_id}.json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result.model_dump_json(indent=4))
            
            print(f"Saved analysis to {output_path}")
            
        except Exception as e:
            print(f"Failed to analyze post {post_id}: {e}")

    print("\nBatch analysis complete.")

if __name__ == "__main__":
    main()

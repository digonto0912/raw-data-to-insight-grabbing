import json
import os
import sys
from data_loader import load_posts, format_post_for_llm
from models import PostMetadata

# Configuration: Choose your LLM provider
USE_OLLAMA = True  # Set to True for local Ollama, False for Groq cloud API

if USE_OLLAMA:
    from agent_ollama import analyze_post
    print("🖥️  Using Ollama (Local, Free, CPU-only)")
else:
    from agent import analyze_post
    print("☁️  Using Groq (Cloud API, Rate Limited)")

# File paths
DATA_FILE = "test_sample.json"  # or "singularity_complete_20251203_195509.json"
OUTPUT_DIR = "analysis_results"

def main():
    print(f"Loading data from {DATA_FILE}...")
    try:
        posts = load_posts(DATA_FILE)
    except FileNotFoundError:
        print(f"Error: File {DATA_FILE} not found.")
        return

    if not posts:
        print("No posts found in the dataset.")
        return

    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Found {len(posts)} posts to analyze.")
    print("=" * 60)

    # Analyze each post individually
    for idx, post in enumerate(posts, 1):
        post_id = post.get("post_id", f"unknown_{idx}")
        title = post.get("title", "No Title")
        num_comments = post.get("num_comments", 0)
        
        print(f"\n[{idx}/{len(posts)}] Analyzing post: {post_id}")
        print(f"Title: {title[:80]}{'...' if len(title) > 80 else ''}")
        print(f"Comments: {num_comments}")

        # Format for LLM
        post_text = format_post_for_llm(post)
        
        # Run Analysis
        try:
            result = analyze_post(post_text)
            
            # Add post metadata to the result
            from datetime import datetime
            
            # Calculate post age
            created_utc = post.get("created_utc", "")
            post_age_days = 0
            if created_utc:
                try:
                    post_date = datetime.fromisoformat(created_utc.replace('Z', '+00:00'))
                    now = datetime.now(post_date.tzinfo)
                    post_age_days = (now - post_date).days
                except:
                    pass
            
            post_metadata = PostMetadata(
                post_id=post.get("post_id", "unknown"),
                url=post.get("url", "unknown"),
                created_utc=created_utc,
                score=post.get("score", 0),
                num_comments=post.get("num_comments", 0),
                subreddit=post.get("subreddit", "unknown"),
                post_age_days=post_age_days
            )
            
            # Create final result with metadata
            final_result = {
                "post_metadata": post_metadata.model_dump(),
                **result.model_dump()
            }
            
            # Save result with index in filename (post_1.json, post_2.json, etc.)
            # This is safer for Colab to prevent data loss if it crashes
            output_file = os.path.join(OUTPUT_DIR, f"post_{idx}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(final_result, f, indent=2, ensure_ascii=False)
            
            print(f"[SUCCESS] Analysis complete! Saved to {output_file}")
            print(f"Summary: {result.high_level_summary[:100]}...")

        except Exception as e:
            print(f"[FAILED] Analysis failed: {e}")
            # Continue with next post even if one fails
            continue

    print("\n" + "=" * 60)
    print(f"All analyses complete! Results saved in '{OUTPUT_DIR}/' directory.")

if __name__ == "__main__":
    main()

import requests
import markdown

# Your blog post data (replace with your actual content)
blog_posts = [
    {"title": "Post 1", "content": "# Hello World! This is my first blog post."},
    {"title": "Post 2", "content": "# Hello Again! This is my second blog post."},
]

# Convert markdown to HTML
for post in blog_posts:
    post["content"] = markdown.markdown(post["content"])

# Output blog posts as JSON
output = {"posts": blog_posts}

# Save output to file (e.g., posts.json)
import json
with open('posts.json', 'w') as f:
    json.dump(output, f)

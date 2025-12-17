import urllib.request
import feedparser
import json
import os
import re
from datetime import datetime

# Configuration
QUERY = 'all:%22U-Net%22+OR+all:%22UNet%22+OR+all:%22segmentation%22'
MAX_RESULTS = 10
HISTORY_FILE = 'history.json'
POSTS_DIR = 'content/posts'

def fetch_arxiv_papers(query, start=0, max_results=10):
    url = f'http://export.arxiv.org/api/query?search_query={query}&start={start}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending'
    data = urllib.request.urlopen(url).read()
    return feedparser.parse(data)

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def clean_filename(title):
    # Remove special chars, spaces to hyphens
    clean = re.sub(r'[^\w\s-]', '', title).strip().lower()
    return re.sub(r'[-\s]+', '-', clean)

def create_post(entry):
    title = entry.title.replace('\n', ' ')
    date_str = entry.published
    # Format date for Hugo: 2024-05-21T10:00:00+09:00
    # ArXiv format: 2024-05-21T14:46:12Z
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
        hugo_date = dt.strftime('%Y-%m-%dT%H:%M:%S+00:00')
    except:
        hugo_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')

    # Get authors
    authors = [a.name for a in entry.authors]
    author_str = ", ".join(authors)
    if len(authors) > 3:
        author_str = ", ".join(authors[:3]) + " et al."

    # Abstract
    abstract = entry.summary.replace('\n', ' ')

    # Link
    link = entry.link

    # Create filename
    filename = f"{clean_filename(title)}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    # Check if file exists (redundant with history but good safety)
    if os.path.exists(filepath):
        return None

    content = f"""---
title: "{title.replace('"', '\\"')}"
date: {hugo_date}
draft: true
tags: ["U-Net", "Medical Imaging", "ArXiv", "Auto-generated"]
author: "{author_str}"
---

## 📝 Abstract

{abstract}

## 📎 Link

[View on ArXiv]({link})

## ✍️ Review

*(Write your review here)*
"""

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

    return entry.id # Return ArXiv ID

def main():
    history = load_history()
    # We fetch more than 10 to account for duplicates, but we stop after adding 10 new ones

    # Actually, the user requirement is "fetch 10 papers per run".
    # But if we fetch 10 and all are duplicates, we do nothing?
    # Or should we find 10 *new* papers?
    # User said: "10개를 가져오고, 총 10개의 글이 작성되면 돼." (Fetch 10, total 10 posts created)
    # This implies we should keep fetching until we have 10 new posts or we run out of reasonable queries.
    # However, simple logic: Fetch 50, filter duplicates, take first 10 new ones.

    feed = fetch_arxiv_papers(QUERY, max_results=50)

    new_posts_count = 0
    new_history_ids = []

    print(f"Found {len(feed.entries)} papers from ArXiv.")

    for entry in feed.entries:
        if new_posts_count >= MAX_RESULTS:
            break

        paper_id = entry.id
        if paper_id in history:
            continue

        if create_post(entry):
            print(f"Created post: {entry.title}")
            history.append(paper_id)
            new_posts_count += 1

    save_history(history)
    print(f"Successfully created {new_posts_count} new posts.")

if __name__ == '__main__':
    main()

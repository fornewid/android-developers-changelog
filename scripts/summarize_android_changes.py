#!/usr/bin/env python3
"""
Summarize changes in Android Developers documentation using Gemini API.
"""

import os
import sys
import argparse
import time
from google import genai
from pathlib import Path
from datetime import datetime, timedelta, timezone
import json
import logging
from dotenv import load_dotenv
import subprocess
import re

# Load environment variables
load_dotenv(override=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).parent.parent
DOCS_DIR = ROOT_DIR / 'docs'
CHANGELOG_JSON = ROOT_DIR / 'pages' / 'changelog.json'

def setup_gemini():
    """Configure Gemini API."""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        logger.error("GEMINI_API_KEY environment variable not set.")
        sys.exit(1)
    return genai.Client(api_key=api_key)

def get_git_diff(file_path, commit_hash=None):
    """Get the git diff for a file."""
    try:
        if commit_hash:
            result = subprocess.run(
                ['git', 'diff', f'{commit_hash}^', commit_hash, '--', file_path],
                capture_output=True, text=True, check=False
            )
            return result.stdout
        
        # Check staged
        result = subprocess.run(
            ['git', 'diff', '--cached', file_path],
            capture_output=True, text=True, check=False
        )
        if result.stdout.strip():
            return result.stdout
            
        # Check unstaged
        result = subprocess.run(
            ['git', 'diff', file_path],
            capture_output=True, text=True, check=False
        )
        return result.stdout
    except Exception as e:
        logger.error(f"Failed to get diff for {file_path}: {e}")
        return None

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text

def extract_title_from_content(content, filename, url=None):
    """Extract actual document title from markdown frontmatter, H1 or live URL."""
    if content:
        # Check for title in yaml frontmatter
        # e.g., title: Some Title Here
        title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE | re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
            # If the frontmatter title is just the URL, fall back to heading
            if not title.startswith('http'):
                return title
                
        # Check for first H1 heading
        # e.g., # Some Title
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1).strip()
            
    # Try fetching from live URL if provided
    if url:
        try:
            import urllib.request
            import html
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                html_text = response.read().decode('utf-8', errors='ignore')
                title_match = re.search(r'<title>(.*?)</title>', html_text, re.IGNORECASE)
                if title_match:
                    title = html.unescape(title_match.group(1)).strip()
                    title = title.split('|')[0].strip()
                    title = title.split('&')[0].strip()
                    return title if title else filename
        except Exception:
            pass
            
    return filename

def extract_yaml_summary(content):
    """Extract 'summary' from the YAML frontmatter if it exists."""
    if not content:
        return None
    match = re.search(r'^summary:\s*["\']?([^"\'\n]+)["\']?.*$', content, re.MULTILINE | re.IGNORECASE)
    if match:
         return match.group(1).strip()
    return None

def generate_summary(client, filename, content, is_new=False):
    """Generate a summary using Gemini."""
    
    prompt_context = "This is a new file." if is_new else "Here is the git diff of the changes."
    
    task_instructions = """
    1. **FILTER TRIVIAL CHANGES:** 
       - Ignore whitespace, formatting, simple rewording, or HTML-to-Markdown conversion artifacts.
       - If changes are trivial: **RETURN AN EMPTY LIST []**.
    2. If changes are meaningful:
       - **Return ONE summary** consolidating the changes.
       - Use "Overview" as the header.
    """

    if is_new:
        task_instructions = """
    1. **NEW FILE ADDED.**
       - Thoroughly summarize the full content of this new documentation page in detail.
       - Focus on the core concepts, main topics, and the exact purpose of the document.
       - Provide a detailed, highly informative, and comprehensive overview.
       - **Return ONE summary** with header "Overview".
    """

    prompt = f"""
    You are an Android expert and tech editor. Analyze the changes in the "{filename}" documentation.
    {prompt_context}
    
    Task:
    {task_instructions}
    
    3. **Write informative properties.** The summary should explain "what changed" and "why it matters" in English. For a new file, provide a comprehensive and detailed overview.
    4. Return the result in JSON format.
    
    Format example:
    [
        {{
            "header": "Overview", 
            "summary": "Detailed summary text goes here."
        }}
    ]
    
    Content/Diff:
    {content[:15000]}
    """
    
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-lite',
                contents=prompt,
                config={'response_mime_type': 'application/json'}
            )
            return json.loads(response.text)
        except Exception as e:
            time.sleep(2)
            if attempt == 2:
                logger.error(f"Gemini API failed for {filename}: {e}")
                
    return [{"header": "Overview", "summary": f"{filename} documentation has been updated."}]

def load_changelog():
    if not CHANGELOG_JSON.exists():
        return []
    try:
        return json.loads(CHANGELOG_JSON.read_text(encoding='utf-8'))
    except:
        return []

def save_changelog(data):
    CHANGELOG_JSON.parent.mkdir(exist_ok=True)
    CHANGELOG_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

def get_commit_date(commit_hash):
    """Get the commit date in ISO 8601 format."""
    try:
        iso_date = subprocess.check_output(
            ['git', 'show', '-s', '--format=%cI', commit_hash],
            text=True
        ).strip()
        return iso_date
    except Exception as e:
        logger.warning(f"Failed to get commit date for {commit_hash}: {e}")
        return datetime.now(timezone.utc).isoformat()

def update_json_data(updates, commit_hash=None):
    if not updates:
        return load_changelog()

    history = load_changelog()
    
    if commit_hash:
        date_str = get_commit_date(commit_hash)
    else:
        date_str = datetime.now(timezone.utc).isoformat()
    
    new_entry = {
        "date": date_str,
        "commit_hash": commit_hash,
        "entries": updates
    }
    
    history.insert(0, new_entry)
    save_changelog(history)
    return history

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--commit-hash', default=None)
    args = parser.parse_args()
    
    if not args.files:
        return

    client = setup_gemini()
    updates = []
    base_url = "https://developer.android.com" 
    # Logic to reconstruct URL from filename might be needed if we want direct links.
    # Filename: path__to__page.md -> https://developer.android.com/path/to/page
    
    for file_arg in args.files:
        time.sleep(1)
        
        if ':' in file_arg:
            status, file_path = file_arg.split(':', 1)
        else:
            status, file_path = 'M', file_arg
            
        filename = os.path.basename(file_path)
        if not filename.endswith('.md'):
            continue
            
        logger.info(f"Processing {filename} (Status: {status})...")
        
        tag_text = "UPDATE"
        tag_class = "update"
        if status == 'A':
            tag_text = "NEW"
            tag_class = "new"
        elif status == 'D':
            tag_text = "DELETE"
            tag_class = "delete"
            
        # Reconstruct URL first so we can use it for title extraction if needed
        rel_path = file_path
        if 'docs/' in rel_path:
             rel_path = rel_path.split('docs/', 1)[1]
             
        url_path = rel_path.replace('.md', '')
        url = f"{base_url}/{url_path}"
            
        if status == 'D':
            updates.append({
                'title': filename,
                'summary': "Documentation has been removed.",
                'tag_text': tag_text,
                'tag_class': tag_class
            })
            continue

        doc_title = filename
        full_content = ""
        try:
            full_content = Path(file_path).read_text(encoding='utf-8')
            doc_title = extract_title_from_content(full_content, filename, url)
        except Exception as e:
            logger.warning(f"Failed to read full content for title extraction of {file_path}: {e}")
            
        content = get_git_diff(file_path, args.commit_hash)
        if status == 'A' and not content:
            content = full_content
                
        if not content and not full_content:
            continue

        if status == 'M':
            yaml_summary = extract_yaml_summary(full_content)
            if not yaml_summary:
                logger.info(f"Skipping {filename} (UPDATE) because no YAML summary found.")
                continue
            summaries = [{'header': 'Overview', 'summary': yaml_summary}]
        elif status == 'A':
            if not content:
                continue
            summaries = generate_summary(client, filename, content, True)
        else:
            summaries = []
        
        for item in summaries:
            summary_text = item.get('summary', '')
            
            entry = {
                'title': f'<a href="{url}" target="_blank">{doc_title}</a>',
                'path': rel_path,
                'summary': summary_text,
                'tag_text': tag_text,
                'tag_class': tag_class
            }
            
            if tag_class == 'update' and content:
                diffs_dir = ROOT_DIR / 'pages' / 'diffs'
                diffs_dir.mkdir(parents=True, exist_ok=True)
                safe_hash = args.commit_hash if args.commit_hash else 'local'
                diff_filename = f"{safe_hash}_{filename}.txt"
                diff_path = diffs_dir / diff_filename
                diff_path.write_text(content, encoding='utf-8')
                entry['diff_file'] = f"pages/diffs/{diff_filename}"
                
            updates.append(entry)
            
    if updates:
        update_json_data(updates, args.commit_hash)
        
        # Generate Release Body for GitHub
        release_body_path = ROOT_DIR / 'release_body.md'
        release_content = "## Android Docs Updates\n\n"
        for update in updates:
            path_str = f"`{update['path']}`\n" if 'path' in update else ""
            release_content += f"### {update['tag_text']} {update['title']}\n{path_str}{update['summary']}\n\n"
        release_body_path.write_text(release_content, encoding='utf-8')

if __name__ == '__main__':
    main()

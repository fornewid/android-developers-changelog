#!/usr/bin/env python3
"""
Backfill script to update older entries in pages/changelog.json
so they use the actual page title instead of the raw .md filename.
"""

import json
import re
import urllib.request
import html
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).parent.parent
CHANGELOG_JSON = ROOT_DIR / 'pages' / 'changelog.json'
RELEASE_BODY = ROOT_DIR / 'release_body.md'

def fetch_title_from_url(url):
    """Fetch the live page HTML and return its <title> contents."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            html_text = response.read().decode('utf-8', errors='ignore')
            title_match = re.search(r'<title>(.*?)</title>', html_text, re.IGNORECASE)
            if title_match:
                title = html.unescape(title_match.group(1)).strip()
                title = title.split('|')[0].strip()
                title = title.split('&')[0].strip()
                return title
    except Exception as e:
        logger.warning(f"Failed to fetch {url}: {e}")
    return None

def main():
    if not CHANGELOG_JSON.exists():
        logger.error(f"Cannot find {CHANGELOG_JSON}")
        return

    try:
        data = json.loads(CHANGELOG_JSON.read_text(encoding='utf-8'))
    except Exception as e:
        logger.error(f"Failed to load JSON: {e}")
        return

    updated_count = 0

    for history_entry in data:
        for entry in history_entry.get('entries', []):
            original_title_html = entry.get('title', '')
            
            # Look for <a> tag containing .md
            # e.g. <a href="https://developer.android.com/something" target="_blank">something.md</a>
            match = re.search(r'<a href="([^"]+)"[^>]*>([^<]+)</a>', original_title_html)
            if match:
                url = match.group(1)
                display_text = match.group(2)
                
                # Add path field if it's missing
                if 'path' not in entry:
                    if url.startswith('https://developer.android.com/'):
                        url_path = url[len('https://developer.android.com/'):]
                        if not url_path.endswith('.md'):
                            entry['path'] = f"{url_path}.md"
                        else:
                            entry['path'] = url_path
                        updated_count += 1
                        logger.info(f"  -> Added path: {entry['path']}")
                
                # If display text still has .md, we need to try updating it
                if display_text.endswith('.md'):
                    logger.info(f"Targeting legacy entry: {display_text}")
                    new_title = fetch_title_from_url(url)
                    
                    if new_title:
                        # Replace the inner text with the new title
                        new_html = original_title_html.replace(f">{display_text}<", f">{new_title}<")
                        if new_html != original_title_html:
                            entry['title'] = new_html
                            updated_count += 1
                            logger.info(f"  -> Updated to: {new_title}")
                    else:
                        logger.warning(f"  -> Could not extract title for {url}")

    if updated_count > 0:
        logger.info(f"Updated {updated_count} entries. Saving...")
        CHANGELOG_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
        
        # Optionally regenerate release_body.md for the most recent changes (first entry in list)
        if data and data[0].get('entries'):
             release_content = "## Android Docs Updates\n\n"
             for update in data[0]['entries']:
                 path_str = f"`{update['path']}`\n" if 'path' in update else ""
                 release_content += f"### {update.get('tag_text', '')} {update.get('title', '')}\n{path_str}{update.get('summary', '')}\n\n"
             RELEASE_BODY.write_text(release_content, encoding='utf-8')
             logger.info("Updated release_body.md")
    else:
        logger.info("No legacy .md files found to update.")

if __name__ == '__main__':
    main()

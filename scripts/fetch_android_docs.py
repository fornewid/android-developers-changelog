#!/usr/bin/env python3
"""
Android Developers documentation fetcher.
Tracks changes in https://developer.android.com/sitemap.xml
"""

import requests
import time
from pathlib import Path
from typing import List, Tuple, Set, Optional
import logging
from datetime import datetime
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
import json
import hashlib
import os
import re
import random
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import concurrent.futures
import threading

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

SITEMAP_INDEX_URL = "https://developer.android.com/sitemap.xml"
MANIFEST_FILE = "docs_manifest.json"
MAX_RETRIES = 3
RETRY_DELAY = 2
MAX_WORKERS = 5 # Parallel threads for content fetching

HEADERS = {
    'User-Agent': 'Android-Docs-Tracker/1.0',
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0'
}

def load_manifest(docs_dir: Path) -> dict:
    """Load the manifest of previously fetched files."""
    manifest_path = docs_dir / MANIFEST_FILE
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text())
            if "files" not in manifest:
                manifest["files"] = {}
            return manifest
        except Exception as e:
            logger.warning(f"Failed to load manifest: {e}")
    return {"files": {}, "last_updated": None}

def save_manifest(docs_dir: Path, manifest: dict) -> None:
    """Save the manifest of fetched files."""
    manifest_path = docs_dir / MANIFEST_FILE
    manifest["last_updated"] = datetime.now().isoformat()
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2))

def url_to_file_path(url: str) -> Path:
    """Convert a URL to a nested file path."""
    parsed = urlparse(url)
    path = parsed.path
    
    # Remove leading slash
    if path.startswith('/'):
        path = path[1:]
    
    # Handle root or empty path
    if not path:
        return Path("index.md")
        
    # Append .md extension
    if not path.endswith('.md'):
        path += '.md'
        
    return Path(path)

def fetch_sitemap_urls(session: requests.Session, sitemap_url: str) -> List[str]:
    """Fetch URLs from a sitemap (handling index or urlset)."""
    urls = []
    
    for attempt in range(MAX_RETRIES):
        try:
            logger.info(f"Fetching sitemap (Attempt {attempt+1}/{MAX_RETRIES}): {sitemap_url}")
            response = session.get(sitemap_url, headers=HEADERS, timeout=60)
            response.raise_for_status()
            
            # Parse XML safely
            try:
                parser = ET.XMLParser(forbid_dtd=True, forbid_entities=True, forbid_external=True)
                root = ET.fromstring(response.content, parser=parser)
            except TypeError:
                 root = ET.fromstring(response.content)
                
            namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            
            # Check if sitemapindex
            if root.tag.endswith('sitemapindex'):
                for sitemap in root.findall('ns:sitemap', namespace):
                    loc = sitemap.find('ns:loc', namespace)
                    if loc is not None and loc.text:
                        # Recursively fetch child sitemaps
                        urls.extend(fetch_sitemap_urls(session, loc.text))
            else:
                # Assume urlset
                for url in root.findall('ns:url', namespace):
                    loc = url.find('ns:loc', namespace)
                    if loc is not None and loc.text:
                        urls.append(loc.text)
            
            return urls # Success, return collected URLs
            
        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt + 1}/{MAX_RETRIES} failed for sitemap {sitemap_url}: {e}")
            if attempt < MAX_RETRIES - 1:
                delay = RETRY_DELAY * (2 ** attempt)
                logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logger.error(f"Failed to process sitemap {sitemap_url} after {MAX_RETRIES} attempts.")
        except Exception as e:
             logger.error(f"Unexpected error processing sitemap {sitemap_url}: {e}")
             break
        
    return urls

def get_child_sitemaps(session: requests.Session, sitemap_index_url: str) -> List[str]:
    """Get list of child sitemaps from the index sitemap."""
    sitemaps = []
    try:
        logger.info(f"Fetching sitemap index: {sitemap_index_url}")
        response = session.get(sitemap_index_url, headers=HEADERS, timeout=60)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        if root.tag.endswith('sitemapindex'):
            for sitemap in root.findall('ns:sitemap', namespace):
                loc = sitemap.find('ns:loc', namespace)
                if loc is not None and loc.text:
                    sitemaps.append(loc.text)
                    
            # Sort sitemaps numerically
            def sort_key(url):
                match = re.search(r'sitemap_(\d+)_of_', url)
                if match:
                    return int(match.group(1))
                return url
            
            sitemaps.sort(key=sort_key)
            
        else:
            # It's not an index, just return itself as a single sitemap to process
            sitemaps.append(sitemap_index_url)
            
    except Exception as e:
        logger.error(f"Failed to fetch sitemap index: {e}")
        
    return sitemaps

def fetch_content(session: requests.Session, url: str) -> Tuple[str, str, str]:
    """
    Fetch content for a URL.
    Returns: (file_path, content, fetch_method)
    fetch_method is 'md.txt' or 'html-scrape'
    """
    file_path = url_to_file_path(url)
    
    # 1. Try fetching .md.txt
    md_url = f"{url}.md.txt"
    try:
        response = session.get(md_url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            content = response.text
            header = f"---\ntitle: {url}\nurl: {url}\nsource: md.txt\n---\n\n"
            return str(file_path), header + content, 'md.txt'
    except Exception:
        pass

    # 2. Fallback to HTML scraping
    try:
        response = session.get(url, headers=HEADERS, timeout=30)
        if response.status_code == 429:
            wait_time = int(response.headers.get('Retry-After', 60))
            time.sleep(wait_time)
            response = session.get(url, headers=HEADERS, timeout=30)
            
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        content_elem = soup.find('article', class_='devsite-article')
        if not content_elem:
            content_elem = soup.find('main')
        if not content_elem:
            content_elem = soup.find('div', role='main')
        
        if not content_elem:
            logger.warning(f"Could not find main content for {url}")
            return str(file_path), "", 'failed'
        
        markdown_content = md(str(content_elem), heading_style="ATX")
        title = soup.title.string if soup.title else 'Untitled'
        header = f"---\ntitle: {title}\nurl: {url}\nsource: html-scrape\n---\n\n"
        
        return str(file_path), header + markdown_content, 'html-scrape'
            
    except Exception as e:
        logger.error(f"Failed to fetch/convert HTML for {url}: {e}")
        return str(file_path), "", 'failed'

def save_markdown_file(docs_dir: Path, rel_path: str, content: str) -> str:
    """Save markdown content and return its hash."""
    file_path = docs_dir / rel_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        file_path.write_text(content, encoding='utf-8')
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    except Exception as e:
        logger.error(f"Failed to save {rel_path}: {e}")
        raise

def cleanup_old_files(docs_dir: Path, current_files: set, manifest: dict) -> None:
    """Remove files that were previously fetched but no longer exist in the sitemap."""
    previous_files = set(manifest.get("files", {}).keys())
    files_to_remove = previous_files - current_files
    
    for filename in files_to_remove:
        if filename == MANIFEST_FILE:
            continue
        file_path = docs_dir / filename
        if file_path.exists():
            logger.info(f"Removing obsolete file: {filename}")
            file_path.unlink()

def process_sitemap_urls(session: requests.Session, urls: List[str], docs_dir: Path, manifest: dict, lock: threading.Lock) -> Tuple[int, int]:
    """Process a list of URLs from a sitemap: filter and download content."""
    
    # Filter URLs
    filtered_urls = []
    skip_patterns = ['/ko/', '/ja/', '/zh-cn/', '/es/', '/pt-br/', '/ru/', '/id/', '/vi/', '/de/', '/fr/', '/it/']
    for url in urls:
        # Skip reference and sdk docs
        if '/reference/' in url or '/sdk/' in url:
            continue
            
        # Skip other reference-like paths and archives
        if '/api_diff/' in url:
            continue
        if '/games/sdk/' in url:
            continue
        if '/games/services/cpp/api/' in url:
            continue
        if '/games/services/web/api/' in url:
            continue
        if 'newsletter' in url:
            continue

        # Skip binary files
        if url.endswith('.pdf') or url.endswith('.zip'):
            continue

        if '?hl=' in url or '&hl=' in url:
            continue
        parsed = urlparse(url)
        if 'hl=' in parsed.query:
            continue
        path = parsed.path
        if not any(lang in path for lang in skip_patterns):
            filtered_urls.append(url)            
    logger.info(f"Found {len(urls)} URLs, {len(filtered_urls)} to process after filtering (excluded /reference/ and /sdk/).")
    
    if not filtered_urls:
        return 0, 0, []

    successful = 0
    failed = 0
    failed_urls = []
    
    # Process each URL
    def process_url(url):
        nonlocal successful, failed
        try:
            rel_path, content, method = fetch_content(session, url)
            
            if not content:
                with lock:
                    failed += 1
                    failed_urls.append(url)
                return
            
            # Use lock to access manifest safely
            with lock:
                old_hash = manifest.get("files", {}).get(rel_path, {}).get("hash", "")
            
            new_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
            
            content_hash = ""
            if new_hash != old_hash:
                content_hash = save_markdown_file(docs_dir, rel_path, content)
                with lock:
                    logger.info(f"Updated ({method}): {rel_path}")
                last_updated = datetime.now().isoformat()
            else:
                content_hash = old_hash
                with lock:
                    last_updated = manifest.get("files", {}).get(rel_path, {}).get("last_updated", datetime.now().isoformat())
            
            with lock:
                manifest["files"][rel_path] = {
                    "original_url": url,
                    "hash": content_hash,
                    "last_updated": last_updated,
                    "fetch_method": method
                }
                successful += 1
                if successful % 100 == 0:
                     logger.info(f"Progress: {successful}/{len(filtered_urls)}")

        except Exception as e:
            with lock:
                logger.error(f"Failed to process {url}: {e}")
                failed += 1
                failed_urls.append(url)

    # Parallel Execution for this batch of URLs
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit all tasks
        futures = [executor.submit(process_url, url) for url in filtered_urls]
        # Wait for all to complete
        concurrent.futures.wait(futures)
        
    return successful, failed, failed_urls

def main():
    logger.info("Starting Android Developers documentation fetch (Sitemap-by-Sitemap)")
    
    docs_dir = Path(__file__).parent.parent / 'docs'
    docs_dir.mkdir(exist_ok=True)
    
    old_manifest = load_manifest(docs_dir)
    manifest = load_manifest(docs_dir)
    lock = threading.Lock()
    
    total_successful = 0
    total_failed = 0
    all_failed_urls = []
    fetched_files = set()
    
    with requests.Session() as session:
        # 1. Get list of all child sitemaps
        child_sitemaps = get_child_sitemaps(session, SITEMAP_INDEX_URL)
        logger.info(f"Found {len(child_sitemaps)} child sitemaps to process.")
        
        # 2. Process each sitemap sequentially
        for i, sitemap_url in enumerate(child_sitemaps):
            logger.info(f"Processing sitemap {i+1}/{len(child_sitemaps)}: {sitemap_url}")
            
            # Fetch URLs for this sitemap
            urls = fetch_sitemap_urls(session, sitemap_url)
            
            # Process URLs
            success, fail, failed_urls = process_sitemap_urls(session, urls, docs_dir, manifest, lock)
            
            total_successful += success
            total_failed += fail
            all_failed_urls.extend(failed_urls)
            
            # Track fetched files
            with lock:
                fetched_files.update(manifest.get("files", {}).keys())
            
            # Save manifest after each sitemap to checkpoint progress
            save_manifest(docs_dir, manifest)
            logger.info(f"Checkpoint saved. Total Success: {total_successful}, Total Failed: {total_failed}")
    
    # Clean up files that no longer exist in the sitemap
    cleanup_old_files(docs_dir, fetched_files, old_manifest)
            
    logger.info("="*50)
    logger.info(f"All completed. Total Successful: {total_successful}, Total Failed: {total_failed}")
    
    if all_failed_urls:
        logger.info("\nList of Failed URLs:")
        for url in all_failed_urls:
            logger.info(f"- {url}")

if __name__ == "__main__":
    main()

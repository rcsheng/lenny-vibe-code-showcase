#!/usr/bin/env python3
"""
Parse creator information and platform details from the HTML
"""
import re
import json
from pathlib import Path
from html.parser import HTMLParser

class CreatorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_span = False
        self.current_text = ""
        self.entries = []
        self.pending_creator = None
        self.next_link_is_creator = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == 'span':
            self.in_span = True
            self.current_text = ""

        if tag == 'a' and self.next_link_is_creator:
            href = attrs_dict.get('href', '')
            # This is the creator link
            if self.pending_creator:
                self.pending_creator['creator_url'] = href

    def handle_endtag(self, tag):
        if tag == 'span':
            self.in_span = False
            # Check if this span contains "by "
            if ', by ' in self.current_text or 'by ' in self.current_text:
                # Extract the title part
                parts = self.current_text.split(', by ')
                if len(parts) == 2:
                    title = parts[0].strip()
                    creator_part = parts[1].strip()
                    self.pending_creator = {
                        'title': title,
                        'creator': creator_part if creator_part else None,
                        'creator_url': None
                    }
                    self.next_link_is_creator = True
                else:
                    parts = self.current_text.split(' by ')
                    if len(parts) == 2:
                        title = parts[0].strip()
                        creator_part = parts[1].strip()
                        self.pending_creator = {
                            'title': title,
                            'creator': creator_part if creator_part else None,
                            'creator_url': None
                        }
                        self.next_link_is_creator = True

        if tag == 'a' and self.pending_creator:
            # Check if we got the creator name from the link
            if self.pending_creator['creator'] is None and self.current_text.strip():
                self.pending_creator['creator'] = self.current_text.strip()

            # Save and reset
            if self.pending_creator['creator']:
                self.entries.append(self.pending_creator)
            self.pending_creator = None
            self.next_link_is_creator = False

    def handle_data(self, data):
        if self.in_span:
            self.current_text += data
        elif self.next_link_is_creator:
            # This is the creator name in the link
            if self.pending_creator and not self.pending_creator['creator']:
                self.pending_creator['creator'] = data.strip()

def extract_with_regex(html_content):
    """Use regex to find patterns"""
    entries = []

    # Pattern 1: <span>Title, by </span><a href="url">Creator Name</a>
    pattern1 = r'<span>([^<]+?), by </span><a href="([^"]+)"[^>]*>([^<]+)</a>'
    matches1 = re.findall(pattern1, html_content)
    for title, url, creator in matches1:
        entries.append({
            'title': title.strip(),
            'creator': creator.strip(),
            'creator_url': url.strip()
        })

    # Pattern 2: <span>Title by </span><a href="url">Creator Name</a>
    pattern2 = r'<span>([^<]+?) by </span><a href="([^"]+)"[^>]*>([^<]+)</a>'
    matches2 = re.findall(pattern2, html_content)
    for title, url, creator in matches2:
        entries.append({
            'title': title.strip(),
            'creator': creator.strip(),
            'creator_url': url.strip()
        })

    return entries

def extract_platform(text, url):
    """Detect which platform was used based on URL or context"""
    url_lower = url.lower()

    if 'replit.app' in url_lower or 'repl.it' in url_lower:
        return 'replit'
    elif 'lovable.app' in url_lower or 'lovable.dev' in url_lower:
        return 'lovable'
    elif 'vercel.app' in url_lower:
        return 'vercel'
    elif 'netlify.app' in url_lower:
        return 'netlify'
    elif 'pages.dev' in url_lower:
        return 'cloudflare'
    elif 'claude.ai' in url_lower:
        return 'claude'
    else:
        return 'custom'

if __name__ == '__main__':
    html_file = Path('original_site/What people are vibe coding (and actually using).html')

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = extract_with_regex(content)

    print(f"Found {len(entries)} projects with creator information:\n")

    # Load existing sites.json to match with URLs
    sites_file = Path('public/sites.json')
    with open(sites_file, 'r', encoding='utf-8') as f:
        sites = json.load(f)

    # Create a mapping of title to entry
    creator_map = {}
    for entry in entries:
        creator_map[entry['title'].lower()] = entry

    # Update sites with creator info
    updated_count = 0
    for site in sites:
        title_lower = site['title'].lower()

        # Try to find matching creator info
        for creator_title, creator_info in creator_map.items():
            if creator_title in title_lower or title_lower in creator_title:
                site['creator'] = creator_info['creator']
                site['creator_url'] = creator_info['creator_url']

                # Detect platform
                platform = extract_platform(creator_info['title'], site['url'])
                site['platform'] = platform
                site['image'] = f'/images/{platform}-logo.svg'

                updated_count += 1
                print(f"✓ {site['title']}")
                print(f"  Creator: {creator_info['creator']}")
                print(f"  Platform: {platform}")
                print()
                break

    # Save updated sites
    with open(sites_file, 'w', encoding='utf-8') as f:
        json.dump(sites, f, indent=2, ensure_ascii=False)

    print(f"\nUpdated {updated_count} sites with creator information")
    print(f"Saved to {sites_file}")

#!/usr/bin/env python3
"""
Update sites.json with creator information from the HTML
"""
import re
import json
from pathlib import Path

def extract_creators_and_links(html_content):
    """Extract creator info and project links from HTML"""
    # Pattern: <span>Description, by </span><a href="creator_url">Creator</a>
    # Then look for the "Check it out" link nearby

    entries = []

    # Find all creator patterns
    pattern = r'<span>([^<]+?), by </span><a href="([^"]+)"[^>]*>([^<]+)</a>'
    creator_matches = re.findall(pattern, html_content)

    # For each creator match, find the associated project URL
    for description, creator_url, creator_name in creator_matches:
        # Find the context around this creator mention
        # Look for href links in the nearby text
        creator_pattern = re.escape(creator_name)
        context_pattern = f'{creator_pattern}.*?href="(https?://[^"]+)"'

        context_match = re.search(context_pattern, html_content, re.DOTALL)
        if context_match:
            project_url = context_match.group(1)
            # Filter out social media URLs
            if not any(domain in project_url.lower() for domain in ['linkedin.com', 'twitter.com', 'x.com', 'facebook.com']):
                entries.append({
                    'description': description.strip(),
                    'creator': creator_name.strip(),
                    'creator_url': creator_url.strip(),
                    'project_url': project_url.strip()
                })

    return entries

def match_urls(url1, url2):
    """Check if two URLs likely point to the same site"""
    # Normalize URLs
    u1 = url1.lower().replace('http://', '').replace('https://', '').replace('www.', '')
    u2 = url2.lower().replace('http://', '').replace('https://', '').replace('www.', '')

    # Remove trailing slashes
    u1 = u1.rstrip('/')
    u2 = u2.rstrip('/')

    # Check if they match or one is a substring of the other
    return u1 == u2 or u1 in u2 or u2 in u1

def extract_platform(url):
    """Detect which platform was used based on URL"""
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
        return 'web'

if __name__ == '__main__':
    html_file = Path('original_site/What people are vibe coding (and actually using).html')

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract all project URLs and their Check it out links
    # Pattern: project description followed by "Check it out" link
    project_pattern = r'<span>([^<]+?), by </span><a href="([^"]+)"[^>]*>([^<]+)</a>.*?<a[^>]*href="(https?://[^"]+)"[^>]*>(?:Check it out|Enjoy|track)'

    matches = re.findall(project_pattern, content, re.DOTALL)

    creators_data = []
    for desc, creator_url, creator_name, project_url in matches:
        # Skip if project URL is a social media link
        if any(domain in project_url.lower() for domain in ['linkedin.com', 'twitter.com', 'x.com', 'facebook.com', 'instagram.com']):
            continue

        creators_data.append({
            'description': desc.strip(),
            'creator': creator_name.strip(),
            'creator_url': creator_url.strip(),
            'project_url': project_url.strip()
        })

    print(f"Found {len(creators_data)} projects with creator info:\n")

    # Load existing sites.json
    sites_file = Path('public/sites.json')
    with open(sites_file, 'r', encoding='utf-8') as f:
        sites = json.load(f)

    # Update sites with creator info by matching URLs
    updated_count = 0
    for site in sites:
        for creator_data in creators_data:
            if match_urls(site['url'], creator_data['project_url']):
                site['creator'] = creator_data['creator']
                site['creator_url'] = creator_data['creator_url']
                site['description'] = creator_data['description']

                # Detect platform and set logo
                platform = extract_platform(site['url'])
                site['image'] = f'/images/{platform}-logo.svg'

                updated_count += 1
                print(f"✓ {site['title']}")
                print(f"  Creator: {creator_data['creator']}")
                print(f"  URL: {site['url'][:60]}...")
                print(f"  Platform: {platform}")
                print()
                break

    # Save updated sites
    with open(sites_file, 'w', encoding='utf-8') as f:
        json.dump(sites, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Updated {updated_count}/{len(sites)} sites with creator information")
    print(f"Saved to {sites_file}")

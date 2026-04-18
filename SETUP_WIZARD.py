#!/usr/bin/env python3
"""
💀 GHOST MARKETER — SETUP WIZARD
Interactive configuration for autonomous marketing
"""

import os
import json
from datetime import datetime, timedelta

CONFIG_FILE = "/home/alex/Desktop/DK/ghost_marketer/config.json"

def save_config(config: dict):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)
    print(f"✅ Configuration saved to {CONFIG_FILE}")

def load_config() -> dict:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def setup_wordpress():
    """Setup WordPress connection"""
    print("\n" + "=" * 50)
    print("🌐 WORDPRESS SETUP")
    print("=" * 50)
    
    config = load_config()
    
    print("\n📝 Enter your WordPress site URL:")
    print("   (e.g., https://mysite.com)")
    wp_url = input("   > ").strip()
    
    print("\n🔑 Enter your WordPress REST API Application Password:")
    print("   (Generate at: WordPress Admin > Users > Application Passwords)")
    print("   Format: username|xxxxxxxxxxxx")
    wp_token = input("   > ").strip()
    
    print("\n📧 Enter admin email for notifications:")
    admin_email = input("   > ").strip()
    
    config['wordpress'] = {
        'url': wp_url,
        'token': wp_token,
        'admin_email': admin_email
    }
    
    # Test connection
    print("\n🔍 Testing WordPress connection...")
    try:
        import requests
        headers = {"Authorization": f"Bearer {wp_token}"}
        response = requests.get(f"{wp_url}/wp-json/wp/v2/posts", headers=headers, timeout=10)
        if response.status_code == 200:
            print("   ✅ WordPress connection successful!")
            draft_count = len(response.json())
            print(f"   📝 Found {draft_count} posts")
        else:
            print(f"   ⚠️  Connection returned status: {response.status_code}")
    except Exception as e:
        print(f"   ⚠️  Connection failed: {e}")
    
    save_config(config)
    return config

def setup_twitter():
    """Setup Twitter/X API"""
    print("\n" + "=" * 50)
    print("🐦 TWITTER/X SETUP")
    print("=" * 50)
    
    config = load_config()
    
    print("\n⚠️  Twitter API v2 requires Developer Account access")
    print("    Apply at: https://developer.twitter.com/en/apply-for-access")
    print("\n📋 Required credentials:")
    print("   1. API Key (Consumer Key)")
    print("   2. API Secret (Consumer Secret)")
    print("   3. Access Token")
    print("   4. Access Token Secret")
    
    print("\n🔑 API Key:")
    api_key = input("   > ").strip()
    
    print("🔑 API Secret:")
    api_secret = input("   > ").strip()
    
    print("🔑 Access Token:")
    access_token = input("   > ").strip()
    
    print("🔑 Access Token Secret:")
    access_secret = input("   > ").strip()
    
    config['twitter'] = {
        'api_key': api_key,
        'api_secret': api_secret,
        'access_token': access_token,
        'access_secret': access_secret
    }
    
    save_config(config)
    print("\n✅ Twitter credentials saved!")
    
    return config

def setup_seo_preferences():
    """Setup SEO preferences"""
    print("\n" + "=" * 50)
    print("🔍 SEO PREFERENCES (2026 Edition)")
    print("=" * 50)
    
    config = load_config()
    
    print("\n🎯 Primary content niches (comma-separated):")
    print("   e.g., AI, Marketing, Technology, Business")
    niches = input("   > ").strip()
    
    print("\n📊 Target audience:")
    print("   1. B2B Professionals")
    print("   2. B2C Consumers")
    print("   3. Tech Startups")
    print("   4. Enterprise")
    audience = input("   > ").strip()
    
    print("\n🌍 Target regions:")
    print("   e.g., Global, US, EU, Asia")
    regions = input("   > ").strip()
    
    print("\n⏰ Schedule time (24h format):")
    print("   (Posts will be scheduled for this time daily)")
    schedule_time = input("   > ").strip() or "09:00"
    
    config['seo'] = {
        'niches': [n.strip() for n in niches.split(',') if n.strip()],
        'audience': audience,
        'regions': regions,
        'schedule_time': schedule_time
    }
    
    save_config(config)
    return config

def setup_image_generation():
    """Setup AI image generation preferences"""
    print("\n" + "=" * 50)
    print("🖼️ IMAGE GENERATION SETUP")
    print("=" * 50)
    
    config = load_config()
    
    print("\n🎨 Preferred image styles:")
    print("   1. Modern Corporate (default)")
    print("   2. Minimalist")
    print("   3. Abstract/Artistic")
    print("   4. Photorealistic")
    style = input("   > ").strip() or "1"
    
    styles = {
        '1': 'modern corporate, professional business',
        '2': 'minimalist clean design',
        '3': 'abstract artistic creative',
        '4': 'photorealistic high detail'
    }
    
    print("\n📏 Image aspect ratio:")
    print("   1. Square (1024x1024) - for Twitter/Instagram")
    print("   2. Landscape (1024x512) - for blog headers")
    print("   3. Portrait (768x1024) - for stories")
    ratio = input("   > ").strip() or "1"
    
    ratios = {
        '1': (1024, 1024),
        '2': (1024, 512),
        '3': (768, 1024)
    }
    
    config['images'] = {
        'style': styles.get(style, styles['1']),
        'aspect_ratio': ratios.get(ratio, ratios['1'])
    }
    
    save_config(config)
    return config

def setup_scheduling():
    """Setup posting schedule"""
    print("\n" + "=" * 50)
    print("📅 SCHEDULING SETUP")
    print("=" * 50)
    
    config = load_config()
    
    print("\n🕐 Default posting time:")
    hour = input("   Hour (0-23) [9]: ").strip() or "9"
    minute = input("   Minute (0-59) [0]: ").strip() or "0"
    
    print("\n📆 Days to post:")
    print("   e.g., mon,wed,fri or all")
    days = input("   > [all]: ").strip() or "all"
    
    print("\n🔢 Posts per day:")
    posts = input("   > [1]: ").strip() or "1"
    
    config['schedule'] = {
        'hour': int(hour),
        'minute': int(minute),
        'days': days,
        'posts_per_day': int(posts)
    }
    
    save_config(config)
    return config

def run_now():
    """Run Ghost Marketer immediately"""
    print("\n" + "=" * 50)
    print("🚀 RUNNING GHOST MARKETER NOW")
    print("=" * 50)
    
    config = load_config()
    
    if 'wordpress' not in config:
        print("❌ WordPress not configured!")
        print("   Please run setup first.")
        return
    
    # Import and run
    import asyncio
    from GHOST_MARKETER import GhostMarketer
    
    gm = GhostMarketer()
    
    asyncio.run(gm.initialize(
        config['wordpress']['url'],
        config['wordpress']['token']
    ))
    
    asyncio.run(gm.run_full_pipeline())

def main():
    print("\n" + "=" * 60)
    print("💀 DARKGEMINI v51.0 — GHOST MARKETER SETUP WIZARD")
    print("=" * 60)
    
    while True:
        print("\n╔═══════════════════════════════════════════════════╗")
        print("║  👻 GHOST MARKETER — SETUP MENU                ║")
        print("╠═══════════════════════════════════════════════════╣")
        print("║  1. 🌐 Setup WordPress Connection              ║")
        print("║  2. 🐦 Setup Twitter/X API                    ║")
        print("║  3. 🔍 Setup SEO Preferences                   ║")
        print("║  4. 🖼️ Setup Image Generation                 ║")
        print("║  5. 📅 Setup Scheduling                        ║")
        print("║  6. 📊 View Current Configuration             ║")
        print("║  7. 🚀 RUN GHOST MARKETER NOW                 ║")
        print("║  0. 🚪 Exit                                    ║")
        print("╚═══════════════════════════════════════════════════╝")
        
        choice = input("\n   Select option: ").strip()
        
        if choice == '1':
            setup_wordpress()
        elif choice == '2':
            setup_twitter()
        elif choice == '3':
            setup_seo_preferences()
        elif choice == '4':
            setup_image_generation()
        elif choice == '5':
            setup_scheduling()
        elif choice == '6':
            config = load_config()
            print("\n📋 Current Configuration:")
            print(json.dumps(config, indent=2))
        elif choice == '7':
            run_now()
        elif choice == '0':
            print("\n👻 Ghost Marketer setup complete!")
            print("   Run: python3 GHOST_MARKETER.py <wp_url> <wp_token>")
            break
        else:
            print("\n⚠️ Invalid option")

if __name__ == "__main__":
    main()

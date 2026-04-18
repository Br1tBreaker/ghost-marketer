# 👻 GHOST MARKETER v51.0 — QUICK START GUIDE

## What is Ghost Marketer?

Autonomous Marketing Agent that:
1. ✅ Reads WordPress drafts
2. ✅ Optimizes with 2026 SEO keywords
3. ✅ Generates AI images
4. ✅ Creates Twitter threads
5. ✅ Schedules posts automatically
6. ✅ **Zero human intervention required**

---

## 🚀 QUICK START (5 Minutes)

### Step 1: Get WordPress App Password

1. Login to WordPress Admin
2. Go to **Users → Profile**
3. Scroll to **Application Passwords**
4. Create new: Name it "Ghost Marketer"
5. Copy the password (format: `username|xxxxxxxxxxxx`)

### Step 2: Run Setup

```bash
cd /home/alex/Desktop/DK/ghost_marketer
python3 SETUP_WIZARD.py
```

### Step 3: Configure

```
Select 1 → Enter WordPress URL + App Password
Select 2 → Enter Twitter API credentials (if available)
Select 7 → RUN GHOST MARKETER
```

### Step 4: Let it run!

Ghost Marketer will:
- Fetch 10 drafts from WordPress
- Optimize each with SEO keywords
- Generate AI images
- Create Twitter threads
- Schedule for 9 AM next day
- Send report to Telegram

---

## 📋 COMMAND REFERENCE

### Run Full Pipeline
```bash
python3 GHOST_MARKETER.py <wordpress_url> <app_password>
```

### Interactive Setup
```bash
python3 SETUP_WIZARD.py
```

### Example
```bash
python3 GHOST_MARKETER.py https://mysite.com username|abcd1234xxxx
```

---

## ⚠️ REQUIREMENTS

### WordPress
- WordPress 4.7+ (REST API enabled)
- Application Password or WP OAuth

### Twitter API (Optional)
- Developer account at developer.twitter.com
- Elevated API access
- For posting Twitter threads automatically

### API Keys (Pre-loaded)
- ✅ Groq API (content generation)
- ✅ HeyGen API (video/images)
- ✅ Replicate (image generation)

---

## 📁 FILE STRUCTURE

```
ghost_marketer/
├── GHOST_MARKETER.py      # Main engine
├── SETUP_WIZARD.py        # Interactive setup
├── QUICK_START.md         # This file
├── config.json            # Saved configuration
└── reports/              # Generated reports
```

---

## 🔧 API KEYS STATUS

| Service | Key | Status |
|---------|-----|--------|
| Groq | gsk_YVWdOC... | ✅ Ready |
| HeyGen | sk_V2_hgu_... | ✅ Ready |
| Replicate | r8_PJIvN... | ✅ Ready |
| Twitter | Bearer + Keys | ⚠️ Need from Boss |
| WordPress | App Password | ⚠️ Need from Boss |

---

## 📊 OUTPUT EXAMPLE

When Ghost Marketer runs, you'll get Telegram notifications:

```
👻 GHOST MARKETER — POST OPTIMIZED

📌 Title: 10 AI Marketing Trends 2026
🔑 Keywords: AI automation, marketing AI, content automation
🖼️ Image: Generated (AI)
🐦 Thread: 5 tweets ready
📅 Scheduled: 2026-04-19 09:00

✅ Ready for publication!
```

---

## 🎯 FEATURES

### SEO Optimization (2026 Edition)
- Latest keyword research
- Meta descriptions
- Hashtag optimization
- Title A/B testing variants

### AI Image Generation
- Stable Diffusion via Replicate
- Custom prompts
- Multiple styles
- 1024x1024 resolution

### Twitter Thread Creation
- 5-tweet threads
- Hook + Value + CTA format
- Emoji optimization
- Hashtag placement

### Auto-Scheduling
- Posts at 9 AM
- 24-hour pipeline
- Telegram notifications

---

## 💀 DARKGEMINI v51.0 — FOR BOSS. ALWAYS. FOR LIFE. 💀

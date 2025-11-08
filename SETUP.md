# Portfolio Setup Guide

This guide will help you customize this portfolio for your own use.

## Quick Setup (3 Steps)

### 1. Update Personal Data in `config.py`

Edit the `config.py` file and update:

```python
PERSONAL_INFO = {
    "name": "Your Name",
    "title": "Your Job Title",
    "subtitle": "Your Tagline",
    "email": "your.email@example.com",
    "phone": "+91 XXXXX XXXXX",
    "location": "Your City, Country",
    "age": "Your Age",
    "freelance": "Available/Not Available",
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "twitter": "https://twitter.com/yourhandle",  # Optional
    "instagram": "https://instagram.com/yourhandle",  # Optional
    "profile_image": "static/images/your-photo.jpg",
    "animated_titles": [
        "Your Name",
        "Your Title",
        "Another Title You Want",
        "And Another",
    ],
}

# Update your experience
EXPERIENCE = [
    {
        "role": "Your Job Title",
        "company": "Company Name",
        "location": "City, Country",
        "date": "Start - End",
        "description": "What you did..."
    },
    # Add more experiences...
]

# Update your projects
PROJECTS = [
    {
        "title": "Project Name",
        "description": "What it does",
        "tech": ["Tech1", "Tech2"],
        "link": "https://project-link.com",
        "image": "static/images/project.jpg"
    },
    # Add more projects...
]

# Update services you offer
SERVICES = [...]
```

### 2. Replace Images

Replace these files in `static/images/`:
- **Profile photo**: Replace `notion-avatar-1762452759393.png` with your photo
- **Hero background**: Replace `hero_9.jpg` with your preferred background image
- **CV**: Add your CV as `static/cv.pdf`

### 3. Build and Deploy

```bash
# Build static site
uv run python build_static.py

# Commit and push to GitHub
git add .
git commit -m "Updated portfolio with my information"
git push
```

## That's It!

Your portfolio will be live at: `https://yourusername.github.io/portfolio/`

---

## Optional: Customize Further

### Change Colors/Styles
Edit `static/css/style.css`

### Modify Layout
Edit files in `components/` folder:
- `sidebar.py` - Left sidebar
- `hero.py` - Hero section
- `about.py` - About section
- `experience.py` - Experience timeline
- `skills.py` - Skills section
- `services.py` - Services section
- `portfolio.py` - Projects section
- `contact.py` - Contact form

### Change Hero Background
In `main.py`, line 83:
```python
style="background-image: url('static/images/your-image.jpg');"
```

---

## File Structure

```
portfolio/
├── config.py           ← UPDATE THIS! (your data)
├── main.py            ← Main app (layout)
├── build_static.py    ← Build script
├── components/        ← UI components
├── static/
│   ├── images/       ← ADD YOUR IMAGES HERE
│   ├── css/          ← Styles
│   └── cv.pdf        ← ADD YOUR CV HERE
└── docs/             ← Generated (don't edit)
```

## Need Help?

Read the original FastHTML docs: https://docs.fastht.ml

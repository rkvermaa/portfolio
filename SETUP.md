# Portfolio Setup Guide

This guide will help you customize this portfolio for your own use.

## Quick Setup (4 Steps)

### 1. Update Personal Data in `config.py`

Edit the `config.py` file and update:

```python
# Personal Information
PERSONAL_INFO = {
    "name": "Your Name",
    "title": "Your Job Title",
    "subtitle": "Your Tagline",
    "email": "your.email@example.com",
    "phone": "+91 XXXXX XXXXX",
    "location": "Your City, Country",
    "birth_year": 1990,  # Your birth year (age will be auto-calculated)
    "freelance": "Available",  # or "Not Available"
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "profile_image": "static/images/your-photo.jpg",
    "animated_titles": [
        "Your Name",
        "Your Job Title",
        "Another Title You Want",
        "And Another",
    ],
}

# Web3Forms Access Key for contact form
WEB3FORMS_ACCESS_KEY = "your-access-key-here"  # Get from https://web3forms.com

# Update your experience
EXPERIENCE = [
    {
        "company": "Company Name",
        "location": "City, Country",
        "role": "Your Job Title",
        "date": "Start Date - End Date",
        "description": "What you did at this company..."
    },
    # Add more experiences...
]

# Update your projects
PROJECTS = [
    {
        "title": "Project Name",
        "description": "What the project does and your role",
        "icon": "code",  # Lucide icon name
        "gradient": "from-blue-500 to-purple-600",
        "tech": ["Tech1", "Tech2", "Tech3"],
        "link": "#",  # or your project URL
        "category": "Category Name"
    },
    # Add more projects...
]

# Update services you offer
SERVICES = [
    {
        "title": "Service Name",
        "icon": "✨",
        "lucide_icon": "sparkles",  # Lucide icon name
        "items": [
            "Service feature 1",
            "Service feature 2",
            "Service feature 3"
        ]
    },
    # Add more services...
]
```

### 2. Get Web3Forms Access Key

1. Visit: https://web3forms.com/
2. Enter your email (the email where you want to receive messages)
3. Click "Create Access Key"
4. Copy the access key
5. Update `WEB3FORMS_ACCESS_KEY` in `config.py`

### 3. Replace Images

Replace these files in `static/images/`:
- **Profile photo**: Replace with your photo (PNG, JPG)
- **CV**: Add your CV as `static/cv.pdf`

Update the `profile_image` path in `config.py`:
```python
"profile_image": "static/images/your-photo.jpg"
```

### 4. Build and Deploy

```bash
# Build static site
uv run python build_static.py

# Commit and push to GitHub
git add .
git commit -m "Updated portfolio with my information"
git push
```

Your portfolio will be live at: `https://yourusername.github.io/portfolio/`

---

## Advanced Customization

### Change Typography

1. Choose a font from [Google Fonts](https://fonts.google.com/)
2. Update `main.py` around line 43:
```python
Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=YourFont:wght@300;400;500;600;700;800&display=swap"),
```

3. Update `static/css/style.css` around line 5:
```css
body {
    font-family: 'YourFont', system-ui, -apple-system, sans-serif;
    ...
}
```

Popular font choices:
- **Poppins** (current) - Modern & professional
- **Inter** - Clean & readable
- **Nunito** - Rounded & friendly
- **Plus Jakarta Sans** - Professional & warm
- **DM Sans** - Elegant

### Change Colors/Theme

Edit `static/css/style.css` to modify:

**Brand Gradient Colors** (blue-purple-pink):
```css
/* Search for "from-blue-500" and replace throughout */
bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500
```

**Sidebar Background**:
```css
bg-white/30 backdrop-blur-md  /* Adjust opacity (30) */
```

**Navbar Background**:
```css
bg-white/30 backdrop-blur-md  /* Adjust opacity (30) */
```

### Modify Layout

Edit files in `components/` folder:

- **`hero.py`** - Landing section with typing animation
- **`sidebar.py`** - Left sidebar with profile info
- **`about.py`** - About Me section
- **`experience.py`** - Experience timeline
- **`skills.py`** - Skills section
- **`portfolio.py`** - Projects section
- **`services.py`** - Services section
- **`contact.py`** - Contact form

### Change Section Order

Edit `main.py` around line 327 to reorder sections:

```python
# Rest of sections - slides OVER the hero section
Div(
    AboutSection(),
    ExperienceSection(EXPERIENCE),
    SkillsSection(),
    PortfolioSection(PROJECTS),  # Swap these
    ServicesSection(SERVICES),   # two if needed
    ContactSection(...),
    ...
)
```

Make sure navbar order matches (around line 301-307).

### Add/Remove Sections

**To Remove a Section:**
1. Comment out or delete the section in `main.py`
2. Remove the corresponding navbar link
3. Remove the import at the top of `main.py`

**To Add a New Section:**
1. Create a new component file in `components/`
2. Import it in `main.py`
3. Add it to the page layout
4. Add a navbar link

---

## File Structure

```
portfolio/
├── config.py              ← UPDATE THIS! (your data)
├── main.py                ← Main app (layout & routing)
├── build_static.py        ← Build script for deployment
├── components/            ← UI components (modular sections)
│   ├── hero.py           ← Landing section
│   ├── sidebar.py        ← Sidebar with profile
│   ├── about.py          ← About section
│   ├── experience.py     ← Experience timeline
│   ├── skills.py         ← Skills showcase
│   ├── portfolio.py      ← Projects section
│   ├── services.py       ← Services offered
│   └── contact.py        ← Contact form
├── static/
│   ├── css/
│   │   └── style.css     ← Custom styles
│   ├── images/           ← ADD YOUR IMAGES HERE
│   └── cv.pdf            ← ADD YOUR CV HERE
└── docs/                 ← Generated static site (don't edit)
```

---

## Deployment Workflow

Every time you make changes:

```bash
# 1. Test locally
uv run python main.py
# Visit http://localhost:5001 to test

# 2. Build static site
uv run python build_static.py

# 3. Deploy to GitHub
git add .
git commit -m "Description of changes"
git push
```

Wait 2-3 minutes for GitHub Pages to update.

---

## Troubleshooting

### Contact Form Not Working

1. Check `WEB3FORMS_ACCESS_KEY` in `config.py`
2. Make sure the access key is from https://web3forms.com
3. Verify your email is correct
4. Check browser console for errors

### Images Not Showing

1. Verify image paths in `config.py`
2. Make sure images are in `static/images/`
3. Rebuild static site: `uv run python build_static.py`
4. Check browser console for 404 errors

### Styles Not Updating

1. Update CSS version in `main.py` line 41:
```python
Link(rel="stylesheet", href="static/css/style.css?v=12"),  # Increment version
```
2. Rebuild: `uv run python build_static.py`
3. Clear browser cache (Ctrl+Shift+R)

### Home Button Not Working

The Home button uses smooth scroll to top. If not working:
1. Check `main.py` line 301 has the onclick handler
2. Clear browser cache
3. Rebuild and redeploy

---

## Need Help?

- **FastHTML Docs**: https://docs.fastht.ml
- **Web3Forms**: https://web3forms.com/
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Lucide Icons**: https://lucide.dev/icons

---

## Tips for Best Results

✅ **Keep it Simple**: Don't overcomplicate - the template is designed to be clean and professional

✅ **Use Quality Images**: High-resolution images make a big difference

✅ **Write Clear Descriptions**: Focus on impact and results in your experience/projects

✅ **Test Responsively**: Check your site on mobile, tablet, and desktop

✅ **Update Regularly**: Keep your portfolio current with latest projects and skills

✅ **Proofread**: Check for typos and grammar before deploying

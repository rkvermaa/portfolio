# Portfolio Website - Built with FastHTML

A modern, responsive portfolio website with glassmorphism design and smooth animations.

## 🎯 Features

- **Modern Glassmorphism Design**: Frosted glass effects with backdrop blur
- **Fully Responsive**: Mobile-first design with hamburger menu
- **Typing Animation**: Dynamic hero section with cycling titles
- **Contact Form**: Integrated with Web3Forms for email notifications
- **Clean Architecture**: Modular components and centralized configuration
- **Poppins Typography**: Professional and modern font styling
- **Smooth Animations**: Fade-in effects and hover interactions
- **GitHub Pages Ready**: Static site generation for easy deployment

## 🚀 Quick Start

### Development Server

Run the development server:
```bash
uv run python main.py
```

Visit: http://localhost:5001

### Build Static Site

Generate static files for deployment:
```bash
uv run python build_static.py
```

Static files will be created in `docs/` folder.

## 📁 Project Structure

```
portfolio/
├── main.py                 # Main application entry point
├── config.py              # UPDATE THIS with your data!
├── build_static.py        # Static site builder for GitHub Pages
├── components/            # UI components
│   ├── hero.py           # Landing/Hero section
│   ├── about.py          # About Me section
│   ├── experience.py     # Work experience timeline
│   ├── skills.py         # Skills showcase
│   ├── portfolio.py      # Projects/Portfolio section
│   ├── services.py       # Services offered
│   ├── contact.py        # Contact form with Web3Forms
│   └── sidebar.py        # Sidebar with profile info
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles and animations
│   └── images/           # Your images (profile, projects, etc.)
├── docs/                 # Generated static site (GitHub Pages)
├── README.md             # This file
└── SETUP.md              # Detailed setup guide
```

## ✏️ Customization

### 1. Update Personal Information

Edit `config.py` and update:

```python
PERSONAL_INFO = {
    "name": "Your Name",
    "title": "Your Job Title",
    "subtitle": "Your Tagline",
    "email": "your.email@example.com",
    "phone": "+91 XXXXX XXXXX",
    "location": "Your City, Country",
    "birth_year": 1990,  # Age will be auto-calculated
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "profile_image": "static/images/your-photo.jpg",
    "animated_titles": [
        "Your Name",
        "Your Title",
        "Another Title",
    ],
}

# Update your experience
EXPERIENCE = [...]

# Update your projects
PROJECTS = [...]

# Update services you offer
SERVICES = [...]
```

### 2. Add Your Images

Replace images in `static/images/`:
- **Profile photo**: Your profile picture
- **Hero background**: Background image for hero section
- **CV**: Add your CV as `static/cv.pdf`

### 3. Configure Contact Form

Update the Web3Forms access key in `config.py`:
```python
WEB3FORMS_ACCESS_KEY = "your-access-key-here"
```

Get your free access key at: https://web3forms.com/

### 4. Build and Deploy

```bash
# Build static site
uv run python build_static.py

# Commit and push to GitHub
git add .
git commit -m "Update portfolio"
git push
```

Your site will be live at: `https://yourusername.github.io/portfolio/`

## 🎨 Customization Options

### Change Colors

Edit `static/css/style.css` to modify:
- Brand gradient colors
- Background colors
- Border colors
- Hover effects

### Change Font

Update `main.py` line 43:
```python
Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=YourFont:wght@300;400;500;600;700;800&display=swap"),
```

And update `static/css/style.css` line 5:
```css
font-family: 'YourFont', system-ui, -apple-system, sans-serif;
```

### Modify Components

Each section is a separate component in `components/`:
- `hero.py` - Landing section with typing animation
- `about.py` - About Me section
- `experience.py` - Work experience timeline
- `skills.py` - Skills showcase
- `portfolio.py` - Projects section
- `services.py` - Services offered
- `contact.py` - Contact form
- `sidebar.py` - Sidebar with profile info

## 🎓 Tech Stack

- **FastHTML**: Python web framework
- **Tailwind CSS**: Utility-first CSS framework (via CDN)
- **Lucide Icons**: Icon library
- **Web3Forms**: Contact form backend
- **Poppins Font**: Google Fonts typography
- **GitHub Pages**: Static site hosting

## 📚 Resources

- [FastHTML Docs](https://docs.fastht.ml)
- [Web3Forms](https://web3forms.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Lucide Icons](https://lucide.dev/)

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio!

## 📄 License

MIT License - Feel free to use this template for your own portfolio.

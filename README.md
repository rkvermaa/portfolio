# Portfolio Website - Built with FastHTML

A modern, responsive portfolio website showcasing your work as a Data Engineer & ML Engineer.

## 🎯 Features

- **Modular Architecture**: Clean separation of components, pages, and configuration
- **Fully Responsive**: Works on desktop, tablet, and mobile devices
- **Easy to Customize**: All personal data in `src/config.py`
- **Modern Design**: Clean UI with smooth animations
- **Complete Sections**: Hero, Services, Education, Experience, Projects, Contact

## 🚀 Quick Start

Run the development server:
```bash
uv run python main.py
```

Visit: http://localhost:5001

## 📁 Project Structure

```
portfolio/
├── main.py                 # Main application
├── src/
│   ├── config.py          # UPDATE THIS with your data!
│   ├── components/        # UI components
│   └── static/            # CSS & images
└── README.md
```

## ✏️ Customization

Edit `src/config.py` to update your:
- Personal information
- Skills & proficiency levels
- Work experience
- Projects
- Education

Add your images to `src/static/images/`:
- profile.jpg
- hero.jpg
- project-*.jpg

## 🎓 Learning FastHTML

Key concepts used in this project:

1. **FastTags**: Python → HTML
2. **Components**: Reusable UI functions
3. **Routing**: URL → Functions
4. **Auto-reload**: Edit & see changes instantly

Check the inline comments in the code for detailed explanations!

## 📚 Resources

- [FastHTML Docs](https://fastht.ml)
- All portfolio data in: `src/config.py`
- All components in: `src/components/`

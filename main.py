"""
Portfolio Website - Main Application

This is the entry point of your FastHTML application.

Key Concepts:
1. fast_app() creates your FastHTML application
2. @rt decorator creates routes (URLs that map to functions)
3. Routes return FastTags which get converted to HTML
4. serve() starts the web server
"""
from fasthtml.common import *

# Import our components
from components.sidebar import ModernSidebar
from components.hero import ModernHero
from components.about import AboutSection
from components.experience import ExperienceSection
from components.skills import SkillsSection
from components.services import ServicesSection
from components.portfolio import PortfolioSection
from components.contact import ContactSection

# Import configuration data
from config import (
    PERSONAL_INFO, SKILLS, HERO, SERVICES,
    EXPERIENCE, PROJECTS
)

# Create the FastHTML app with Tailwind CSS + custom CSS
# FastHTML automatically serves files from 'static/' directory
app, rt = fast_app(
    hdrs=(
        # Tailwind CSS via CDN
        Script(src="https://cdn.tailwindcss.com"),
        # Modern CSS for animations and custom styles
        Link(rel="stylesheet", href="static/css/style.css?v=8"),
        # Google Fonts for modern typography
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"),
        # Lucide Icons
        Script(src="https://unpkg.com/lucide@latest"),
    ),
    pico=False  # Disable default Pico CSS
)

# Teaching moment:
# All data is now imported from config.py
# This makes it easier to update your portfolio without touching the main code


@rt("/")
def get():
    """
    Home page route.

    Teaching moment:
    - @rt("/") means this function handles requests to the root URL (homepage)
    - The function name doesn't matter (we use 'get' by convention for GET requests)
    - We return a tuple of FastTags, which becomes a complete HTML page
    - Title() sets the browser tab title
    - Div with class="container" wraps everything in a layout container
    """

    # Teaching moment:
    # All data comes from src/config.py - making it easy to update
    # We use **PERSONAL_INFO to unpack the dictionary as keyword arguments

    # Prepare animated titles for typing effect (including name)
    animated_titles = [
        "Ravi Kumar Verma",
        "Full-Stack AI Engineer",
        "GenAI Solutions Architect",
        "LLM Specialist",
        "AI/ML Solutions Builder"
    ]

    return (
        Title(f"{PERSONAL_INFO['name']} - {PERSONAL_INFO['title']}"),

        # Layer 1: Fixed background image that never moves
        Div(
            cls="fixed inset-0 bg-cover bg-center bg-no-repeat",
            style="background-image: url('static/images/maxim-berg-qHJiyaCTVPw-unsplash.jpg');"
        ),

        # Dark overlay to reduce brightness of background
        Div(
            cls="fixed inset-0 bg-black/20"
        ),

        # Layer 2: Scrollable sidebar
        ModernSidebar(
            name=PERSONAL_INFO["name"],
            title=PERSONAL_INFO["title"],
            subtitle=PERSONAL_INFO["subtitle"],
            email=PERSONAL_INFO["email"],
            phone=PERSONAL_INFO.get("phone", "+91 XXXXX XXXXX"),
            location=PERSONAL_INFO.get("location", "India"),
            age=PERSONAL_INFO.get("age", "25 Years"),
            freelance=PERSONAL_INFO.get("freelance", "Available"),
            linkedin=PERSONAL_INFO.get("linkedin", "#"),
            github=PERSONAL_INFO.get("github", "#"),
            twitter=PERSONAL_INFO.get("twitter", "#"),
            instagram=PERSONAL_INFO.get("instagram", "#"),
            profile_image=PERSONAL_INFO["profile_image"],
            skills_major=SKILLS["major"]
        ),

        # Layer 3: Scrollable main content with light transparent overlay
        Div(
            # Full-width navigation bar from sidebar edge to right edge
            Nav(
                Div(
                    A("Home", href="#hero", cls="nav-link"),
                    A("About", href="#about", cls="nav-link"),
                    A("Experience", href="#experience", cls="nav-link"),
                    A("Skills", href="#skills", cls="nav-link"),
                    A("Portfolio", href="#portfolio", cls="nav-link"),
                    A("Services", href="#services", cls="nav-link"),
                    A("Contact", href="#contact", cls="contact-btn"),
                    cls="flex items-center justify-center gap-2"
                ),
                cls="fixed top-0 left-0 lg:left-80 right-0 z-40 bg-white/30 backdrop-blur-md px-12 py-3 shadow-lg border-b border-gray-300/50"
            ),

            # Hero section - FIXED like background, doesn't scroll
            Div(
                Div(
                    # Hi There! - static with waving hand
                    P(
                        Span("Hi There!", cls="font-bold"),
                        Span(" 👋", cls="inline-block wave-hand"),
                        cls="text-xl md:text-2xl text-blue-200 mb-6 animate-fade-in tracking-wide"
                    ),
                    # I Am [typing animation] - cycles through name and titles
                    Div(
                        Span("I Am ", cls="text-xl md:text-3xl lg:text-4xl text-white font-light"),
                        Span(
                            "",
                            id="typing-text",
                            cls="text-xl md:text-3xl lg:text-4xl text-blue-400 font-bold"
                        ),
                        Span(
                            "|",
                            cls="text-xl md:text-3xl lg:text-4xl text-blue-400 animate-blink ml-1"
                        ),
                        cls="mb-10"
                    ),
                    # Scroll indicator - minimal
                    Div(
                        Button(
                            Div(
                                Span("Scroll to explore", cls="text-white/70 text-sm font-light mb-2"),
                                I(data_lucide="chevron-down", cls="w-6 h-6 text-white/70 animate-bounce mx-auto"),
                                cls="flex flex-col items-center"
                            ),
                            onclick="window.scrollTo({ top: window.innerHeight, behavior: 'smooth' })",
                            cls="hover:text-white transition-all duration-300 cursor-pointer bg-transparent border-0"
                        ),
                        cls="flex justify-center"
                    ),
                    cls="relative z-10 text-center"
                ),
                cls="fixed inset-0 left-0 lg:left-80 flex items-center justify-center pt-20"
            ),

            # Spacer to push content down (invisible, takes up hero space)
            Div(cls="h-screen"),

            # Rest of sections - slides OVER the hero section
            Div(
                # About Me section
                AboutSection(),

                # Experience section - right after About Me
                ExperienceSection(EXPERIENCE),

                # Skills section with colored icons
                SkillsSection(),

                # Services/Skills section
                ServicesSection(SERVICES),

                # Portfolio/Projects section
                PortfolioSection(PROJECTS),

                # Contact section
                ContactSection(
                    email=PERSONAL_INFO["email"],
                    phone=PERSONAL_INFO["phone"],
                    location=PERSONAL_INFO["location"]
                ),

                # Footer
                Footer(
                    Div(
                        # Decorative line
                        Div(cls="w-full h-px bg-gradient-to-r from-transparent via-gray-300 to-transparent mb-8"),

                        # Footer content
                        Div(
                            # Tagline
                            P(
                                "Building the future, one line of code at a time",
                                cls="text-gray-600 text-lg font-medium mb-4 text-center"
                            ),

                            # Copyright
                            Div(
                                Span("© ", cls="text-gray-500"),
                                Span("2025", cls="text-gray-700 font-semibold"),
                                Span(" ", cls="text-gray-500"),
                                Span(PERSONAL_INFO["name"], cls="text-transparent bg-clip-text bg-gradient-to-r from-blue-500 to-purple-600 font-bold"),
                                Span(". All rights reserved.", cls="text-gray-500"),
                                cls="text-center mb-2"
                            ),

                            # Made with love
                            P(
                                Span("Crafted with ", cls="text-gray-500"),
                                Span("❤️", cls="text-red-500 animate-pulse"),
                                Span(" and ", cls="text-gray-500"),
                                Span("☕", cls=""),
                                Span(" using FastHTML", cls="text-gray-500"),
                                cls="text-sm text-center"
                            ),

                            cls="fade-in-scroll"
                        ),

                        cls="container mx-auto px-8 md:px-16"
                    ),
                    cls="py-12 bg-gray-50 relative overflow-hidden"
                ),

                cls="relative z-30 bg-white"  # Slides over hero with higher z-index
            ),

            # Typing animation script
            Script(f"""
                const titles = {animated_titles};
                let titleIndex = 0;
                let charIndex = 0;
                let isDeleting = false;
                const typingSpeed = 100;
                const deletingSpeed = 50;
                const pauseTime = 2000;

                function typeEffect() {{
                    const titleElement = document.getElementById('typing-text');
                    if (!titleElement) return;

                    const currentTitle = titles[titleIndex];

                    if (!isDeleting) {{
                        // Typing
                        titleElement.textContent = currentTitle.substring(0, charIndex + 1);
                        charIndex++;

                        if (charIndex === currentTitle.length) {{
                            // Finished typing, wait then start deleting
                            isDeleting = true;
                            setTimeout(typeEffect, pauseTime);
                            return;
                        }}
                    }} else {{
                        // Deleting
                        titleElement.textContent = currentTitle.substring(0, charIndex - 1);
                        charIndex--;

                        if (charIndex === 0) {{
                            // Finished deleting, move to next title
                            isDeleting = false;
                            titleIndex = (titleIndex + 1) % titles.length;
                        }}
                    }}

                    const speed = isDeleting ? deletingSpeed : typingSpeed;
                    setTimeout(typeEffect, speed);
                }}

                // Start animation when page loads
                document.addEventListener('DOMContentLoaded', () => {{
                    setTimeout(typeEffect, 500);
                }});
            """),

            # Initialize Lucide icons
            Script("""
                document.addEventListener('DOMContentLoaded', () => {
                    lucide.createIcons();
                });
            """),

            # Scroll animation for about section
            Script("""
                // Intersection Observer for scroll animations
                const observerOptions = {
                    threshold: 0.1,
                    rootMargin: '0px 0px -100px 0px'
                };

                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('visible');
                        }
                    });
                }, observerOptions);

                // Observe all fade-in-scroll elements
                document.addEventListener('DOMContentLoaded', () => {
                    const elements = document.querySelectorAll('.fade-in-scroll');
                    elements.forEach(el => observer.observe(el));
                });
            """),

            cls="ml-0 lg:ml-80 relative"  # Offset by sidebar width
        )
    )


# Start the server
# This checks if the script is run directly (not imported)
# and starts uvicorn on port 5001
serve()

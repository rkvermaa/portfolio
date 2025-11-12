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
from datetime import datetime

# Import our components
from components.sidebar import ModernSidebar
from components.hero import HeroSection
from components.about import AboutSection
from components.experience import ExperienceSection
from components.skills import SkillsSection
from components.services import ServicesSection
from components.portfolio import PortfolioSection
from components.contact import ContactSection

# Import configuration data
from config import (
    PERSONAL_INFO, SKILLS, HERO, SERVICES,
    EXPERIENCE, PROJECTS, WEB3FORMS_ACCESS_KEY
)

# Create the FastHTML app with Tailwind CSS + custom CSS
# FastHTML automatically serves files from 'static/' directory
app, rt = fast_app(
    hdrs=(
        # Favicons - multiple sizes for better quality
        Link(rel="icon", type="image/png", sizes="32x32", href=f"static/images/{PERSONAL_INFO['profile_image'].split('/')[-1]}"),
        Link(rel="icon", type="image/png", sizes="16x16", href=f"static/images/{PERSONAL_INFO['profile_image'].split('/')[-1]}"),
        Link(rel="apple-touch-icon", sizes="180x180", href=f"static/images/{PERSONAL_INFO['profile_image'].split('/')[-1]}"),
        # Tailwind CSS via CDN
        Script(src="https://cdn.tailwindcss.com"),
        # Modern CSS for animations and custom styles
        Link(rel="stylesheet", href="static/css/style.css?v=11"),
        # Google Fonts for modern typography
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap"),
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

    # Prepare animated titles for typing effect (from config)
    animated_titles = PERSONAL_INFO.get("animated_titles", [
        PERSONAL_INFO["name"],
        PERSONAL_INFO["title"],
        "GenAI Solutions Architect",
        "LLM Specialist",
        "AI/ML Solutions Builder"
    ])

    return (
        Title(f"{PERSONAL_INFO['name']} - {PERSONAL_INFO['title']}"),

        # Layer 1: Fixed background image that never moves
        Div(
            cls="fixed inset-0 bg-cover bg-center bg-no-repeat",
            style="background-image: url('static/images/hero_9.jpg');"
        ),

        # Dark overlay to reduce brightness of background
        Div(
            cls="fixed inset-0 bg-black/20"
        ),

        # Layer 2: Scrollable sidebar (width: 16rem/256px)
        ModernSidebar(
            name=PERSONAL_INFO["name"],
            title=PERSONAL_INFO["title"],
            subtitle=PERSONAL_INFO["subtitle"],
            email=PERSONAL_INFO["email"],
            phone=PERSONAL_INFO.get("phone", "+91 XXXXX XXXXX"),
            location=PERSONAL_INFO.get("location", "India"),
            age=PERSONAL_INFO.get("age", "25 Years"),
            birth_year=PERSONAL_INFO.get("birth_year"),  # Auto-calculates age
            freelance=PERSONAL_INFO.get("freelance", "Available"),
            linkedin=PERSONAL_INFO.get("linkedin", "#"),
            github=PERSONAL_INFO.get("github", "#"),
            medium=PERSONAL_INFO.get("medium", "#"),
            twitter=PERSONAL_INFO.get("twitter", "#"),
            instagram=PERSONAL_INFO.get("instagram", "#"),
            profile_image=PERSONAL_INFO["profile_image"],
            skills_major=SKILLS["major"]
        ),

        # Layer 3: Scrollable main content with light transparent overlay
        Div(
            # Mobile hamburger menu button - only visible on mobile
            Button(
                I(data_lucide="menu", cls="w-6 h-6"),
                onclick="document.getElementById('mobile-sidebar').classList.toggle('translate-x-full')",
                cls="fixed top-4 left-4 z-50 lg:hidden bg-white/30 backdrop-blur-md p-2 rounded-full shadow-lg border border-gray-300/50 hover:bg-white/50 transition-all"
            ),

            # Mobile sidebar drawer - slides in from right
            Div(
                # Close button
                Button(
                    I(data_lucide="x", cls="w-6 h-6"),
                    onclick="document.getElementById('mobile-sidebar').classList.add('translate-x-full')",
                    cls="absolute top-4 right-4 bg-white/20 hover:bg-white/30 p-2 rounded-full transition-all"
                ),

                # Sidebar content for mobile
                Div(
                    # Profile section
                    Div(
                        Div(
                            Img(
                                src=PERSONAL_INFO["profile_image"],
                                alt=PERSONAL_INFO["name"],
                                cls="w-24 h-24 rounded-full border-2 border-blue-400/50 shadow-xl mx-auto"
                            ),
                            cls="mb-4"
                        ),
                        H2(PERSONAL_INFO["name"], cls="text-lg font-bold text-white text-center mb-2 leading-tight"),
                        P(PERSONAL_INFO["title"], cls="text-xs text-blue-200 text-center mb-1 px-2"),
                        P(PERSONAL_INFO["subtitle"], cls="text-[10px] text-blue-300/80 text-center mb-4 px-2"),
                        cls="mb-5"
                    ),

                    # Social links
                    Div(
                        A(I(data_lucide="linkedin", cls="w-4 h-4"), href=PERSONAL_INFO.get("linkedin", "#"), target="_blank", cls="text-white/60 hover:text-blue-400 transition-colors"),
                        A(I(data_lucide="github", cls="w-4 h-4"), href=PERSONAL_INFO.get("github", "#"), target="_blank", cls="text-white/60 hover:text-blue-400 transition-colors"),
                        A(I(data_lucide="pen-line", cls="w-4 h-4"), href=PERSONAL_INFO.get("medium", "#"), target="_blank", cls="text-white/60 hover:text-emerald-400 transition-colors", title="Medium"),
                        A(I(data_lucide="graduation-cap", cls="w-4 h-4"), href="static/coming-soon.html", target="_blank", cls="text-white/60 hover:text-teal-400 transition-colors", title="Learning Hub"),
                        cls="flex gap-5 justify-center mb-5"
                    ),

                    # Contact info - properly aligned
                    Div(
                        Div(
                            Span("Email:", cls="text-white/70 text-xs font-bold"),
                            A(PERSONAL_INFO["email"], href=f"mailto:{PERSONAL_INFO['email']}", cls="text-white/80 text-xs hover:text-blue-400 transition-colors break-all"),
                            cls="flex justify-between mb-2 px-2 gap-2"
                        ),
                        Div(
                            Span("Language:", cls="text-white/70 text-xs font-bold"),
                            Span("Hindi, English", cls="text-white/80 text-xs"),
                            cls="flex justify-between mb-2 px-2"
                        ),
                        Div(
                            Span("Phone:", cls="text-white/70 text-xs font-bold"),
                            Span(PERSONAL_INFO["phone"], cls="text-white/80 text-xs"),
                            cls="flex justify-between mb-2 px-2"
                        ),
                        Div(
                            Span("Location:", cls="text-white/70 text-xs font-bold"),
                            Span(PERSONAL_INFO["location"], cls="text-white/80 text-xs"),
                            cls="flex justify-between mb-2 px-2"
                        ),
                        Div(
                            Span("Age:", cls="text-white/70 text-xs font-bold"),
                            Span(PERSONAL_INFO.get("age", "25 Years"), cls="text-white/80 text-xs"),
                            cls="flex justify-between mb-2 px-2"
                        ),
                        Div(
                            Span("Freelance:", cls="text-white/70 text-xs font-bold"),
                            Span(PERSONAL_INFO.get("freelance", "Available"), cls="text-green-400 text-xs font-medium"),
                            cls="flex justify-between mb-2 px-2"
                        ),
                        cls="mb-5 py-3 border-t border-b border-white/10"
                    ),

                    # Skills section - compact pills
                    Div(
                        H3("Skills", cls="text-white text-sm font-semibold mb-2 text-center"),

                        # AI & GenAI Category
                        Div(
                            Span("AI & GenAI", cls="text-blue-200 text-[11px] font-semibold mb-1 block"),
                            Div(
                                Span("Python", cls="mobile-skill-chip"),
                                Span("LLM", cls="mobile-skill-chip"),
                                Span("GenAI", cls="mobile-skill-chip"),
                                Span("RAG", cls="mobile-skill-chip"),
                                Span("Prompt Eng", cls="mobile-skill-chip"),
                                Span("Multi-Agent", cls="mobile-skill-chip"),
                                cls="flex flex-wrap gap-1"
                            ),
                            cls="mb-2"
                        ),

                        # ML & NLP Category
                        Div(
                            Span("ML & NLP", cls="text-blue-200 text-[11px] font-semibold mb-1 block"),
                            Div(
                                Span("ML", cls="mobile-skill-chip"),
                                Span("Deep Learning", cls="mobile-skill-chip"),
                                Span("NLP", cls="mobile-skill-chip"),
                                Span("Classification", cls="mobile-skill-chip"),
                                Span("Clustering", cls="mobile-skill-chip"),
                                Span("PyTorch", cls="mobile-skill-chip"),
                                cls="flex flex-wrap gap-1"
                            ),
                            cls="mb-2"
                        ),

                        # Frameworks Category
                        Div(
                            Span("Frameworks", cls="text-blue-200 text-[11px] font-semibold mb-1 block"),
                            Div(
                                Span("LangChain", cls="mobile-skill-chip"),
                                Span("LangGraph", cls="mobile-skill-chip"),
                                Span("FastAPI", cls="mobile-skill-chip"),
                                Span("Pandas", cls="mobile-skill-chip"),
                                Span("Scikit-learn", cls="mobile-skill-chip"),
                                Span("TensorFlow", cls="mobile-skill-chip"),
                                cls="flex flex-wrap gap-1"
                            ),
                            cls="mb-2"
                        ),

                        # Data & Databases Category
                        Div(
                            Span("Data & DBs", cls="text-blue-200 text-[11px] font-semibold mb-1 block"),
                            Div(
                                Span("SQL", cls="mobile-skill-chip"),
                                Span("PostgreSQL", cls="mobile-skill-chip"),
                                Span("MongoDB", cls="mobile-skill-chip"),
                                Span("Vector DBs", cls="mobile-skill-chip"),
                                Span("PySpark", cls="mobile-skill-chip"),
                                Span("Redis", cls="mobile-skill-chip"),
                                cls="flex flex-wrap gap-1"
                            ),
                            cls="mb-2"
                        ),

                        # Cloud & DevOps Category
                        Div(
                            Span("Cloud & DevOps", cls="text-blue-200 text-[11px] font-semibold mb-1 block"),
                            Div(
                                Span("AWS", cls="mobile-skill-chip"),
                                Span("Docker", cls="mobile-skill-chip"),
                                Span("Kubernetes", cls="mobile-skill-chip"),
                                Span("CI/CD", cls="mobile-skill-chip"),
                                Span("MLFlow", cls="mobile-skill-chip"),
                                Span("Langsmith", cls="mobile-skill-chip"),
                                cls="flex flex-wrap gap-1"
                            ),
                            cls="mb-2"
                        ),

                        cls="mb-5 px-2"
                    ),

                    # Learning Hub button
                    A(
                        Div(
                            I(data_lucide="graduation-cap", cls="w-5 h-5 mr-2"),
                            Span("Learning Hub", cls="font-bold"),
                            cls="flex items-center justify-center"
                        ),
                        href="static/coming-soon.html",
                        target="_blank",
                        cls="block w-full py-3 px-6 mb-3 bg-gradient-to-r from-emerald-400 via-teal-500 to-cyan-600 hover:from-emerald-500 hover:via-teal-600 hover:to-cyan-700 text-white text-center rounded-full text-sm transition-all duration-300 hover:scale-105 shadow-lg"
                    ),

                    # Download CV button
                    A(
                        "Download CV",
                        href="static/cv.pdf",
                        cls="block w-full py-3 px-6 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 hover:from-blue-600 hover:via-purple-600 hover:to-pink-600 text-white text-center rounded-full text-sm font-bold transition-all duration-300 hover:scale-105 shadow-lg"
                    ),

                    cls="p-6 pt-16"
                ),

                id="mobile-sidebar",
                cls="fixed top-0 right-0 bottom-0 w-80 max-w-[85vw] z-50 bg-gradient-to-br from-blue-600/95 to-purple-600/95 backdrop-blur-md shadow-2xl transform translate-x-full transition-transform duration-300 overflow-y-auto lg:hidden"
            ),

            # Overlay when mobile menu is open
            Div(
                onclick="document.getElementById('mobile-sidebar').classList.add('translate-x-full')",
                id="mobile-overlay",
                cls="hidden"
            ),

            # Desktop navigation bar (full menu with glassy background)
            Nav(
                Div(
                    A("Home", href="#home", onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return true;", cls="nav-link"),
                    A("About", href="#about", cls="nav-link"),
                    A("Experience", href="#experience", cls="nav-link"),
                    A("Skills", href="#skills", cls="nav-link"),
                    A("Portfolio", href="#portfolio", cls="nav-link"),
                    A("Services", href="#services", cls="nav-link"),
                    A("Contact", href="#contact", cls="px-5 py-1.5 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 hover:from-blue-600 hover:via-purple-600 hover:to-pink-600 text-white font-semibold text-sm rounded-full transition-all duration-300 hover:scale-105 shadow-lg"),
                    cls="flex items-center justify-center gap-3"
                ),
                cls="hidden lg:block fixed top-4 left-[17rem] right-4 z-40 bg-white/30 backdrop-blur-md px-4 py-1.5 shadow-lg border border-gray-300/50 rounded-full max-w-fit mx-auto"
            ),

            # Floating Learning Hub button - Desktop (aligned with navbar, expands on hover)
            A(
                I(data_lucide="graduation-cap", cls="w-4 h-4 transition-all duration-300"),
                Span("Learning", cls="max-w-0 overflow-hidden whitespace-nowrap opacity-0 group-hover:max-w-xs group-hover:opacity-100 group-hover:ml-1.5 transition-all duration-300 font-semibold text-xs"),
                href="static/coming-soon.html",
                target="_blank",
                cls="hidden lg:flex group fixed top-5 right-6 z-50 h-10 px-3 bg-gradient-to-br from-emerald-400 via-teal-500 to-cyan-600 hover:from-emerald-500 hover:via-teal-600 hover:to-cyan-700 text-white rounded-full shadow-lg hover:shadow-2xl transition-all duration-300 items-center justify-center animate-pulse hover:animate-none hover:px-4"
            ),

            # Mobile Contact button (right side, no glassy background)
            A(
                "Contact",
                href="#contact",
                cls="lg:hidden fixed top-4 right-4 z-40 px-5 py-2.5 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 hover:from-blue-600 hover:via-purple-600 hover:to-pink-600 text-white font-bold text-sm rounded-full transition-all duration-300 hover:scale-105 shadow-lg"
            ),

            # Hero section - FIXED like background, doesn't scroll
            HeroSection(animated_titles),

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

                # Portfolio/Projects section
                PortfolioSection(PROJECTS),

                # Services/Skills section
                ServicesSection(SERVICES),

                # Contact section
                ContactSection(
                    email=PERSONAL_INFO["email"],
                    phone=PERSONAL_INFO["phone"],
                    location=PERSONAL_INFO["location"],
                    linkedin=PERSONAL_INFO["linkedin"],
                    github=PERSONAL_INFO["github"],
                    web3forms_key=WEB3FORMS_ACCESS_KEY
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

                            # Copyright with dynamic year
                            Div(
                                Span("© ", cls="text-gray-500"),
                                Span(str(datetime.now().year), cls="text-gray-700 font-semibold"),
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

            # Initialize Lucide icons
            Script("""
                document.addEventListener('DOMContentLoaded', () => {
                    lucide.createIcons();

                    // Close mobile menu when clicking on navigation links
                    const mobileNavLinks = document.querySelectorAll('nav a');
                    const mobileSidebar = document.getElementById('mobile-sidebar');

                    mobileNavLinks.forEach(link => {
                        link.addEventListener('click', () => {
                            if (mobileSidebar && !mobileSidebar.classList.contains('translate-x-full')) {
                                mobileSidebar.classList.add('translate-x-full');
                            }
                        });
                    });
                });
            """),

            # Active navbar pill indicator
            Script("""
                // Update active nav link based on scroll position
                document.addEventListener('DOMContentLoaded', () => {
                    const sections = document.querySelectorAll('section[id]');
                    const navLinks = document.querySelectorAll('.nav-link');

                    function updateActiveLink() {
                        let current = '';

                        sections.forEach(section => {
                            const sectionTop = section.offsetTop;
                            const sectionHeight = section.clientHeight;
                            if (scrollY >= sectionTop - 200) {
                                current = section.getAttribute('id');
                            }
                        });

                        navLinks.forEach(link => {
                            link.classList.remove('active');
                            if (link.getAttribute('href') === '#' + current) {
                                link.classList.add('active');
                            }
                        });

                        // Set Home as active when at top
                        if (scrollY < 300) {
                            navLinks.forEach(link => link.classList.remove('active'));
                            navLinks[0].classList.add('active');
                        }
                    }

                    window.addEventListener('scroll', updateActiveLink);
                    updateActiveLink(); // Initial call
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

            cls="ml-0 lg:ml-64 relative"  # Offset by sidebar width
        )
    )


# Start the server
# This checks if the script is run directly (not imported)
# and starts uvicorn on port 5001
serve()

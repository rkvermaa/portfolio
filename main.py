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
        Link(rel="stylesheet", href="static/css/style.css?v=11"),
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
                        A(I(data_lucide="facebook", cls="w-4 h-4"), href=PERSONAL_INFO.get("twitter", "#"), target="_blank", cls="text-white/60 hover:text-blue-400 transition-colors"),
                        A(I(data_lucide="instagram", cls="w-4 h-4"), href=PERSONAL_INFO.get("instagram", "#"), target="_blank", cls="text-white/60 hover:text-blue-400 transition-colors"),
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
                    A("Home", href="#hero", cls="nav-link"),
                    A("About", href="#about", cls="nav-link"),
                    A("Experience", href="#experience", cls="nav-link"),
                    A("Skills", href="#skills", cls="nav-link"),
                    A("Portfolio", href="#portfolio", cls="nav-link"),
                    A("Services", href="#services", cls="nav-link"),
                    A("Contact", href="#contact", cls="px-5 py-1.5 bg-gray-900 text-white font-semibold text-sm rounded-full hover:bg-gray-800 transition-all duration-300"),
                    cls="flex items-center justify-center gap-3"
                ),
                cls="hidden lg:block fixed top-4 left-[17rem] right-4 z-40 bg-white/30 backdrop-blur-md px-4 py-1.5 shadow-lg border border-gray-300/50 rounded-full max-w-fit mx-auto"
            ),

            # Mobile Contact button (right side, no glassy background)
            A(
                "Contact",
                href="#contact",
                cls="lg:hidden fixed top-4 right-4 z-40 px-5 py-2.5 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 hover:from-blue-600 hover:via-purple-600 hover:to-pink-600 text-white font-bold text-sm rounded-full transition-all duration-300 hover:scale-105 shadow-lg"
            ),

            # Hero section - FIXED like background, doesn't scroll
            Div(
                Div(
                    # Hi There! - static with waving hand
                    P(
                        Span("Hi There!", cls="font-bold"),
                        Span(" 👋", cls="inline-block wave-hand"),
                        cls="text-lg sm:text-xl md:text-2xl text-blue-200 mb-4 sm:mb-6 animate-fade-in tracking-wide"
                    ),
                    # I Am [typing animation] - cycles through name and titles
                    Div(
                        Span("I Am ", cls="text-lg sm:text-xl md:text-3xl lg:text-4xl text-white font-light"),
                        Span(
                            "",
                            id="typing-text",
                            cls="text-lg sm:text-xl md:text-3xl lg:text-4xl text-blue-400 font-bold"
                        ),
                        Span(
                            "|",
                            cls="text-lg sm:text-xl md:text-3xl lg:text-4xl text-blue-400 animate-blink ml-1"
                        ),
                        cls="mb-6 sm:mb-10 px-4"
                    ),
                    # Scroll indicator - minimal
                    Div(
                        Button(
                            Div(
                                Span("Scroll to explore", cls="text-white/70 text-xs sm:text-sm font-light mb-2"),
                                I(data_lucide="chevron-down", cls="w-5 h-5 sm:w-6 sm:h-6 text-white/70 animate-bounce mx-auto"),
                                cls="flex flex-col items-center"
                            ),
                            onclick="window.scrollTo({ top: window.innerHeight, behavior: 'smooth' })",
                            cls="hover:text-white transition-all duration-300 cursor-pointer bg-transparent border-0"
                        ),
                        cls="flex justify-center"
                    ),
                    cls="relative z-10 text-center px-4"
                ),
                cls="fixed inset-0 left-0 lg:left-64 flex items-center justify-center pt-20 sm:pt-20"
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

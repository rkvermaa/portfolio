"""
Modern Fullscreen Hero Component with Typing Animation

This creates a stunning fullscreen hero section inspired by Amanda Malat's design.
"""
from fasthtml.common import *

def ModernHero(name="Your Name", titles=None, background_image=None):
    """
    Creates a modern fullscreen hero with animated typing text.

    Teaching moment:
    - We use Tailwind CSS classes for styling
    - JavaScript for the typing animation
    - Fullscreen background with overlay

    Args:
        name: Your full name
        titles: List of titles to rotate through (e.g., ["AI Engineer", "GenAI Specialist"])
        background_image: URL or path to background image
    """

    if titles is None:
        titles = ["Full-Stack AI Engineer", "GenAI Specialist", "LLM Expert"]

    if background_image is None:
        background_image = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1920&q=80"

    # Typing animation JavaScript
    typing_script = Script(f"""
        const titles = {titles};
        let titleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        const typingSpeed = 100;
        const deletingSpeed = 50;
        const pauseTime = 2000;

        function typeEffect() {{
            const titleElement = document.getElementById('typing-text');
            const currentTitle = titles[titleIndex];

            if (!isDeleting) {{
                // Typing
                titleElement.textContent = currentTitle.substring(0, charIndex + 1);
                charIndex++;

                if (charIndex === currentTitle.length) {{
                    // Pause before deleting
                    setTimeout(() => {{ isDeleting = true; }}, pauseTime);
                    return;
                }}
            }} else {{
                // Deleting
                titleElement.textContent = currentTitle.substring(0, charIndex - 1);
                charIndex--;

                if (charIndex === 0) {{
                    isDeleting = false;
                    titleIndex = (titleIndex + 1) % titles.length;
                }}
            }}

            const speed = isDeleting ? deletingSpeed : typingSpeed;
            setTimeout(typeEffect, speed);
        }}

        // Start typing animation when page loads
        document.addEventListener('DOMContentLoaded', () => {{
            setTimeout(typeEffect, 500);
        }});
    """)

    return Div(
        # Background image with overlay
        Div(
            cls="absolute inset-0 bg-cover bg-center bg-no-repeat",
            style=f"background-image: url('{background_image}');"
        ),
        # Dark overlay for better text readability
        Div(cls="absolute inset-0 bg-gradient-to-br from-slate-900/90 via-blue-900/80 to-slate-900/90"),

        # Content
        Div(
            # Greeting text
            P(
                "Hi There!",
                cls="text-lg md:text-xl text-blue-300 mb-4 animate-fade-in font-light tracking-wide"
            ),

            # Main heading with name
            H1(
                f"I Am {name}",
                cls="text-4xl md:text-6xl lg:text-7xl font-bold text-white mb-6 animate-slide-up"
            ),

            # Animated subtitle
            Div(
                Span("I Am ", cls="text-2xl md:text-3xl lg:text-4xl text-gray-300 font-light"),
                Span(
                    titles[0] if titles else "AI Engineer",
                    id="typing-text",
                    cls="text-2xl md:text-3xl lg:text-4xl text-blue-400 font-semibold"
                ),
                Span(
                    "|",
                    cls="text-2xl md:text-3xl lg:text-4xl text-blue-400 animate-blink ml-1"
                ),
                cls="mb-8"
            ),

            # CTA Buttons
            Div(
                A(
                    "View My Work",
                    href="#portfolio",
                    cls="px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-semibold transition-all duration-300 hover:scale-105 hover:shadow-xl inline-block mr-4"
                ),
                A(
                    "Contact Me",
                    href="#contact",
                    cls="px-8 py-4 border-2 border-white hover:bg-white hover:text-gray-900 text-white rounded-lg font-semibold transition-all duration-300 inline-block"
                ),
                cls="flex flex-wrap gap-4"
            ),

            # Social links
            Div(
                A("💼", href="#", cls="text-3xl hover:scale-125 transition-transform"),
                A("🔗", href="#", cls="text-3xl hover:scale-125 transition-transform"),
                A("📧", href="#", cls="text-3xl hover:scale-125 transition-transform"),
                cls="flex gap-6 mt-12 animate-fade-in-delay"
            ),

            cls="relative z-10 flex flex-col items-start justify-center px-8 md:px-16 lg:px-24"
        ),

        # Typing animation script
        typing_script,

        cls="relative w-full h-screen flex items-center overflow-hidden",
        id="hero"
    )

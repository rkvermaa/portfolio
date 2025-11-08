"""
Hero/Landing Section Component

The main landing section with typing animation and scroll indicator.
"""
from fasthtml.common import *

def HeroSection(animated_titles):
    """
    Creates the hero/landing section with typing animation.

    Args:
        animated_titles: List of titles to cycle through in typing animation
    """

    return Div(
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
                    cls="text-lg sm:text-xl md:text-3xl lg:text-4xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 bg-clip-text text-transparent"
                ),
                Span(
                    "|",
                    cls="text-lg sm:text-xl md:text-3xl lg:text-4xl text-purple-400 animate-blink ml-1"
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

        # Typing animation script
        Script(f"""
            const titles = {animated_titles};
            let titleIndex = 0;
            let charIndex = 0;
            let isDeleting = false;
            const typingSpeed = 100;
            const deletingSpeed = 50;
            const pauseTime = 2000;

            function typeTitle() {{
                const currentTitle = titles[titleIndex];
                const typingText = document.getElementById('typing-text');

                if (!typingText) return;

                if (isDeleting) {{
                    typingText.textContent = currentTitle.substring(0, charIndex - 1);
                    charIndex--;
                }} else {{
                    typingText.textContent = currentTitle.substring(0, charIndex + 1);
                    charIndex++;
                }}

                let timeout = isDeleting ? deletingSpeed : typingSpeed;

                if (!isDeleting && charIndex === currentTitle.length) {{
                    timeout = pauseTime;
                    isDeleting = true;
                }} else if (isDeleting && charIndex === 0) {{
                    isDeleting = false;
                    titleIndex = (titleIndex + 1) % titles.length;
                }}

                setTimeout(typeTitle, timeout);
            }}

            // Start typing animation when page loads
            document.addEventListener('DOMContentLoaded', typeTitle);
        """),

        id="home",
        cls="fixed inset-0 left-0 lg:left-64 flex items-center justify-center pt-20 sm:pt-20"
    )

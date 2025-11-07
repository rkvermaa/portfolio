"""
Modern Glassmorphism Sidebar Component

Creates a transparent, blurred sidebar with glass effect.
"""
from fasthtml.common import *

def ModernSidebar(name="Your Name", title="Your Title", subtitle="", email="your@email.com",
                  phone="+91 XXXXX XXXXX", location="India", age="25 Years", freelance="Available",
                  linkedin="#", github="#", twitter="#", instagram="#",
                  profile_image="static/images/profile.jpg", skills_major=None):
    """
    Creates a modern glassmorphism sidebar.

    Teaching moment:
    - Uses Tailwind CSS for glass effect (backdrop-blur)
    - Fixed position sidebar that overlays content
    - Smooth transitions and hover effects
    """

    if skills_major is None:
        skills_major = [
            {"name": "Python", "level": 90},
            {"name": "GenAI/LLM", "level": 85},
            {"name": "ML/AI", "level": 88},
        ]

    return Div(
        # Sidebar content
        Div(
            # Profile section
            Div(
                # Profile image - with status dot
                Div(
                    Div(
                        Div(
                            Img(
                                src=profile_image,
                                alt=name,
                                cls="w-full h-auto"
                            ),
                            cls="relative -top-2"
                        ),
                        cls="w-28 h-28 rounded-full border-2 border-blue-400/50 shadow-xl shadow-blue-500/50 overflow-hidden ring-1 ring-blue-400/30 ring-offset-1 ring-offset-transparent"
                    ),
                    # Green "Available" status dot
                    Div(
                        cls="absolute bottom-2 right-2 w-4 h-4 bg-green-500 rounded-full border-2 border-slate-400 status-dot"
                    ),
                    cls="relative w-28 h-28 mx-auto mb-4"
                ),
                # Name
                H2(name, cls="text-2xl font-bold text-white text-center mb-2"),
                # Title (smaller than name)
                P(title, cls="text-sm text-blue-200 text-center mb-1 px-2 font-medium"),
                # Subtitle (smaller than title)
                P(subtitle, cls="text-xs text-blue-300/80 text-center mb-4 px-2"),

                cls="mb-6"
            ),

            # Social media icons
            Div(
                A(I(data_lucide="linkedin", cls="w-4 h-4"), href=linkedin, target="_blank", cls="text-white/60 hover:text-blue-400 transition-colors"),
                A(I(data_lucide="github", cls="w-4 h-4"), href=github, target="_blank", cls="text-white/60 hover:text-blue-400 transition-colors"),
                A(I(data_lucide="facebook", cls="w-4 h-4"), href=twitter, target="_blank", cls="text-white/60 hover:text-blue-400 transition-colors"),
                A(I(data_lucide="instagram", cls="w-4 h-4"), href=instagram, target="_blank", cls="text-white/60 hover:text-blue-400 transition-colors"),
                cls="flex gap-5 justify-center mb-6"
            ),

            # Personal info details
            Div(
                # Email
                Div(
                    Span("Email:", cls="text-white/70 text-xs font-bold"),
                    A(email, href=f"mailto:{email}", cls="text-white/80 text-xs hover:text-blue-400 transition-colors"),
                    cls="flex justify-between mb-2 px-2"
                ),
                # Language
                Div(
                    Span("Language:", cls="text-white/70 text-xs font-bold"),
                    Span("Hindi, English", cls="text-white/80 text-xs"),
                    cls="flex justify-between mb-2 px-2"
                ),
                # Phone
                Div(
                    Span("Phone:", cls="text-white/70 text-xs font-bold"),
                    Span(phone, cls="text-white/80 text-xs"),
                    cls="flex justify-between mb-2 px-2"
                ),
                # Location
                Div(
                    Span("Location:", cls="text-white/70 text-xs font-bold"),
                    Span(location, cls="text-white/80 text-xs"),
                    cls="flex justify-between mb-2 px-2"
                ),
                # Age
                Div(
                    Span("Age:", cls="text-white/70 text-xs font-bold"),
                    Span(age, cls="text-white/80 text-xs"),
                    cls="flex justify-between mb-2 px-2"
                ),
                # Freelance status
                Div(
                    Span("Freelance:", cls="text-white/70 text-xs font-bold"),
                    Span(freelance, cls="text-green-400 text-xs font-medium"),
                    cls="flex justify-between mb-2 px-2"
                ),
                cls="mb-6 py-3 border-t border-b border-white/10"
            ),

            # Skills grouped by category
            Div(
                H3("Skills", cls="text-white text-xl font-semibold mb-3 text-center text-base"),

                # AI & GenAI Category
                Div(
                    Span("AI & GenAI", cls="text-blue-300 text-sm font-semibold mb-2 block"),
                    Div(
                        Span("Python", cls="category-chip"),
                        Span("LLM", cls="category-chip"),
                        Span("GenAI", cls="category-chip"),
                        Span("RAG", cls="category-chip"),
                        Span("Prompt Eng", cls="category-chip"),
                        Span("Multi-Agent", cls="category-chip"),
                        cls="flex flex-wrap gap-1.5"
                    ),
                    cls="mb-3"
                ),

                # ML & NLP Category
                Div(
                    Span("ML & NLP", cls="text-blue-300 text-sm font-semibold mb-2 block"),
                    Div(
                        Span("ML", cls="category-chip"),
                        Span("Deep Learning", cls="category-chip"),
                        Span("NLP", cls="category-chip"),
                        Span("Classification", cls="category-chip"),
                        Span("Clustering", cls="category-chip"),
                        Span("PyTorch", cls="category-chip"),
                        cls="flex flex-wrap gap-1.5"
                    ),
                    cls="mb-3"
                ),

                # Frameworks Category
                Div(
                    Span("Frameworks", cls="text-blue-300 text-sm font-semibold mb-2 block"),
                    Div(
                        Span("LangChain", cls="category-chip"),
                        Span("LangGraph", cls="category-chip"),
                        Span("FastAPI", cls="category-chip"),
                        Span("Pandas", cls="category-chip"),
                        Span("Scikit-learn", cls="category-chip"),
                        Span("TensorFlow", cls="category-chip"),
                        cls="flex flex-wrap gap-1.5"
                    ),
                    cls="mb-3"
                ),

                # Data & Databases Category
                Div(
                    Span("Data & DBs", cls="text-blue-300 text-sm font-semibold mb-2 block"),
                    Div(
                        Span("SQL", cls="category-chip"),
                        Span("PostgreSQL", cls="category-chip"),
                        Span("MongoDB", cls="category-chip"),
                        Span("Vector DBs", cls="category-chip"),
                        Span("PySpark", cls="category-chip"),
                        Span("Redis", cls="category-chip"),
                        cls="flex flex-wrap gap-1.5"
                    ),
                    cls="mb-3"
                ),

                # Cloud & DevOps Category
                Div(
                    Span("Cloud & DevOps", cls="text-blue-300 text-sm font-semibold mb-2 block"),
                    Div(
                        Span("AWS", cls="category-chip"),
                        Span("Docker", cls="category-chip"),
                        Span("Kubernetes", cls="category-chip"),
                        Span("CI/CD", cls="category-chip"),
                        Span("MLFlow", cls="category-chip"),
                        Span("Langsmith", cls="category-chip"),
                        cls="flex flex-wrap gap-1.5"
                    ),
                    cls="mb-3"
                ),

                cls="mb-6 px-2"
            ),

            # Download CV button - attractive glowy gradient pill
            A(
                "Download CV",
                href="static/cv.pdf",
                cls="block w-full py-3 px-6 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 hover:from-blue-600 hover:via-purple-600 hover:to-pink-600 text-white text-center rounded-full text-sm font-bold transition-all duration-300 hover:scale-105 shadow-lg hover:shadow-xl hover:shadow-purple-500/50"
            ),

            cls="p-6 pt-10"
        ),

        # Dark transparent overlay without blur
        cls="""
            fixed left-0 top-0 h-screen w-80 z-50
            bg-slate-900/30
            border-r border-white/20
            shadow-2xl
            overflow-y-auto
            scrollbar-thin scrollbar-thumb-white/30 scrollbar-track-transparent
            hidden lg:block
        """,
        # Note: Sidebar is hidden on mobile (< 1024px) to prevent overlap
    )


def SkillBarCompact(name, level):
    """Compact skill bar for sidebar"""
    return Div(
        Div(
            Span(name, cls="text-white text-xs font-medium"),
            Span(f"{level}%", cls="text-blue-300 text-xs"),
            cls="flex justify-between mb-1"
        ),
        Div(
            Div(
                style=f"width: {level}%",
                cls="h-1 bg-gradient-to-r from-blue-500 to-blue-400 rounded-full transition-all duration-500"
            ),
            cls="w-full bg-white/10 rounded-full h-1"
        ),
        cls="mb-3"
    )

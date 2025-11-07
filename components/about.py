"""
Modern About Me Section with Stats and Story
"""
from fasthtml.common import *

def AboutSection():
    """
    Creates a modern about section with two-column layout and education timeline.
    Features scroll animations and abstract geometric background.
    """

    # What I love doing - 6 cards
    passions = [
        {"icon": "cpu", "title": "Building Scalable AI Systems"},
        {"icon": "lightbulb", "title": "Solving Real-World Problems"},
        {"icon": "zap", "title": "Working with LLM Tech"},
        {"icon": "code", "title": "Crafting Clean Code"},
        {"icon": "coffee", "title": "Sleeping in my spare time"},
        {"icon": "rocket", "title": "Exploring New Technologies"},
    ]

    # Education timeline
    education = [
        {
            "degree": "Part Time PhD",
            "field": "Mechanical & Industrial Engineering",
            "institution": "IIT Roorkee, Uttarakhand",
            "year": "2025 - Cont."
        },
        {
            "degree": "M.Tech in Solid State Electronics Materials",
            "field": "Department of Physics",
            "institution": "IIT Roorkee, Uttarakhand",
            "year": "2016 - 2018"
        },
        {
            "degree": "B.Tech in Electronics & Communication",
            "field": "Electronics & Communication Technology",
            "institution": "UIET, CSJM University Kanpur",
            "year": "2005 - 2009"
        }
    ]

    return Section(
        # Full white background layer
        Div(cls="absolute inset-0 bg-white"),

        # Abstract geometric background shapes - now covers full section
        Div(
            # Large gradient circle - top left
            Div(cls="absolute -top-40 -left-40 w-[600px] h-[600px] bg-gradient-to-br from-blue-500/20 to-purple-500/20 rounded-full blur-3xl"),
            # Medium gradient circle - center right
            Div(cls="absolute top-1/2 -right-40 w-[500px] h-[500px] bg-gradient-to-br from-pink-500/20 to-blue-500/20 rounded-full blur-3xl"),
            # Small gradient circle - bottom left
            Div(cls="absolute -bottom-40 left-1/4 w-[400px] h-[400px] bg-gradient-to-br from-purple-500/20 to-pink-500/20 rounded-full blur-3xl"),
            cls="absolute inset-0 overflow-hidden pointer-events-none"
        ),

        # Content container
        Div(
            # Section heading
            Div(
                H2("Who am I?", cls="text-3xl md:text-4xl font-bold text-gray-800 mb-4 text-center"),
                Div(cls="w-20 h-1 bg-gradient-to-r from-blue-500 to-purple-500 mx-auto mb-12"),
                cls="mb-16 fade-in-scroll"
            ),

            # Hook line
            Div(
                H3(
                    "Full-Stack AI Engineer turning complex data into intelligent solutions",
                    cls="text-2xl md:text-3xl font-light text-gray-700 text-center max-w-4xl mx-auto leading-relaxed"
                ),
                cls="mb-16 fade-in-scroll"
            ),

            # Two column layout - About Me & Education
            Div(
                # Left column - About Me
                Div(
                    H3("About Me", cls="text-2xl font-bold text-gray-800 mb-6"),
                    P(
                        """I'm a Full-Stack AI Engineer specializing in building scalable data infrastructure
                        and intelligent ML systems. Currently at Passageway, I architect enterprise-scale
                        solutions that process terabytes of smart meter data, transforming raw information
                        into actionable insights.""",
                        cls="text-base text-gray-700 leading-relaxed mb-4"
                    ),
                    P(
                        """My passion lies in leveraging cutting-edge technologies—from LLMs and GenAI to
                        distributed data systems—to solve real-world challenges. I believe in the power of
                        AI to revolutionize how we interact with data, and I'm committed to building
                        solutions that are not just powerful, but also scalable and elegant.""",
                        cls="text-base text-gray-700 leading-relaxed mb-4"
                    ),
                    P(
                        """Whether it's designing data lakehouses, developing ML models for anomaly detection,
                        or implementing RAG systems with multi-agent workflows, I thrive on turning complex
                        problems into simple, intelligent solutions.""",
                        cls="text-base text-gray-700 leading-relaxed"
                    ),
                    cls="fade-in-scroll"
                ),

                # Right column - Education Timeline
                Div(
                    H3("Education", cls="text-2xl font-bold text-gray-800 mb-6"),
                    Div(
                        *[
                            Div(
                                # Timeline dot and line
                                Div(
                                    # Make the first (PhD) dot glow
                                    Div(cls=f"w-3 h-3 bg-blue-500 rounded-full {'status-dot' if i == 0 else ''}"),
                                    Div(cls="absolute top-3 left-1.5 w-0.5 h-full bg-blue-200") if i < len(education) - 1 else None,
                                    cls="relative"
                                ),
                                # Content
                                Div(
                                    Div(edu["year"], cls="text-sm text-blue-600 font-semibold mb-1"),
                                    H4(edu["degree"], cls="text-lg font-bold text-gray-800 mb-1"),
                                    P(edu["field"], cls="text-sm text-gray-700 mb-1"),
                                    P(edu["institution"], cls="text-sm text-gray-600"),
                                    cls="ml-6"
                                ),
                                cls="flex gap-4 mb-8 last:mb-0"
                            )
                            for i, edu in enumerate(education)
                        ],
                        cls="relative"
                    ),
                    cls="fade-in-scroll"
                ),

                cls="grid md:grid-cols-2 gap-12 mb-20 max-w-6xl mx-auto"
            ),

            # What I love doing - 6 pill-shaped cards in 3x2 grid
            Div(
                H3("What I Love Doing", cls="text-2xl font-bold text-gray-800 mb-8 text-center"),
                Div(
                    *[
                        Div(
                            I(data_lucide=passion["icon"], cls="w-5 h-5 text-gray-700 mr-2"),
                            Span(passion["title"], cls="text-sm font-medium text-gray-800"),
                            cls="glass-card px-5 py-3 rounded-full hover:shadow-lg hover:scale-105 transition-all duration-300 fade-in-scroll flex items-center justify-center gap-2"
                        )
                        for passion in passions
                    ],
                    cls="grid md:grid-cols-3 gap-4 max-w-5xl mx-auto"
                ),
                cls="mb-20"
            ),

            cls="container mx-auto px-8 md:px-16 relative z-10"
        ),

        id="about",
        cls="py-16 relative overflow-hidden"
    )

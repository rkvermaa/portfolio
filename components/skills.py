"""
Skills Section with Pill-Shaped Icons
"""
from fasthtml.common import *

def SkillsSection():
    """
    Creates a skills section with categorized pill-shaped icons.
    No floating animation, clean and organized.
    """

    # Organized skill categories with color themes
    skill_categories = [
        {
            "category": "AI & GenAI",
            "color": "blue-500",
            "skills": [
                {"name": "Python", "icon": "code-2"},
                {"name": "GenAI", "icon": "sparkles"},
                {"name": "LLMs", "icon": "bot"},
                {"name": "RAG", "icon": "search"},
                {"name": "Multi-Agent", "icon": "users"},
                {"name": "Prompt Eng", "icon": "message-circle"},
            ]
        },
        {
            "category": "ML & Deep Learning",
            "color": "purple-500",
            "skills": [
                {"name": "TensorFlow", "icon": "cpu"},
                {"name": "PyTorch", "icon": "flame"},
                {"name": "Scikit-learn", "icon": "chart-line"},
                {"name": "NLP", "icon": "message-square"},
                {"name": "Deep Learning", "icon": "network"},
                {"name": "Classification", "icon": "layers"},
            ]
        },
        {
            "category": "Frameworks & Libraries",
            "color": "pink-500",
            "skills": [
                {"name": "LangChain", "icon": "link"},
                {"name": "LangGraph", "icon": "git-branch"},
                {"name": "FastAPI", "icon": "zap"},
                {"name": "Django", "icon": "box"},
                {"name": "Pandas", "icon": "table"},
                {"name": "NumPy", "icon": "calculator"},
            ]
        },
        {
            "category": "Data & Databases",
            "color": "green-500",
            "skills": [
                {"name": "SQL", "icon": "database"},
                {"name": "PostgreSQL", "icon": "server"},
                {"name": "MongoDB", "icon": "layers"},
                {"name": "Redis", "icon": "circle"},
                {"name": "PySpark", "icon": "cloud"},
                {"name": "Vector DBs", "icon": "box"},
            ]
        },
        {
            "category": "Cloud & DevOps",
            "color": "indigo-500",
            "skills": [
                {"name": "AWS", "icon": "cloud"},
                {"name": "Docker", "icon": "package"},
                {"name": "Kubernetes", "icon": "container"},
                {"name": "CI/CD", "icon": "git-merge"},
                {"name": "MLFlow", "icon": "trending-up"},
                {"name": "Langsmith", "icon": "wrench"},
            ]
        },
        {
            "category": "Analytics & Visualization",
            "color": "orange-500",
            "skills": [
                {"name": "Tableau", "icon": "bar-chart-2"},
                {"name": "PowerBI", "icon": "pie-chart"},
                {"name": "Streamlit", "icon": "layout"},
                {"name": "Plotly", "icon": "area-chart"},
                {"name": "Seaborn", "icon": "chart-bar"},
                {"name": "Matplotlib", "icon": "line-chart"},
            ]
        },
    ]

    return Section(
        # Subtle gradient background
        Div(
            Div(cls="absolute -top-40 left-1/4 w-[600px] h-[600px] bg-gradient-to-br from-blue-500/10 to-purple-500/10 rounded-full blur-3xl"),
            Div(cls="absolute top-1/2 right-1/4 w-[600px] h-[600px] bg-gradient-to-br from-pink-500/10 to-blue-500/10 rounded-full blur-3xl"),
            cls="absolute inset-0 overflow-hidden pointer-events-none"
        ),

        # Content
        Div(
            # Section heading
            Div(
                H2("Skills & Technologies", cls="text-3xl md:text-4xl font-bold text-gray-800 mb-4 text-center"),
                P("My technical toolkit for building intelligent solutions", cls="text-lg text-gray-600 mb-6 text-center"),
                Div(cls="w-20 h-1 bg-gradient-to-r from-blue-500 to-purple-500 mx-auto mb-12"),
                cls="mb-16 fade-in-scroll"
            ),

            # Skill categories
            Div(
                *[
                    Div(
                        # Category header
                        Div(
                            H3(cat["category"], cls="text-lg font-semibold text-gray-800 mb-6"),
                            cls="fade-in-scroll"
                        ),
                        # Skills grid - pill shaped with colored icons
                        Div(
                            *[
                                Div(
                                    I(data_lucide=skill["icon"], cls=f"w-4 h-4 text-{cat['color']} mr-2"),
                                    Span(skill["name"], cls="text-sm text-gray-700"),
                                    cls="inline-flex items-center gap-2 px-5 py-2.5 bg-white/80 backdrop-blur-sm rounded-full border border-gray-200 hover:border-blue-400 hover:bg-blue-50 hover:scale-105 transition-all duration-300 fade-in-scroll"
                                )
                                for skill in cat["skills"]
                            ],
                            cls="flex flex-wrap gap-3 mb-12"
                        ),
                        cls="mb-8"
                    )
                    for cat in skill_categories
                ],
                cls="max-w-6xl mx-auto"
            ),

            cls="container mx-auto px-8 md:px-16 relative z-10"
        ),

        id="skills",
        cls="py-16 bg-white relative overflow-hidden"
    )

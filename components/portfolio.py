"""
Stunning Portfolio Section with Beautiful Image Cards
"""
from fasthtml.common import *

def PortfolioSection(projects_list):
    """
    Creates a stunning portfolio grid with large image cards.
    Features beautiful images with overlay on hover showing details.
    """

    return Section(
        # Full white background layer
        Div(cls="absolute inset-0 bg-white"),

        # Abstract geometric background shapes
        Div(
            # Large gradient circle - top left
            Div(cls="absolute -top-40 left-1/4 w-[600px] h-[600px] bg-gradient-to-br from-blue-500/10 to-purple-500/10 rounded-full blur-3xl"),
            # Medium gradient circle - center right
            Div(cls="absolute top-1/2 -right-40 w-[500px] h-[500px] bg-gradient-to-br from-pink-500/10 to-blue-500/10 rounded-full blur-3xl"),
            cls="absolute inset-0 overflow-hidden pointer-events-none"
        ),

        # Content container
        Div(
            # Section heading
            Div(
                H2("Portfolio", cls="text-3xl md:text-4xl font-bold text-gray-800 mb-4 text-center"),
                P("Showcasing my best work in AI, Data Engineering, and ML", cls="text-lg text-gray-600 mb-6 text-center"),
                Div(cls="w-20 h-1 bg-gradient-to-r from-blue-500 to-purple-500 mx-auto mb-16"),
                cls="mb-16 fade-in-scroll"
            ),

            # Projects grid - 3 columns on desktop, 2 on tablet, 1 on mobile
            Div(
                *[
                    # Project card with beautiful image
                    Div(
                        # Card container
                        Div(
                            # Background gradient image
                            Div(cls=f"absolute inset-0 bg-gradient-to-br {project.get('gradient', 'from-blue-400 to-purple-600')}"),

                            # Pattern overlay for texture
                            Div(cls="absolute inset-0 opacity-10", style="background-image: radial-gradient(circle, white 1px, transparent 1px); background-size: 20px 20px;"),

                            # Large icon in center
                            Div(
                                I(data_lucide=project.get('icon', 'code'), cls="w-24 h-24 text-white/80 drop-shadow-2xl"),
                                cls="absolute inset-0 flex items-center justify-center transition-transform duration-500 group-hover:scale-110 group-[.active]:scale-110"
                            ),

                            # Dark overlay on hover/click
                            Div(cls="absolute inset-0 bg-gradient-to-t from-black/90 via-black/50 to-transparent opacity-0 group-hover:opacity-100 group-[.active]:opacity-100 transition-all duration-500"),

                            # Content overlay (appears on hover/click)
                            Div(
                                # Title at top (always visible)
                                Div(
                                    H3(
                                        project["title"],
                                        cls="text-xl font-bold text-white mb-2 leading-tight drop-shadow-lg"
                                    ),
                                    cls="absolute top-6 left-6 right-6"
                                ),

                                # Bottom content (appears on hover/click)
                                Div(
                                    # Description
                                    P(
                                        project.get("description", "")[:100] + "...",
                                        cls="text-sm text-white/90 leading-relaxed mb-4"
                                    ),

                                    # Tech tags
                                    Div(
                                        *[
                                            Span(
                                                tech,
                                                cls="inline-block px-3 py-1 bg-white/20 backdrop-blur-sm text-white text-xs font-medium rounded-full border border-white/30"
                                            )
                                            for tech in project.get("tech", [])[:4]
                                        ],
                                        cls="flex flex-wrap gap-2"
                                    ),

                                    cls="absolute bottom-6 left-6 right-6 opacity-0 group-hover:opacity-100 group-[.active]:opacity-100 transform translate-y-4 group-hover:translate-y-0 group-[.active]:translate-y-0 transition-all duration-500"
                                ),

                                cls="absolute inset-0"
                            ),

                            cls="relative h-96 rounded-3xl overflow-hidden shadow-xl hover:shadow-2xl transition-all duration-500 group-hover:scale-[1.02] cursor-pointer",
                            onclick="this.parentElement.classList.toggle('active')"
                        ),

                        cls="group fade-in-scroll"
                    )
                    for project in projects_list
                ],
                cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto"
            ),

            cls="container mx-auto px-8 md:px-16 relative z-10"
        ),

        id="portfolio",
        cls="py-16 relative overflow-hidden"
    )

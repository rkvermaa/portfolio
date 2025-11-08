"""
Modern Experience Section with Timeline - Minimal Design
"""
from fasthtml.common import *

def ExperienceSection(experience_list):
    """
    Creates a clean, minimal experience section inspired by reference design.
    Simple timeline with role on left, company details on right.
    """

    return Section(
        # Full white background layer
        Div(cls="absolute inset-0 bg-white"),

        # Abstract geometric background shapes
        Div(
            # Large gradient circle - top right
            Div(cls="absolute -top-40 right-1/4 w-[600px] h-[600px] bg-gradient-to-br from-purple-500/20 to-blue-500/20 rounded-full blur-3xl"),
            # Medium gradient circle - center left
            Div(cls="absolute top-1/2 -left-40 w-[500px] h-[500px] bg-gradient-to-br from-blue-500/20 to-pink-500/20 rounded-full blur-3xl"),
            cls="absolute inset-0 overflow-hidden pointer-events-none"
        ),

        # Content container
        Div(
            # Section heading
            Div(
                H2("Experience", cls="text-3xl md:text-4xl font-bold text-gray-800 mb-16 fade-in-scroll"),
                cls="mb-20"
            ),

            # Timeline container with background line
            Div(
                *[
                    item
                    for i, exp in enumerate(experience_list)
                    for item in [
                        # Mobile layout - stacked vertically
                        Div(
                            # Timeline dot (mobile)
                            Div(
                                Div(cls="absolute top-3 left-1.5 w-0.5 h-full bg-blue-200") if i < len(experience_list) - 1 else None,
                                Div(cls=f"w-3 h-3 bg-blue-500 rounded-full {'status-dot' if i == 0 else ''} relative z-10"),
                                cls="relative flex-shrink-0 mr-4"
                            ),
                            # Content (mobile)
                            Div(
                                P(exp["date"], cls="text-xs text-blue-600 font-semibold mb-1"),
                                H3(exp["role"], cls="text-base font-bold text-gray-800 mb-1 leading-tight"),
                                Div(
                                    Span(exp["company"], cls="text-sm font-semibold text-gray-700"),
                                    Span(" • ", cls="text-gray-400 mx-1 text-sm"),
                                    Span(exp.get("location", ""), cls="text-xs text-gray-600"),
                                    cls="mb-2"
                                ),
                                P(exp["description"], cls="text-sm text-gray-700 leading-relaxed whitespace-pre-line"),
                                cls="flex-1 fade-in-scroll"
                            ),
                            cls="flex items-start mb-12 last:mb-0 lg:hidden"
                        ),

                        # Desktop layout - horizontal
                        Div(
                            # Left side - Date, Role, Company (1/3 width)
                            Div(
                                # Date
                                P(exp["date"], cls="text-sm text-blue-600 font-semibold mb-2"),
                                # Role
                                H3(exp["role"], cls="text-lg font-bold text-gray-800 mb-2 leading-tight"),
                                # Company and location
                                Div(
                                    Span(exp["company"], cls="text-base font-semibold text-gray-700"),
                                    Span(" • ", cls="text-gray-400 mx-1"),
                                    Span(exp.get("location", ""), cls="text-sm text-gray-600"),
                                ),
                                cls="flex-shrink-0 w-80 pr-8 text-left fade-in-scroll"
                            ),

                            # Timeline dot with connecting line container
                            Div(
                                # Connecting line background (only show if not last item)
                                Div(cls="absolute top-3 left-1.5 w-0.5 h-full bg-blue-200") if i < len(experience_list) - 1 else None,
                                # Glowing dot for current role (first one), normal blue for others
                                Div(cls=f"w-3 h-3 bg-blue-500 rounded-full {'status-dot' if i == 0 else ''} relative z-10"),
                                cls="relative flex-shrink-0 mr-8"
                            ),

                            # Right side - Description (2/3 width)
                            Div(
                                P(
                                    exp["description"],
                                    cls="text-base text-gray-700 leading-relaxed whitespace-pre-line"
                                ),
                                cls="flex-1 fade-in-scroll"
                            ),

                            cls="hidden lg:flex items-start mb-16 last:mb-0"
                        )
                    ]
                ],
                cls="max-w-6xl mx-auto relative"
            ),

            cls="container mx-auto px-8 md:px-16 relative z-10"
        ),

        id="experience",
        cls="py-16 relative overflow-hidden"
    )

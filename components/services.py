"""
Modern Services Section with Beautiful Cards
"""
from fasthtml.common import *

def ServicesSection(services_list):
    """
    Creates a modern services section with icon cards.
    Features hover effects and clean design.
    """

    return Section(
        # Full white background layer
        Div(cls="absolute inset-0 bg-gray-50"),

        # Abstract geometric background shapes
        Div(
            # Large gradient circle - top right
            Div(cls="absolute -top-40 right-1/4 w-[600px] h-[600px] bg-gradient-to-br from-purple-500/10 to-blue-500/10 rounded-full blur-3xl"),
            # Medium gradient circle - center left
            Div(cls="absolute top-1/2 -left-40 w-[500px] h-[500px] bg-gradient-to-br from-blue-500/10 to-pink-500/10 rounded-full blur-3xl"),
            cls="absolute inset-0 overflow-hidden pointer-events-none"
        ),

        # Content container
        Div(
            # Section heading
            Div(
                H2("What I Do", cls="text-3xl md:text-4xl font-bold text-gray-800 mb-4 text-center"),
                P("Specialized services in AI, Data Engineering, and Machine Learning", cls="text-lg text-gray-600 mb-6 text-center"),
                Div(cls="w-20 h-1 bg-gradient-to-r from-purple-500 to-blue-500 mx-auto mb-16"),
                cls="mb-16 fade-in-scroll"
            ),

            # Services grid - 3 columns on desktop
            Div(
                *[
                    # Service card with light gradient background
                    Div(
                        # Card container with gradient matching portfolio style
                        Div(
                            # Light gradient background
                            Div(cls=f"absolute inset-0 bg-gradient-to-br from-blue-50 to-purple-50 group-hover:from-blue-100 group-hover:to-purple-100 transition-all duration-500"),

                            # Content
                            Div(
                                # Minimal outline icon
                                Div(
                                    I(data_lucide=service.get("lucide_icon", "sparkles"), cls="w-12 h-12 text-blue-600 group-hover:text-purple-600 transition-colors duration-500"),
                                    cls="w-20 h-20 border-2 border-blue-200 rounded-2xl flex items-center justify-center mb-6 group-hover:border-purple-300 group-hover:scale-110 transition-all duration-500"
                                ),

                                # Title
                                H3(
                                    service["title"],
                                    cls="text-xl font-bold text-gray-800 mb-4"
                                ),

                                # Service items as simple text
                                Div(
                                    *[
                                        P(item, cls="text-sm text-gray-600 mb-2 last:mb-0")
                                        for item in service["items"]
                                    ],
                                    cls="space-y-1"
                                ),

                                cls="relative z-10"
                            ),

                            cls="relative h-full p-8 rounded-2xl shadow-md hover:shadow-xl transition-all duration-500 group-hover:-translate-y-1 overflow-hidden"
                        ),

                        cls="group fade-in-scroll h-full"
                    )
                    for service in services_list
                ],
                cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto"
            ),

            cls="container mx-auto px-8 md:px-16 relative z-10"
        ),

        id="services",
        cls="py-16 relative overflow-hidden"
    )

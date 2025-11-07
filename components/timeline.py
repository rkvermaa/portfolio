"""
Timeline Components for Education and Experience

This creates timeline layouts for displaying chronological information.
"""
from fasthtml.common import *

def EducationSection(education_list):
    """
    Creates an education section with timeline layout.

    Teaching moment:
    - We're using similar patterns as ServicesSection
    - Timeline uses CSS for the visual line connecting items
    - Each item has a date badge and description

    Args:
        education_list: List of dicts with keys: institution, degree, date, description
    """
    return Div(
        H2("Education", cls="section-title"),
        P("Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit.",
          cls="section-subtitle"),

        Div(
            *[TimelineItem(item) for item in education_list],
            cls="timeline"
        ),
        cls="section",
        id="education"
    )


def ExperienceSection(experience_list):
    """
    Creates an experience section with timeline layout.

    Args:
        experience_list: List of dicts with keys: company, role, date, description, achievements
    """
    return Div(
        H2("Experience", cls="section-title"),
        P("My professional journey in building scalable data solutions and ML systems.",
          cls="section-subtitle"),

        Div(
            *[ExperienceItem(item) for item in experience_list],
            cls="timeline"
        ),
        cls="section",
        id="experience"
    )


def TimelineItem(item):
    """
    A single timeline item for education.

    Teaching moment:
    - We use Span for inline elements like date badges
    - The timeline dot and line are created with CSS
    """
    return Div(
        Div(cls="timeline-dot"),
        Div(
            H3(item["institution"]),
            Span(item["date"], cls="timeline-date"),
            H4(item["degree"], style="margin: 10px 0; color: var(--text-dark); font-size: 1rem;"),
            P(item["description"], cls="timeline-text"),
            cls="timeline-content"
        ),
        cls="timeline-item"
    )


def ExperienceItem(item):
    """
    A single timeline item for work experience.

    Teaching moment:
    - This is similar to TimelineItem but with more detailed content
    - We can have nested lists for achievements
    - Notice how we check if 'achievements' exists before rendering it
    """
    return Div(
        Div(cls="timeline-dot"),
        Div(
            H3(item["company"]),
            Span(item["date"], cls="timeline-date"),
            H4(item["role"], style="margin: 10px 0; color: var(--text-dark); font-size: 1rem;"),
            P(item["description"], cls="timeline-text"),

            # If there are achievements, render them as a list
            (Div(
                H4("Key Achievements:", style="margin-top: 15px; font-size: 0.95rem;"),
                Ul(
                    *[Li(achievement, style="margin: 8px 0; color: var(--text-light);")
                      for achievement in item.get("achievements", [])],
                    style="padding-left: 20px;"
                ),
            ) if item.get("achievements") else None),

            # Tech stack badge
            (Div(
                Strong("Tech Stack: ", style="color: var(--text-dark);"),
                Span(item["tech_stack"], style="color: var(--text-light); font-size: 0.9rem;"),
                style="margin-top: 15px;"
            ) if item.get("tech_stack") else None),

            cls="timeline-content"
        ),
        cls="timeline-item"
    )

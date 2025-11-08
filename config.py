"""
Configuration file for portfolio data

Teaching moment:
- This is a good practice to separate data from code
- You can easily update your portfolio information here
- In a production app, this might come from a database or CMS
"""

# Personal Information
PERSONAL_INFO = {
    "name": "Ravi Kumar Verma",
    "title": "Full-Stack AI Engineer",
    "subtitle": "LLM • GenAI • ML",
    "email": "rkverma87@gmail.com",  # Update with your real email
    "phone": "+91 7409210692",  # Update with your real phone
    "location": "India",
    "birth_year": 1987,  # Your birth year (age will be auto-calculated)
    "age": "37 years",  # This will be auto-calculated from birth_year
    "freelance": "Available",
    "linkedin": "https://www.linkedin.com/in/ravi-kumar-verma-16837734/",  # Update with your LinkedIn
    "github": "https://github.com/rkvermaa",  # Update with your GitHub
    "profile_image": "static/images/notion-avatar-1762452759393.png",  # Your Notion avatar
    # Typing animation titles (shown on hero section)
    "animated_titles": [
        "Ravi Kumar Verma",  # Will be auto-filled with name
        "Full-Stack AI Engineer",  # Will be auto-filled with title
        "GenAI Solutions Architect",
        "LLM Specialist",
        "AI/ML Solutions Builder"
    ],
}

# Skills for sidebar
SKILLS = {
    "major": [
        {"name": "Python", "level": 90},
        {"name": "SQL/Database", "level": 85},
        {"name": "Data Engineering", "level": 88},
        {"name": "Machine Learning", "level": 82},
        {"name": "Cloud (AWS)", "level": 75},
    ],
    "extra": [
        "PySpark", "Polars", "DuckDB", "Docker", "Prefect",
        "ClickHouse", "PostgreSQL", "MinIO", "Dremio", "Git"
    ]
}

# Hero section text
HERO = {
    "headline": "Building Scalable Data Solutions & ML Systems",
    "description": "Data Engineer & ML Engineer specializing in data lakehouse architecture, ETL/ELT pipelines, and machine learning for enterprise-scale applications. Currently working at Passageway Pvt Ltd on smart meter analytics.",
}

# Services/Skills you offer
SERVICES = [
    {
        "title": "GenAI & Multi-Agent Systems",
        "icon": "✨",
        "lucide_icon": "sparkles",
        "items": [
            "LLM Integration & Fine-tuning",
            "Multi-Agent Workflows",
            "RAG Systems & Vector DBs",
            "Prompt Engineering"
        ]
    },
    {
        "title": "Data Engineering",
        "icon": "🗄️",
        "lucide_icon": "database",
        "items": [
            "Data Lakehouse Architecture",
            "ETL/ELT Pipeline Development",
            "Distributed Systems"
        ]
    },
    {
        "title": "Machine Learning",
        "icon": "🤖",
        "lucide_icon": "cpu",
        "items": [
            "Anomaly Detection",
            "Time Series Forecasting",
            "Unsupervised Learning"
        ]
    },
    {
        "title": "Data Analytics",
        "icon": "📊",
        "lucide_icon": "bar-chart-2",
        "items": [
            "Business Intelligence",
            "Dashboard Development",
            "Performance Optimization"
        ]
    },
    {
        "title": "Cloud & DevOps",
        "icon": "☁️",
        "lucide_icon": "cloud",
        "items": [
            "AWS Infrastructure",
            "Docker Containerization",
            "CI/CD Pipelines"
        ]
    },
    {
        "title": "Backend Development",
        "icon": "⚙️",
        "lucide_icon": "code",
        "items": [
            "Python/FastAPI",
            "Database Design",
            "API Development"
        ]
    }
]

# Education history
EDUCATION = [
    {
        "institution": "Your University Name",
        "degree": "Bachelor of Technology in Computer Science",
        "date": "2018 - 2022",
        "description": "Focused on data structures, algorithms, machine learning, and distributed systems."
    },
    # Add more education entries here
]

# Work experience
EXPERIENCE = [
    {
        "company": "Passageway",
        "location": "Jaipur, India",
        "role": "Lead Data Scientist",
        "date": "August 2024 - Present",
        "description": "As a Lead Data Scientist, I architect and deploy enterprise-scale data infrastructure and intelligent ML systems. Currently building scalable solutions for UPCL smart meter analytics, processing terabytes of data from 600,000+ meters.\n\nKey project: Redesigned data architecture from failing PostgreSQL to scalable lakehouse using MinIO, Dremio, and ClickHouse, with ML models for energy forecasting and tampering detection."
    },
    {
        "company": "Xaigi Technology",
        "location": "Noida, India",
        "role": "Data Scientist | Gen AI Solution Architect",
        "date": "January 2024 - August 2024",
        "description": "As a Project Lead and Generative AI Architect, I led the development of AI-driven solutions and designed intelligent agent-based systems. My focus was on building scalable architectures using LLMs and multi-agent frameworks to automate financial workflows.\n\nKey project: Built a multi-agent conversational AI system integrated with QuickBooks, WooCommerce, and Shopify, achieving 90% automation of financial queries."
    },
    {
        "company": "Ericsson",
        "location": "Noida, India",
        "role": "Data Scientist",
        "date": "December 2021 - December 2023",
        "description": "As a Data Scientist, I developed scalable machine learning and NLP solutions to enhance telecom operations and customer experience. I focused on processing large-scale data, deploying models in production, and driving insights through automated analytics pipelines.\n\nKey project: Built a PySpark-based batch ETL pipeline on GCP to process ~1M rows every 15 minutes using Argo Workflows for real-time telecom data analytics."
    },
    {
        "company": "ATCS (Nagarro)",
        "location": "Jaipur, India",
        "role": "Data Scientist",
        "date": "July 2018 - November 2021",
        "description": "As a Data Scientist, I built predictive models and intelligent systems to improve service operations, optimize maintenance workflows, and support data-driven business decisions. I also mentored junior team members and collaborated with stakeholders to align analytics with strategic goals.\n\nKey project: Developed a predictive maintenance solution using telematics data, resulting in a 500% increase in service call volume and 2× boost in conversions."
    },
    {
        "company": "Bharat Sanchar Nigam Limited",
        "location": "Gujarat, India",
        "role": "Junior Telecom Officer (JTO)",
        "date": "May 2010 - June 2016",
        "description": "As a JTO, I was responsible for managing telecom operations, maintaining infrastructure, and ensuring uninterrupted network services across rural and urban regions. I also oversaw ERP-driven inventory operations and led customer service excellence initiatives.\n\nKey achievement: Managed 12 rural and 1 urban telephone exchanges, ensuring continuous telecommunication services across the district."
    }
]

# Projects/Portfolio
PROJECTS = [
    {
        "title": "Conversational AI for Finance | Multi-Agent Flow",
        "description": "Designed and led development of a multi-agent conversational AI system integrated with QuickBooks, WooCommerce, Shopify, and Authorize.net. Built 50+ LangChain tools enabling 90% automation of financial queries, achieving 400% tool coverage expansion and 94% accuracy.",
        "icon": "bot",
        "gradient": "from-blue-500 to-purple-600",
        "tech": ["Python", "LangChain", "LangGraph", "GPT-4", "LlamaParser", "SQLAgent", "Vector DBs", "FastAPI"],
        "link": "#",
        "category": "GenAI"
    },
    {
        "title": "AI-Driven Merchant Onboarding Platform",
        "description": "Led development of a Generative AI-powered onboarding system to streamline merchant registration across multiple payment processors. Reduced form-filling time from several minutes to just a few seconds via intelligent autofill and adaptive question flows.",
        "icon": "sparkles",
        "gradient": "from-purple-500 to-pink-600",
        "tech": ["Python", "LangChain", "FastAPI", "LlamaParser", "Pydantic", "GenAI"],
        "link": "#",
        "category": "GenAI"
    },
    {
        "title": "UPCL Smart Meter Analytics Platform",
        "description": "Enterprise data lakehouse for 600k+ smart meters, processing 8GB daily. Redesigned data architecture from failing PostgreSQL to scalable lakehouse using MinIO, Dremio, and ClickHouse, with ML models for energy forecasting and tampering detection.",
        "icon": "database",
        "gradient": "from-green-500 to-blue-600",
        "tech": ["Python", "ClickHouse", "MinIO", "Dremio", "Prefect", "PySpark", "ML"],
        "link": "#",
        "category": "Data Engineering"
    },
    {
        "title": "NPS-Based Topic Classification for Telecom",
        "description": "Led development of a topic classification system using customer NPS feedback to enhance service experience. Applied LDA to identify key themes and developed sentiment analysis pipeline, delivering actionable insights through Tableau dashboard.",
        "icon": "chart-bar",
        "gradient": "from-orange-500 to-red-600",
        "tech": ["PySpark", "Python", "Argo-flow", "LDA", "Tableau", "NLP"],
        "link": "#",
        "category": "ML & Analytics"
    },
    {
        "title": "Predictive Service Reminder System for VECV",
        "description": "Built predictive model using historical telematics data to forecast scheduled service intervals, improving task management. Automated calling list generation and service categorization, resulting in 500% increase in service call volume and 2× conversion rate improvement.",
        "icon": "trending-up",
        "gradient": "from-cyan-500 to-blue-600",
        "tech": ["Python", "Z-score", "Docker", "Kubernetes", "ML"],
        "link": "#",
        "category": "ML & Predictive Analytics"
    },
    {
        "title": "Repair Package Recommendation System for Daimler",
        "description": "Developed ML-driven recommendation engine to standardize vehicle repair quality and streamline claims processing. Leveraged historical claim data to suggest optimal repair packages, reducing false claim submissions and accelerating claim clearance.",
        "icon": "wrench",
        "gradient": "from-indigo-500 to-purple-600",
        "tech": ["Python", "NLP", "Machine Learning"],
        "link": "#",
        "category": "ML & NLP"
    }
]

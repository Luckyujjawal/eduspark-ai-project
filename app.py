import streamlit as st
import time
import random

st.set_page_config(
    page_title="EduSpark | AI Project Blueprint Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# High-Contrast CSS Styling (Selectbox Dropdown Fix Included)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Main Background */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #0d1117 !important;
        color: #ffffff !important;
    }

    h1, h2, h3, h4, h5, h6, p, span, label, strong {
        color: #ffffff !important;
    }

    .glowing-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #94a3b8 !important;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    /* Form Container */
    div[data-testid="stForm"] {
        background-color: #161b22 !important;
        border: 2px solid #30363d !important;
        border-radius: 12px;
        padding: 25px;
    }

    /* Inputs & Selectbox Closed State */
    .stTextInput input, 
    div[data-baseweb="select"] > div {
        background-color: #21262d !important;
        color: #ffffff !important;
        border: 1px solid #484f58 !important;
        border-radius: 6px !important;
    }

    div[data-baseweb="select"] * {
        color: #ffffff !important;
    }

    /* DROPDOWN MENU OPEN LIST FIX (Options Visibility) */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    ul[role="listbox"] {
        background-color: #1e293b !important;
        border: 1px solid #475569 !important;
        border-radius: 8px !important;
    }

    li[role="option"],
    div[role="option"] {
        background-color: #1e293b !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        padding: 10px 14px !important;
        cursor: pointer !important;
    }

    li[role="option"]:hover,
    div[role="option"]:hover,
    li[aria-selected="true"],
    div[aria-selected="true"] {
        background-color: #2563eb !important;
        color: #ffffff !important;
    }

    /* Submit Button */
    div[data-testid="stForm"] button[kind="primaryFormSubmit"],
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%) !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 1.2rem !important;
        border: 2px solid #a855f7 !important;
        padding: 14px 28px !important;
        border-radius: 10px !important;
        box-shadow: 0 0 15px rgba(168, 85, 247, 0.6) !important;
        width: 100% !important;
    }

    /* Expander Cards */
    div[data-testid="stExpander"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }

    div[data-testid="stExpander"] * {
        color: #f0f6fc !important;
    }

    code {
        background-color: #21262d !important;
        color: #38bdf8 !important;
        border: 1px solid #30363d !important;
        padding: 3px 6px !important;
        border-radius: 4px !important;
        font-weight: 600 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #010409 !important;
        border-right: 1px solid #30363d;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
st.markdown("<div class='glowing-title'>EduSpark AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Next-Gen Project Blueprint and Learning Roadmap Generator</div>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Control Panel")
    st.markdown("---")
    st.markdown("**System Architecture:**")
    st.markdown("- Built-in Blueprint Engine")
    st.markdown("- Zero API Dependency")
    st.markdown("- Multi-Domain Generator")
    st.markdown("---")
    st.caption("Designed for Academic Presentations")

# -----------------------------------------------------------------------------
# Form Section
# -----------------------------------------------------------------------------
with st.form("project_input_form"):
    st.markdown("<h3 style='color: #ffffff !important; margin-bottom: 20px;'>Student Profile Settings</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        subject = st.text_input("Subject / Domain", placeholder="e.g. Python, AI, Web Dev, Java")
    with col2:
        skill_level = st.selectbox("Current Skill Level", ["Beginner", "Intermediate", "Advanced"])
    with col3:
        interests = st.text_input("Interests / Specialization", placeholder="e.g. Healthcare, Finance, Gaming, E-commerce")

    num_ideas = st.slider("Number of Blueprints to Generate", min_value=1, max_value=3, value=2)

    st.markdown("<br>", unsafe_allow_html=True)
    submit_btn = st.form_submit_button("Generate Industry Blueprints", type="primary")

# -----------------------------------------------------------------------------
# Dynamic Blueprint Generator Function
# -----------------------------------------------------------------------------
def generate_dynamic_blueprints(sub, lvl, interest, count):
    topic = interest.strip().title() if interest.strip() else "Modern Systems"
    domain = sub.strip().title() if sub.strip() else "Core Development"

    templates = [
        {
            "title": f"Smart {topic} Analytics and Automation Suite",
            "summary": f"An enterprise-ready {domain} platform that leverages data analytics to monitor, optimize, and streamline workflows in {topic}.",
            "key_features": [
                f"Real-time {topic} data ingestion and filtering engine",
                "Automated anomaly detection and trigger notifications",
                "Interactive visual dashboard with actionable metrics"
            ],
            "tech_stack": [f"{domain}", "Streamlit", "Pandas", "Plotly", "SQLite"],
            "roadmap": [
                f"Phase 1: Architecture design and data pipeline setup for {topic}",
                "Phase 2: Core algorithm implementation and validation tests",
                "Phase 3: Dashboard UI integration, packaging, and cloud deployment"
            ]
        },
        {
            "title": f"Autonomous {topic} Management and Recommendation Hub",
            "summary": f"A comprehensive {domain}-based system tailored for {lvl} developers to deliver predictive insights and personalized recommendations in {topic}.",
            "key_features": [
                f"Rule-based recommendation algorithms for {topic}",
                "Secure multi-user authentication and profile management",
                "REST API integration for external data synchronization"
            ],
            "tech_stack": [f"{domain}", "FastAPI", "SQLAlchemy", "Docker"],
            "roadmap": [
                "Phase 1: Database schema modeling and authentication setup",
                f"Phase 2: Building recommendation logic for {topic}",
                "Phase 3: Performance testing, CI/CD pipeline, and documentation"
            ]
        },
        {
            "title": f"Next-Gen {topic} Interactive Simulator and Testing Engine",
            "summary": f"A highly extensible {domain} tool designed to simulate real-world {topic} environments with logging, performance tracking, and diagnostics.",
            "key_features": [
                f"Dynamic parameter configuration for {topic} scenarios",
                "Comprehensive stress testing and telemetry logging",
                "Automated report generation with performance benchmarks"
            ],
            "tech_stack": [f"{domain}", "PyTest", "NumPy", "Matplotlib", "GitHub Actions"],
            "roadmap": [
                f"Phase 1: Simulation module structure and mathematical logic",
                "Phase 2: Telemetry tracking and report generation engine",
                "Phase 3: Final optimization, edge-case testing, and live release"
            ]
        }
    ]

    return templates[:count]

# -----------------------------------------------------------------------------
# Execution
# -----------------------------------------------------------------------------
if submit_btn:
    if not subject:
        st.warning("Please fill the Subject / Domain field.")
    else:
        with st.spinner("Crafting your project blueprints..."):
            time.sleep(1.0)
            blueprints = generate_dynamic_blueprints(subject, skill_level, interests, num_ideas)

            st.success("Project Blueprints Generated Successfully!")

            for idx, proj in enumerate(blueprints, 1):
                with st.expander(f"Blueprint #{idx}: {proj['title']}", expanded=True):
                    st.markdown(f"**Difficulty Level:** `{skill_level}`")
                    st.markdown(f"**Overview:** {proj['summary']}")
                    st.markdown("---")

                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown("##### Key Features")
                        for feat in proj["key_features"]:
                            st.write(f"- {feat}")

                    with c2:
                        st.markdown("##### Tech Stack")
                        tech_badges = " ".join([f"`{t}`" for t in proj["tech_stack"]])
                        st.write(tech_badges)

                    st.markdown("---")
                    st.markdown("##### Execution Roadmap")
                    for step_num, step in enumerate(proj["roadmap"], 1):
                        st.write(f"**Step {step_num}:** {step}")

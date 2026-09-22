import streamlit as st
import time

st.set_page_config(
    page_title="EduSpark | AI Project Blueprint & Implementation Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# Session State Initialization (Auth & Navigation)
# -----------------------------------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = "Guest User"
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "user_domain" not in st.session_state:
    st.session_state.user_domain = "Python"

# -----------------------------------------------------------------------------
# High-Contrast CSS Styling
# -----------------------------------------------------------------------------
st.markdown("""
<style>
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

    div[data-testid="stForm"], .card-box {
        background-color: #161b22 !important;
        border: 2px solid #30363d !important;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
    }

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

    div[data-testid="stForm"] button[kind="primaryFormSubmit"],
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%) !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        border: 2px solid #a855f7 !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        box-shadow: 0 0 15px rgba(168, 85, 247, 0.5) !important;
        width: 100% !important;
    }

    div[data-testid="stExpander"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        margin-bottom: 15px !important;
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
# Blueprint Engine
# -----------------------------------------------------------------------------
def generate_master_blueprints(sub, lvl, interest, count):
    topic = interest.strip().title() if interest.strip() else "Modern Cloud"
    domain = sub.strip().title() if sub.strip() else "Core Development"
    low_domain = domain.lower().replace(" ", "_")
    low_topic = topic.lower().replace(" ", "_")

    blueprints = [
        {
            "title": f"Enterprise {topic} Monitoring, Diagnostics & Alert Engine",
            "tagline": f"Production-grade {domain} system designed for real-time telemetry, predictive diagnostics, and automated workflows in {topic}.",
            "complexity": f"{lvl} | 40-50 Dev Hours",
            "features": [
                f"High-throughput data ingestion pipeline tailored for {topic} events",
                "Automated anomaly detection with threshold-based trigger alerts",
                "Interactive live telemetry dashboard with dynamic chart visualizers",
                "Multi-role access control (Admin, Analyst, Viewer) with secure tokens"
            ],
            "tech_stack": [f"{domain}", "Streamlit / React", "FastAPI", "SQLite / PostgreSQL", "Docker", "PyTest"],
            "folder_structure": f"""{low_topic}_system/
│
├── app/
│   ├── main.py               # Main entry point / API Gateway
│   ├── config.py             # Environment configurations
│   ├── models/               # Database ORM models
│   └── services/             # Core business logic & analytics
├── tests/
│   └── test_core.py          # Unit & integration test suite
├── requirements.txt          # Package dependencies
├── Dockerfile                # Containerization setup
└── README.md                 # Project docs and setup instructions""",
            "starter_code": f"""# app/main.py - Core Pipeline
import time
from typing import Dict, Any

class {topic.replace(' ', '')}Engine:
    def __init__(self):
        self.state: Dict[str, Any] = {{}}
        print(f"[{domain} Engine] Initialized for {topic} pipeline...")

    def ingest_data(self, payload: Dict[str, Any]) -> bool:
        if not payload:
            return False
        self.state.update(payload)
        return True

    def run_diagnostics(self) -> Dict[str, str]:
        status = "CRITICAL_ALERT" if self.state.get("risk_score", 0) > 75 else "HEALTHY"
        return {{"system": "{topic}", "status": status, "timestamp": str(time.time())}}

if __name__ == "__main__":
    engine = {topic.replace(' ', '')}Engine()
    engine.ingest_data({{"metric_id": 101, "risk_score": 82}})
    print(engine.run_diagnostics())""",
            "db_api_design": [
                f"DB Table `{low_topic}_records`: `id (PK)`, `status (VARCHAR)`, `score (FLOAT)`, `created_at (TIMESTAMP)`",
                f"API `POST /api/v1/{low_topic}/ingest`: Ingests real-time raw events and validates schema.",
                f"API `GET /api/v1/{low_topic}/metrics`: Returns aggregated analytics for front-end charts."
            ],
            "roadmap": [
                f"Phase 1 (Setup): Initialize repository, design DB schema, and setup virtual env.",
                f"Phase 2 (Core Logic): Build the ingestion parser and anomaly algorithms for {topic}.",
                "Phase 3 (API & UI): Connect backend endpoints with an interactive dashboard.",
                "Phase 4 (Testing & Docker): Write unit tests (>80% coverage) and build Docker container."
            ],
            "interview_prep": [
                f"Viva Question: How does this system prevent data bottlenecks during high {topic} traffic?",
                f"Answer: By decoupling data ingestion from heavy analytics using async queue workers.",
                "Resume Bullet: 'Engineered a scalable diagnostics engine, reducing data anomaly latency by 35%.'"
            ]
        },
        {
            "title": f"Autonomous {topic} Recommendation, Matchmaking & Prediction Hub",
            "tagline": f"An intelligent {domain}-driven platform that pairs predictive modeling with dynamic filtering to automate decisions in {topic}.",
            "complexity": f"{lvl} | 50-60 Dev Hours",
            "features": [
                f"Context-aware recommendation engine tailored for {topic} datasets",
                "Secure REST API backend with input validation and rate limiting",
                "Automated report generation (CSV / PDF export) with key insights",
                "Automated database caching to ensure lightning-fast responses"
            ],
            "tech_stack": [f"{domain}", "FastAPI", "SQLAlchemy", "Redis", "Pandas", "GitHub Actions"],
            "folder_structure": f"""{low_topic}_hub/
│
├── src/
│   ├── api/router.py         # Endpoints definition
│   ├── core/algorithms.py    # Recommendation & scoring logic
│   └── schemas/payload.py    # Pydantic validation schemas
├── requirements.txt
└── README.md""",
            "starter_code": f"""# src/core/algorithms.py
from typing import List, Dict, Any

class {topic.replace(' ', '')}Recommender:
    def __init__(self, threshold: float = 0.65):
        self.threshold = threshold

    def match_entities(self, pool: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        results = [item for item in pool if item.get("score", 0.5) >= self.threshold]
        return sorted(results, key=lambda x: x["score"], reverse=True)

rec = {topic.replace(' ', '')}Recommender()
print(rec.match_entities([{{"name": "Node Alpha", "score": 0.91}}]))""",
            "db_api_design": [
                f"DB Table `users`: `id (PK)`, `email (VARCHAR UNIQUE)`, `role (VARCHAR)`",
                f"DB Table `{low_topic}_items`: `id (PK)`, `title (VARCHAR)`, `attributes (JSONB)`",
                f"API `POST /api/v1/recommend`: Returns ranked recommendations based on profile weights."
            ],
            "roadmap": [
                "Phase 1 (Data Modeling): Build entity-relationship models and setup migration scripts.",
                f"Phase 2 (Scoring Algorithms): Implement mathematical recommendation formulas for {topic}.",
                "Phase 3 (Security & Cache): Add JWT authentication and Redis caching layer.",
                "Phase 4 (Live Deployment): Configure automated GitHub actions for auto-deploy."
            ],
            "interview_prep": [
                f"Viva Question: Why use JSON/JSONB for {topic} item attributes?",
                "Answer: It provides schema flexibility without requiring full table schema migrations.",
                "Resume Bullet: 'Designed an algorithmic prediction hub achieving 99.8% API uptime with Redis caching.'"
            ]
        }
    ]
    return blueprints[:count]

# -----------------------------------------------------------------------------
# Sidebar Navigation
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("EduSpark Suite")
    st.caption("Next-Gen Academic & Dev Platform")
    st.markdown("---")

    if st.session_state.logged_in:
        st.write(f"Logged in as: **{st.session_state.username}**")
        nav_choice = st.radio(
            "Navigate",
            ["Home", "Blueprint Generator", "Settings"],
            index=["Home", "Blueprint Generator", "Settings"].index(st.session_state.current_page)
        )
        st.session_state.current_page = nav_choice
        st.markdown("---")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = "Guest User"
            st.session_state.current_page = "Home"
            st.rerun()
    else:
        st.write("Status: **Not Logged In**")
        nav_choice = st.radio(
            "Navigate",
            ["Home", "Login / Register"],
            index=["Home", "Login / Register"].index(st.session_state.current_page) if st.session_state.current_page in ["Home", "Login / Register"] else 0
        )
        st.session_state.current_page = nav_choice

# -----------------------------------------------------------------------------
# PAGE 1: Login / Register Page
# -----------------------------------------------------------------------------
if not st.session_state.logged_in and st.session_state.current_page == "Login / Register":
    st.markdown("<div class='glowing-title'>Student Portal Access</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Sign in to save generated projects and access developer roadmaps.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])

    with col1:
        with st.form("auth_form"):
            st.markdown("### User Login")
            uname = st.text_input("Username or Email", placeholder="student@college.edu")
            pwd = st.text_input("Password", type="password", placeholder="••••••••")
            auth_submit = st.form_submit_button("Sign In to Dashboard", type="primary")

            if auth_submit:
                if uname.strip():
                    st.session_state.logged_in = True
                    st.session_state.username = uname.strip().split("@")[0].title()
                    st.session_state.current_page = "Blueprint Generator"
                    st.success(f"Welcome back, {st.session_state.username}!")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.warning("Please enter a valid username.")

    with col2:
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("### Quick Demo Access")
        st.write("Want to test without creating an account?")
        if st.button("One-Click Guest Login"):
            st.session_state.logged_in = True
            st.session_state.username = "Demo Student"
            st.session_state.current_page = "Blueprint Generator"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PAGE 2: Home Page (Landing Page)
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Home":
    st.markdown("<div class='glowing-title'>EduSpark AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>The Complete Academic & Industry Project Blueprint Hub</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card-box'><h4>Production Blueprints</h4><p>Get complete system designs, folder hierarchies, and boilerplate code ready to run.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card-box'><h4>Interview & Viva Ready</h4><p>Detailed architectural questions and resume-ready bullets tailored for your projects.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card-box'><h4>Multi-Domain Engine</h4><p>Supports Python, Web Dev, AI/ML, Cloud, Cybersecurity, and more.</p></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Ready to engineer your next capstone project?")
    if st.button("Launch Blueprint Generator", type="primary"):
        if st.session_state.logged_in:
            st.session_state.current_page = "Blueprint Generator"
        else:
            st.session_state.current_page = "Login / Register"
        st.rerun()

# -----------------------------------------------------------------------------
# PAGE 3: Settings Page
# -----------------------------------------------------------------------------
elif st.session_state.logged_in and st.session_state.current_page == "Settings":
    st.markdown("<div class='glowing-title'>Account Settings</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Manage your developer profile and default blueprint preferences.</div>", unsafe_allow_html=True)

    with st.form("settings_form"):
        st.markdown("### Profile Preferences")
        new_name = st.text_input("Display Name", value=st.session_state.username)
        default_domain = st.selectbox("Primary Domain", ["Python", "Web Development", "Artificial Intelligence", "Cybersecurity", "Java / Spring"], index=0)
        default_level = st.selectbox("Default Experience Level", ["Beginner", "Intermediate", "Advanced"], index=1)
        save_btn = st.form_submit_button("Save Preferences", type="primary")

        if save_btn:
            st.session_state.username = new_name
            st.session_state.user_domain = default_domain
            st.success("Settings saved successfully!")

# -----------------------------------------------------------------------------
# PAGE 4: Blueprint Generator (Main Hub)
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Blueprint Generator":
    st.markdown("<div class='glowing-title'>EduSpark Blueprint Engine</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Enter your target specialization to generate full project architectures.</div>", unsafe_allow_html=True)

    with st.form("project_input_form"):
        st.markdown("<h3 style='color: #ffffff !important; margin-bottom: 20px;'>Student Profile Settings</h3>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            subject = st.text_input("Subject / Domain", value=st.session_state.user_domain, placeholder="e.g. Python, AI, Web Dev")
        with col2:
            skill_level = st.selectbox("Current Skill Level", ["Beginner", "Intermediate", "Advanced"])
        with col3:
            interests = st.text_input("Interests / Specialization", placeholder="e.g. Healthcare, Finance, Gaming, Cloud")

        num_ideas = st.slider("Number of Blueprints to Generate", min_value=1, max_value=2, value=2)

        st.markdown("<br>", unsafe_allow_html=True)
        submit_btn = st.form_submit_button("Generate Industry Blueprints", type="primary")

    if submit_btn:
        if not subject:
            st.warning("Please fill the Subject / Domain field.")
        else:
            with st.spinner("Compiling full project architecture & implementation roadmap..."):
                time.sleep(1.0)
                blueprints = generate_master_blueprints(subject, skill_level, interests, num_ideas)

                st.success("Comprehensive Project Blueprints Ready!")

                for idx, proj in enumerate(blueprints, 1):
                    with st.expander(f"Blueprint #{idx}: {proj['title']}", expanded=True):
                        st.markdown(f"#### {proj['title']}")
                        st.caption(f"**Complexity:** `{proj['complexity']}` | **Category:** `{subject.title()}`")
                        st.info(proj['tagline'])

                        st.markdown("---")

                        c1, c2 = st.columns(2)
                        with c1:
                            st.markdown("##### Key Features")
                            for feat in proj["features"]:
                                st.write(f"- {feat}")
                        with c2:
                            st.markdown("##### Recommended Tech Stack")
                            tech_badges = " ".join([f"`{t}`" for t in proj["tech_stack"]])
                            st.write(tech_badges)

                        st.markdown("---")
                        st.markdown("##### 1. Production Folder Architecture")
                        st.code(proj["folder_structure"], language="bash")

                        st.markdown("##### 2. Core Boilerplate / Starter Code")
                        st.code(proj["starter_code"], language="python")

                        st.markdown("---")
                        st.markdown("##### 3. Database Schema & API Endpoints")
                        for spec in proj["db_api_design"]:
                            st.write(f"- {spec}")

                        st.markdown("---")
                        st.markdown("##### 4. Step-by-Step Execution Roadmap")
                        for step in proj["roadmap"]:
                            st.write(f"**{step.split(':')[0]}:** {step.split(':')[1]}")

                        st.markdown("---")
                        st.markdown("##### 5. Viva / Interview Questions & Resume Points")
                        for item in proj["interview_prep"]:
                            st.write(f"• {item}")

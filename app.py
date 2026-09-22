import streamlit as st
import time

st.set_page_config(
    page_title="EduSpark | AI Project Blueprint Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# Session State Setup
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
# Styling
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

    li[role="option"], div[role="option"] {
        background-color: #1e293b !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        padding: 10px 14px !important;
        cursor: pointer !important;
    }

    li[role="option"]:hover, div[role="option"]:hover {
        background-color: #2563eb !important;
        color: #ffffff !important;
    }

    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border: 1px solid #a855f7 !important;
        border-radius: 8px !important;
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
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TOP NAVIGATION BAR (Visible Everywhere on PC & Mobile)
# -----------------------------------------------------------------------------
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([1.5, 1, 1, 1, 1])

with nav_col1:
    st.markdown("<h3 style='margin:0; padding:0; background: linear-gradient(90deg,#38bdf8,#818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>EduSpark</h3>", unsafe_allow_html=True)

with nav_col2:
    if st.button("Home"):
        st.session_state.current_page = "Home"
        st.rerun()

with nav_col3:
    if st.button("Generator"):
        st.session_state.current_page = "Blueprint Generator"
        st.rerun()

with nav_col4:
    if st.session_state.logged_in:
        if st.button("Settings"):
            st.session_state.current_page = "Settings"
            st.rerun()
    else:
        if st.button("Login"):
            st.session_state.current_page = "Login / Register"
            st.rerun()

with nav_col5:
    if st.session_state.logged_in:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = "Guest User"
            st.session_state.current_page = "Home"
            st.rerun()
    else:
        st.caption(f"Status: Guest")

st.markdown("<hr style='margin-top: 5px; margin-bottom: 25px; border-color: #30363d;'>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Blueprint Engine
# -----------------------------------------------------------------------------
def generate_master_blueprints(sub, lvl, interest, count):
    topic = interest.strip().title() if interest.strip() else "Modern Systems"
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
                "Multi-role access control with secure JWT tokens"
            ],
            "tech_stack": [f"{domain}", "Streamlit / React", "FastAPI", "SQLite / PostgreSQL", "Docker", "PyTest"],
            "folder_structure": f"""{low_topic}_system/
│
├── app/
│   ├── main.py               # Main API Gateway & pipeline
│   ├── config.py             # Environment configurations
│   ├── models/               # Database ORM models
│   └── services/             # Core business logic & analytics
├── tests/
│   └── test_core.py          # Unit & integration test suite
├── requirements.txt
├── Dockerfile
└── README.md""",
            "starter_code": f"""# app/main.py
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
                f"API `POST /api/v1/{low_topic}/ingest`: Ingests real-time events.",
                f"API `GET /api/v1/{low_topic}/metrics`: Returns aggregated analytics."
            ],
            "roadmap": [
                "Phase 1: Architecture design and DB modeling",
                f"Phase 2: Ingestion & alert algorithm for {topic}",
                "Phase 3: Interactive UI and API integration",
                "Phase 4: Unit testing & Docker packaging"
            ],
            "interview_prep": [
                f"Viva Question: How does this system handle high {topic} data spikes?",
                "Answer: By decoupling data ingestion from analytical processing using queue workers.",
                "Resume Bullet: 'Designed a high-throughput monitoring engine reducing anomaly latency by 35%.'"
            ]
        },
        {
            "title": f"Autonomous {topic} Recommendation & Prediction Hub",
            "tagline": f"An intelligent {domain}-driven platform that pairs predictive modeling with dynamic filtering to automate decisions in {topic}.",
            "complexity": f"{lvl} | 50-60 Dev Hours",
            "features": [
                f"Context-aware recommendation engine tailored for {topic}",
                "Secure REST API backend with input validation",
                "Automated report generation with key insights",
                "Redis database caching for fast response times"
            ],
            "tech_stack": [f"{domain}", "FastAPI", "SQLAlchemy", "Redis", "Pandas", "GitHub Actions"],
            "folder_structure": f"""{low_topic}_hub/
│
├── src/
│   ├── api/router.py         # Endpoints
│   ├── core/algorithms.py    # Logic
│   └── schemas/payload.py    # Schemas
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
                f"API `POST /api/v1/recommend`: Returns ranked recommendations."
            ],
            "roadmap": [
                "Phase 1: Entity-relationship design and schema setup",
                f"Phase 2: Recommendation scoring logic for {topic}",
                "Phase 3: Redis caching layer & auth tokens",
                "Phase 4: Cloud deployment and testing"
            ],
            "interview_prep": [
                f"Viva Question: Why use JSON/JSONB for {topic} attributes?",
                "Answer: Provides flexibility without frequent table schema migrations.",
                "Resume Bullet: 'Engineered a prediction hub achieving 99.8% uptime with Redis caching.'"
            ]
        }
    ]
    return blueprints[:count]

# -----------------------------------------------------------------------------
# PAGE 1: Home
# -----------------------------------------------------------------------------
if st.session_state.current_page == "Home":
    st.markdown("<div class='glowing-title'>EduSpark AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>The Complete Academic & Industry Project Blueprint Hub</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card-box'><h4>Production Blueprints</h4><p>Complete system designs, folder hierarchies, and runnable starter code.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card-box'><h4>Interview & Viva Ready</h4><p>Architectural viva questions and resume-ready bullets.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card-box'><h4>Multi-Domain Engine</h4><p>Supports Python, Web Dev, AI/ML, Cloud, Cybersecurity, and more.</p></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Launch Blueprint Generator", type="primary"):
        st.session_state.current_page = "Blueprint Generator"
        st.rerun()

# -----------------------------------------------------------------------------
# PAGE 2: Blueprint Generator
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Blueprint Generator":
    st.markdown("<div class='glowing-title'>Blueprint Engine</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Generate complete production architectures tailored to your requirements.</div>", unsafe_allow_html=True)

    with st.form("project_input_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            subject = st.text_input("Subject / Domain", value=st.session_state.user_domain, placeholder="e.g. Python, AI, Web Dev")
        with col2:
            skill_level = st.selectbox("Current Skill Level", ["Beginner", "Intermediate", "Advanced"])
        with col3:
            interests = st.text_input("Interests / Specialization", placeholder="e.g. Healthcare, Finance, Gaming, Cloud")

        num_ideas = st.slider("Number of Blueprints to Generate", min_value=1, max_value=2, value=2)
        submit_btn = st.form_submit_button("Generate Industry Blueprints", type="primary")

    if submit_btn:
        if not subject:
            st.warning("Please fill the Subject / Domain field.")
        else:
            with st.spinner("Compiling full project architecture & implementation roadmap..."):
                time.sleep(0.8)
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

                        st.markdown("##### 2. Core Starter Code")
                        st.code(proj["starter_code"], language="python")

                        st.markdown("---")
                        st.markdown("##### 3. Database Schema & API Endpoints")
                        for spec in proj["db_api_design"]:
                            st.write(f"- {spec}")

                        st.markdown("---")
                        st.markdown("##### 4. Execution Roadmap")
                        for step in proj["roadmap"]:
                            st.write(f"- {step}")

                        st.markdown("---")
                        st.markdown("##### 5. Viva / Interview Questions & Resume Points")
                        for item in proj["interview_prep"]:
                            st.write(f"• {item}")

# -----------------------------------------------------------------------------
# PAGE 3: Login / Register
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Login / Register":
    st.markdown("<div class='glowing-title'>Student Portal Access</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Sign in to personalize your developer profile.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])
    with col1:
        with st.form("auth_form"):
            uname = st.text_input("Username or Email", placeholder="student@college.edu")
            pwd = st.text_input("Password", type="password", placeholder="••••••••")
            auth_submit = st.form_submit_button("Sign In", type="primary")

            if auth_submit:
                if uname.strip():
                    st.session_state.logged_in = True
                    st.session_state.username = uname.strip().split("@")[0].title()
                    st.session_state.current_page = "Blueprint Generator"
                    st.rerun()
                else:
                    st.warning("Please enter a valid username.")

    with col2:
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("### Quick Demo Access")
        st.write("One-click instant login:")
        if st.button("One-Click Guest Login"):
            st.session_state.logged_in = True
            st.session_state.username = "Demo Student"
            st.session_state.current_page = "Blueprint Generator"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PAGE 4: Settings
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Settings":
    st.markdown("<div class='glowing-title'>Account Settings</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Manage your developer profile and preferences.</div>", unsafe_allow_html=True)

    with st.form("settings_form"):
        new_name = st.text_input("Display Name", value=st.session_state.username)
        default_domain = st.selectbox("Primary Domain", ["Python", "Web Development", "Artificial Intelligence", "Cybersecurity", "Java / Spring"], index=0)
        save_btn = st.form_submit_button("Save Preferences", type="primary")

        if save_btn:
            st.session_state.username = new_name
            st.session_state.user_domain = default_domain
            st.success("Settings saved successfully!")

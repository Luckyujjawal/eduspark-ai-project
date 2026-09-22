import streamlit as st
import time

st.set_page_config(
    page_title="EduSpark | AI Project Blueprint Hub",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# User Storage & Session State
# -----------------------------------------------------------------------------
if "users_db" not in st.session_state:
    st.session_state.users_db = {
        "admin": "admin123"
    }

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "current_page" not in st.session_state:
    st.session_state.current_page = "Generator"
if "user_domain" not in st.session_state:
    st.session_state.user_domain = "Python"

# -----------------------------------------------------------------------------
# High-Contrast CSS (Password Eye Icon & Text Visibility Fix)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Main Background & Base Text */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #0d1117 !important;
        color: #f0f6fc !important;
    }

    h1, h2, h3, h4, h5, h6, p, span, label, strong, b, em, li, div {
        color: #ffffff !important;
        opacity: 1 !important;
    }

    .sub-title {
        color: #94a3b8 !important;
        font-size: 1.15rem;
        margin-bottom: 25px;
    }

    .glowing-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    div[data-testid="stForm"], .card-box {
        background-color: #161b22 !important;
        border: 2px solid #30363d !important;
        border-radius: 14px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }

    .card-box p, .card-box span, .card-box h3, .card-box h4, .card-box div {
        color: #f0f6fc !important;
        line-height: 1.6;
    }

    /* Text Inputs Container */
    .stTextInput input {
        background-color: #21262d !important;
        color: #ffffff !important;
        border: 1px solid #484f58 !important;
        border-radius: 8px !important;
        font-size: 1rem !important;
    }

    .stTextInput input::placeholder {
        color: #8b949e !important;
    }

    /* PASSWORD SHOW / HIDE (EYE ICON) VISIBILITY FIX */
    div[data-testid="stTextInput"] button,
    div[data-baseweb="input"] button {
        background-color: transparent !important;
        border: none !important;
        color: #38bdf8 !important;
        box-shadow: none !important;
    }

    div[data-testid="stTextInput"] button:hover,
    div[data-baseweb="input"] button:hover {
        background-color: rgba(56, 189, 248, 0.15) !important;
        border-radius: 4px !important;
    }

    div[data-testid="stTextInput"] svg,
    div[data-baseweb="input"] svg {
        fill: #38bdf8 !important;
        stroke: #38bdf8 !important;
        width: 20px !important;
        height: 20px !important;
        opacity: 1 !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #21262d !important;
        border: 1px solid #484f58 !important;
        border-radius: 8px !important;
    }

    div[data-baseweb="select"] * {
        color: #ffffff !important;
    }

    /* Dropdown popup options */
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
    }

    li[role="option"]:hover, div[role="option"]:hover {
        background-color: #2563eb !important;
        color: #ffffff !important;
    }

    /* Primary Submit Buttons */
    div[data-testid="stForm"] button[kind="primaryFormSubmit"],
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border: 1px solid #a855f7 !important;
        border-radius: 8px !important;
        width: 100% !important;
    }

    /* Expanders & Output text visibility */
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

    /* Loader Box */
    .auth-loader-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 30px;
        background: rgba(22, 27, 34, 0.95);
        border: 2px solid #818cf8;
        border-radius: 16px;
        box-shadow: 0 0 30px rgba(129, 140, 248, 0.4);
        margin: 20px auto;
        max-width: 480px;
    }

    .glowing-spinner {
        width: 60px;
        height: 60px;
        border: 4px solid #21262d;
        border-top: 4px solid #38bdf8;
        border-right: 4px solid #a855f7;
        border-radius: 50%;
        animation: spinRing 0.9s cubic-bezier(0.68, -0.55, 0.27, 1.55) infinite;
        margin-bottom: 20px;
    }

    .auth-pulse-text {
        font-size: 1.25rem;
        font-weight: 700;
        color: #38bdf8 !important;
    }

    @keyframes spinRing {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>
""", unsafe_allow_html=True)

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

# =============================================================================
# SCENARIO 1: NOT LOGGED IN -> GATEWAY
# =============================================================================
if not st.session_state.logged_in:
    st.markdown("<div class='glowing-title'>EduSpark AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Next-Gen Industry Project Blueprint Hub. Authentication is required to enter.</div>", unsafe_allow_html=True)

    auth_col1, auth_col2 = st.columns([1.2, 1])

    with auth_col1:
        tab_login, tab_register = st.tabs(["Sign In", "Create New Account"])

        with tab_login:
            with st.form("login_form"):
                st.markdown("#### Login to Developer Portal")
                l_user = st.text_input("Username", placeholder="e.g. admin").strip().lower()
                l_pass = st.text_input("Password", type="password", placeholder="••••••••").strip()
                login_btn = st.form_submit_button("Sign In", type="primary")

                if login_btn:
                    if not l_user or not l_pass:
                        st.warning("Please fill in both Username and Password.")
                    elif l_user in st.session_state.users_db and st.session_state.users_db[l_user] == l_pass:
                        anim_placeholder = st.empty()
                        anim_placeholder.markdown("""
                        <div class='auth-loader-container'>
                            <div class='glowing-spinner'></div>
                            <div class='auth-pulse-text'>Verifying Credentials...</div>
                        </div>
                        """, unsafe_allow_html=True)
                        time.sleep(0.8)

                        st.session_state.logged_in = True
                        st.session_state.username = l_user.title()
                        st.session_state.current_page = "Generator"
                        st.rerun()
                    else:
                        st.error("Invalid Username or Password. Please register if you are new.")

        with tab_register:
            with st.form("register_form"):
                st.markdown("#### Create a New Account")
                r_user = st.text_input("Choose Username", placeholder="e.g. lucky").strip().lower()
                r_pass = st.text_input("Create Password", type="password", placeholder="Min 4 characters").strip()
                r_pass2 = st.text_input("Confirm Password", type="password", placeholder="Re-enter password").strip()
                reg_btn = st.form_submit_button("Register & Activate Workspace", type="primary")

                if reg_btn:
                    if not r_user or not r_pass:
                        st.warning("All fields are required.")
                    elif len(r_pass) < 4:
                        st.warning("Password must be at least 4 characters long.")
                    elif r_pass != r_pass2:
                        st.error("Passwords do not match!")
                    elif r_user in st.session_state.users_db:
                        st.error("Username already exists! Please choose another.")
                    else:
                        st.session_state.users_db[r_user] = r_pass
                        st.session_state.logged_in = True
                        st.session_state.username = r_user.title()
                        st.session_state.current_page = "Generator"
                        st.rerun()

    with auth_col2:
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("### Developer Workspace Perks")
        st.write("• **Production Architecture**: Directory designs & tree structures.")
        st.write("• **Ready Starter Code**: Complete working boilerplate files.")
        st.write("• **Database & API Specs**: Relational schemas & REST specifications.")
        st.write("• **Interview & Viva Prep**: Model viva questions & resume impact metrics.")
        st.markdown("<hr style='border-color: #30363d;'>", unsafe_allow_html=True)
        st.write("🔒 Verified portal. Authentication required for entry.")
        st.markdown("</div>", unsafe_allow_html=True)

# =============================================================================
# SCENARIO 2: LOGGED IN -> DASHBOARD
# =============================================================================
else:
    top_c1, top_c2, top_c3, top_c4 = st.columns([2, 1, 1, 1])

    with top_c1:
        st.markdown(f"<h3 style='margin:0; padding:0; background: linear-gradient(90deg,#38bdf8,#818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>EduSpark | Hi, {st.session_state.username}</h3>", unsafe_allow_html=True)

    with top_c2:
        if st.button("Generator"):
            st.session_state.current_page = "Generator"
            st.rerun()

    with top_c3:
        if st.button("Settings"):
            st.session_state.current_page = "Settings"
            st.rerun()

    with top_c4:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.current_page = "Generator"
            st.rerun()

    st.markdown("<hr style='margin-top: 5px; margin-bottom: 25px; border-color: #30363d;'>", unsafe_allow_html=True)

    if st.session_state.current_page == "Generator":
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
                            st.caption(f"Complexity: `{proj['complexity']}` | Category: `{subject.title()}`")
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

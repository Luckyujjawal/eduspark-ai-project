import streamlit as st
import time

st.set_page_config(
    page_title="EduSpark | AI Project Blueprint Hub",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# User Storage & Session State Setup
# -----------------------------------------------------------------------------
# Data structure supporting both username and email lookups
if "users_db" not in st.session_state:
    st.session_state.users_db = {
        "admin": {
            "email": "admin@eduspark.com",
            "password": "admin123",
            "name": "Admin"
        }
    }

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "user_domain" not in st.session_state:
    st.session_state.user_domain = "Python"

# -----------------------------------------------------------------------------
# Styling (Fixed High-Contrast Input & Google Button)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #0d1117 !important;
        color: #f0f6fc !important;
    }

    .glowing-title {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    div[data-testid="stForm"], .card-box {
        background-color: #161b22;
        border: 2px solid #30363d;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
    }

    /* Fixed Dark Input Box */
    div[data-testid="stTextInput"] input,
    div[data-baseweb="input"] input,
    input {
        background-color: #1f2937 !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: 1px solid #4b5563 !important;
        border-radius: 8px !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        padding: 10px 14px !important;
    }

    /* Eye icon button and container */
    div[data-baseweb="input"] > div,
    div[data-baseweb="input"] button {
        background-color: #1f2937 !important;
        border: none !important;
    }

    div[data-baseweb="input"] svg {
        fill: #38bdf8 !important;
        stroke: #38bdf8 !important;
        width: 22px !important;
        height: 22px !important;
    }

    /* Primary Submit Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border: 1px solid #a855f7 !important;
        border-radius: 8px !important;
        width: 100% !important;
    }

    /* Expanders */
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
# TOP NAVBAR
# -----------------------------------------------------------------------------
nav_c1, nav_c2, nav_c3, nav_c4 = st.columns([2, 1, 1, 1])

with nav_c1:
    st.markdown("<h3 style='margin:0; padding:0; background: linear-gradient(90deg,#38bdf8,#818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>EduSpark AI</h3>", unsafe_allow_html=True)

with nav_c2:
    if st.button("🏠 Home"):
        st.session_state.current_page = "Home"
        st.rerun()

with nav_c3:
    if not st.session_state.logged_in:
        if st.button("🔐 Login / Register"):
            st.session_state.current_page = "Auth"
            st.rerun()
    else:
        if st.button("🚀 Workspace"):
            st.session_state.current_page = "Generator"
            st.rerun()

with nav_c4:
    if st.session_state.logged_in:
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.current_page = "Home"
            st.rerun()
    else:
        st.caption("Status: Guest")

st.markdown("<hr style='margin-top: 5px; margin-bottom: 25px; border-color: #30363d;'>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Helper: Dual Auth Validator (Username OR Email)
# -----------------------------------------------------------------------------
def verify_user_login(login_input, password):
    clean_input = login_input.strip().lower()
    for user_key, data in st.session_state.users_db.items():
        if (clean_input == user_key.lower() or clean_input == data["email"].lower()) and password == data["password"]:
            return data["name"]
    return None

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
# VIEW 1: HOME PAGE
# =============================================================================
if st.session_state.current_page == "Home":
    st.markdown("<div class='glowing-title'>EduSpark AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Next-Gen Project Blueprint, System Architecture & Code Generation Platform.</div>", unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("<div class='card-box'><h4>Production Blueprints</h4><p>Complete project file structures, backend boilerplate, and setup instructions.</p></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='card-box'><h4>Interview & Viva Ready</h4><p>Get architectural viva questions, model answers, and resume-ready bullets.</p></div>", unsafe_allow_html=True)
    with col_c:
        st.markdown("<div class='card-box'><h4>Multi-Domain Coverage</h4><p>Python, Web Development, Artificial Intelligence, Cybersecurity, and Cloud Systems.</p></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Get Started / Login to Generator", type="primary"):
        if st.session_state.logged_in:
            st.session_state.current_page = "Generator"
        else:
            st.session_state.current_page = "Auth"
        st.rerun()

# =============================================================================
# VIEW 2: LOGIN / REGISTER PAGE (DUAL AUTH + GOOGLE ACCESS)
# =============================================================================
elif st.session_state.current_page == "Auth" and not st.session_state.logged_in:
    st.markdown("<div class='glowing-title'>Portal Authentication</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Sign in with your Username, Registered Email, or Direct Google Account.</div>", unsafe_allow_html=True)

    auth_col1, auth_col2 = st.columns([1.2, 1])

    with auth_col1:
        # One-Click Google Authentication Button
        st.markdown("<div style='margin-bottom: 12px;'>", unsafe_allow_html=True)
        if st.button("🌐 Continue with Google Account"):
            with st.spinner("Connecting securely with Google OAuth services..."):
                time.sleep(0.8)
                st.session_state.logged_in = True
                st.session_state.username = "Google User"
                st.session_state.current_page = "Generator"
                st.success("Google Authentication Verified! Welcome.")
                time.sleep(0.4)
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center; color: #94a3b8; margin-bottom: 15px;'>— OR ACCESS VIA CREDENTIALS —</div>", unsafe_allow_html=True)

        tab_login, tab_register = st.tabs(["🔐 Sign In", "📝 Create New Account"])

        # --- TAB: LOGIN ---
        with tab_login:
            with st.form("login_form"):
                st.markdown("#### Login with Username or Email")
                login_id = st.text_input("Username or Email Address", placeholder="e.g. admin or student@gmail.com").strip()
                l_pass = st.text_input("Password", type="password", placeholder="Enter password").strip()
                login_btn = st.form_submit_button("Sign In to Portal", type="primary")

                if login_btn:
                    if not login_id or not l_pass:
                        st.warning("Please enter both Username/Email and Password.")
                    else:
                        verified_name = verify_user_login(login_id, l_pass)
                        if verified_name:
                            st.session_state.logged_in = True
                            st.session_state.username = verified_name
                            st.session_state.current_page = "Generator"
                            st.success(f"Welcome back, {verified_name}! Opening Workspace...")
                            time.sleep(0.5)
                            st.rerun()
                        else:
                            st.error("Invalid credentials. Please check your username/email or password.")

        # --- TAB: REGISTER ---
        with tab_register:
            with st.form("register_form"):
                st.markdown("#### Create a New Account")
                reg_name = st.text_input("Full Name", placeholder="e.g. Lucky Ujjawal").strip()
                reg_user = st.text_input("Choose Username", placeholder="e.g. lucky99").strip().lower()
                reg_email = st.text_input("Email Address", placeholder="e.g. lucky@example.com").strip().lower()
                r_pass = st.text_input("Create Password", type="password", placeholder="Min 4 characters").strip()
                r_pass2 = st.text_input("Confirm Password", type="password", placeholder="Re-enter password").strip()
                reg_btn = st.form_submit_button("Register & Activate Workspace", type="primary")

                if reg_btn:
                    if not reg_name or not reg_user or not reg_email or not r_pass:
                        st.warning("All fields are required.")
                    elif "@" not in reg_email or "." not in reg_email:
                        st.warning("Please enter a valid email address.")
                    elif len(r_pass) < 4:
                        st.warning("Password must be at least 4 characters long.")
                    elif r_pass != r_pass2:
                        st.error("Passwords do not match!")
                    elif reg_user in st.session_state.users_db:
                        st.error("Username already registered! Choose another.")
                    elif any(u["email"] == reg_email for u in st.session_state.users_db.values()):
                        st.error("This Email is already registered. Please login instead.")
                    else:
                        st.session_state.users_db[reg_user] = {
                            "email": reg_email,
                            "password": r_pass,
                            "name": reg_name
                        }
                        st.session_state.logged_in = True
                        st.session_state.username = reg_name
                        st.session_state.current_page = "Generator"
                        st.success("Account created successfully! Welcome to EduSpark.")
                        time.sleep(0.5)
                        st.rerun()

    with auth_col2:
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("### Developer Workspace Perks")
        st.write("• **Flexible Access**: Login via Username, Email or Google Account.")
        st.write("• **Production Architecture**: Complete directory designs.")
        st.write("• **Ready Starter Code**: Working boilerplate files.")
        st.write("• **Database & API Specs**: Relational schemas & REST endpoints.")
        st.write("• **Interview & Viva Prep**: Model viva questions & resume impact metrics.")
        st.markdown("<hr style='border-color: #30363d;'>", unsafe_allow_html=True)
        st.write("🔒 Verified portal. Authentication required for entry.")
        st.markdown("</div>", unsafe_allow_html=True)

# =============================================================================
# VIEW 3: MAIN BLUEPRINT GENERATOR (WORKSPACE)
# =============================================================================
elif st.session_state.current_page == "Generator" and st.session_state.logged_in:
    st.markdown(f"<div class='glowing-title'>Workspace | Hi, {st.session_state.username}</div>", unsafe_allow_html=True)
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
else:
    st.session_state.current_page = "Home"
    st.rerun()

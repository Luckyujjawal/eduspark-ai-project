import streamlit as st
import time

st.set_page_config(
    page_title="EduSpark AI | Project Blueprint Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# User Storage and Session State
# -----------------------------------------------------------------------------
if "users_db" not in st.session_state:
    st.session_state.users_db = {
        "admin": {
            "email": "admin@gmail.com",
            "password": "admin123",
            "name": "Admin"
        }
    }

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "user_domain" not in st.session_state:
    st.session_state.user_domain = "Python"
if "page" not in st.session_state:
    st.session_state.page = "Login / Register"

# -----------------------------------------------------------------------------
# Styling (Clean Dark Theme without Emoji)
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
# Blueprint Engine Logic
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

def verify_user_login(login_id, password):
    clean_id = login_id.strip().lower()
    for user_key, data in st.session_state.users_db.items():
        if (clean_id == user_key.lower() or clean_id == data["email"].lower()) and password == data["password"]:
            return data["name"], data["email"]
    return None, None

# -----------------------------------------------------------------------------
# Dedicated Page Router (Sidebar)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### Navigation Portal")
    if st.session_state.logged_in:
        st.write(f"Active Account: **{st.session_state.username}**")
        available_pages = [
            "Home",
            "Blueprint Generator",
            "Settings",
            "Logout"
        ]
    else:
        st.caption("Status: Unauthenticated")
        available_pages = [
            "Login / Register",
            "Home"
        ]

    selected_page = st.radio(
        "Select Page:",
        available_pages,
        index=available_pages.index(st.session_state.page) if st.session_state.page in available_pages else 0
    )
    st.session_state.page = selected_page
    st.markdown("---")
    st.caption("EduSpark AI Multi-Page Platform")

# =============================================================================
# SCENARIO A: LOGIN / REGISTER PAGE (Default Landing View)
# =============================================================================
if st.session_state.page == "Login / Register":
    st.markdown("<div class='glowing-title'>Authentication Gateway</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Please sign in with your Username or Gmail address, or create a new student profile.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.3, 1])

    with col1:
        tab_login, tab_register = st.tabs(["Sign In", "Create New Account"])

        with tab_login:
            with st.form("dedicated_login_form"):
                st.markdown("#### Developer Portal Sign In")
                login_id = st.text_input("Username or Gmail Address", placeholder="e.g. ujjawal or ujjawal@gmail.com").strip()
                l_pass = st.text_input("Password", type="password", placeholder="Enter your password").strip()
                login_btn = st.form_submit_button("Sign In to Platform", type="primary")

                if login_btn:
                    if not login_id or not l_pass:
                        st.warning("Please enter both Username/Gmail and Password.")
                    else:
                        verified_name, verified_email = verify_user_login(login_id, l_pass)
                        if verified_name:
                            st.session_state.logged_in = True
                            st.session_state.username = verified_name
                            st.session_state.user_email = verified_email
                            st.session_state.page = "Blueprint Generator"
                            st.success(f"Welcome back, {verified_name}! Redirecting to Workspace...")
                            time.sleep(0.5)
                            st.rerun()
                        else:
                            st.error("Invalid credentials. Please verify your details or register a new account.")

        with tab_register:
            with st.form("dedicated_reg_form"):
                st.markdown("#### New User Registration")
                reg_name = st.text_input("Full Name", placeholder="e.g. Ujjawal Jha").strip()
                reg_user = st.text_input("Choose Username", placeholder="e.g. ujjawal99").strip().lower()
                reg_email = st.text_input("Gmail Address", placeholder="e.g. ujjawal@gmail.com").strip().lower()
                r_pass = st.text_input("Create Password", type="password", placeholder="Minimum 4 characters").strip()
                r_pass2 = st.text_input("Confirm Password", type="password", placeholder="Re-enter password").strip()
                reg_btn = st.form_submit_button("Register & Activate Workspace", type="primary")

                if reg_btn:
                    if not reg_name or not reg_user or not reg_email or not r_pass:
                        st.warning("All input fields are required.")
                    elif "@" not in reg_email or "." not in reg_email:
                        st.warning("Please enter a valid Gmail or Email address.")
                    elif len(r_pass) < 4:
                        st.warning("Password must be at least 4 characters long.")
                    elif r_pass != r_pass2:
                        st.error("Passwords do not match. Please recheck.")
                    elif reg_user in st.session_state.users_db:
                        st.error("Username is already taken. Please choose another username.")
                    elif any(u["email"] == reg_email for u in st.session_state.users_db.values()):
                        st.error("This email address is already registered. Please sign in.")
                    else:
                        st.session_state.users_db[reg_user] = {
                            "email": reg_email,
                            "password": r_pass,
                            "name": reg_name
                        }
                        st.session_state.logged_in = True
                        st.session_state.username = reg_name
                        st.session_state.user_email = reg_email
                        st.session_state.page = "Blueprint Generator"
                        st.success("Account created successfully! Redirecting to Workspace...")
                        time.sleep(0.5)
                        st.rerun()

    with col2:
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("### Access Specifications")
        st.write("- **Dual Sign-In:** Authenticate using registered Username or Gmail address.")
        st.write("- **Gated Environment:** Architecture and starter code are strictly protected.")
        st.write("- **Instant Session:** Immediate workspace authorization upon credential verification.")
        st.markdown("<hr style='border-color: #30363d;'>", unsafe_allow_html=True)
        st.caption("Please sign in or register to access the Blueprint Generator and Settings.")
        st.markdown("</div>", unsafe_allow_html=True)

# =============================================================================
# SCENARIO B: HOME PAGE (Overview)
# =============================================================================
elif st.session_state.page == "Home":
    st.markdown("<div class='glowing-title'>EduSpark AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Next-Gen Project Blueprint, System Architecture & Code Generation Platform.</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card-box'><h4>Production Blueprints</h4><p>Complete project file structures, backend boilerplate, and setup instructions.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card-box'><h4>Interview & Viva Ready</h4><p>Get architectural viva questions, model answers, and resume-ready bullets.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card-box'><h4>Multi-Domain Coverage</h4><p>Python, Web Development, Artificial Intelligence, Cybersecurity, and Cloud Systems.</p></div>", unsafe_allow_html=True)

    st.markdown("---")
    if not st.session_state.logged_in:
        st.info("Authentication required. Please navigate to the Login / Register page to access tools.")
    else:
        st.success(f"Authenticated as {st.session_state.username}. Select Blueprint Generator from the sidebar to continue.")

# =============================================================================
# SCENARIO C: BLUEPRINT GENERATOR PAGE (Gated Workspace)
# =============================================================================
elif st.session_state.page == "Blueprint Generator":
    if not st.session_state.logged_in:
        st.warning("Access Denied! Please authenticate via the Login / Register page.")
        st.session_state.page = "Login / Register"
        st.rerun()

    st.markdown(f"<div class='glowing-title'>Blueprint Generator | Hi, {st.session_state.username}</div>", unsafe_allow_html=True)
    if st.session_state.user_email:
        st.caption(f"Authenticated Account: `{st.session_state.user_email}`")
    st.markdown("<div class='sub-title'>Generate complete production architectures tailored to your requirements.</div>", unsafe_allow_html=True)

    with st.form("dedicated_generator_form"):
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
                            tech_badges = tech_badges if tech_badges else "`Core`"
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
                            st.write(f"- {item}")

# =============================================================================
# SCENARIO D: SETTINGS PAGE
# =============================================================================
elif st.session_state.page == "Settings":
    if not st.session_state.logged_in:
        st.warning("Please sign in to access account preferences.")
        st.session_state.page = "Login / Register"
        st.rerun()

    st.markdown("<div class='glowing-title'>Account Settings</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Manage your developer profile and default blueprint preferences.</div>", unsafe_allow_html=True)

    with st.form("dedicated_settings_form"):
        st.markdown("### Profile Preferences")
        new_name = st.text_input("Display Name", value=st.session_state.username)
        default_domain = st.selectbox(
            "Default Domain",
            ["Python", "Web Development", "Artificial Intelligence", "Cybersecurity", "Java / Spring"],
            index=["Python", "Web Development", "Artificial Intelligence", "Cybersecurity", "Java / Spring"].index(st.session_state.user_domain) if st.session_state.user_domain in ["Python", "Web Development", "Artificial Intelligence", "Cybersecurity", "Java / Spring"] else 0
        )
        save_btn = st.form_submit_button("Save Preferences", type="primary")

        if save_btn:
            st.session_state.username = new_name
            st.session_state.user_domain = default_domain
            st.success("Preferences updated successfully!")

# =============================================================================
# SCENARIO E: LOGOUT PAGE
# =============================================================================
elif st.session_state.page == "Logout":
    st.markdown("<div class='glowing-title'>Sign Out Confirmation</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Are you sure you want to terminate your active developer session?</div>", unsafe_allow_html=True)

    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.write(f"Active User: **{st.session_state.username}**")
    if st.session_state.user_email:
        st.write(f"Registered Email: **{st.session_state.user_email}**")
    st.write("Terminating this session will protect your workspace until your next authentication.")
    st.markdown("</div>", unsafe_allow_html=True)

    col_l1, col_l2 = st.columns([1, 1])
    with col_l1:
        if st.button("Confirm Sign Out", type="primary"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.user_email = ""
            st.session_state.page = "Login / Register"
            st.success("Session ended successfully. Redirecting to Authentication...")
            time.sleep(0.5)
            st.rerun()

    with col_l2:
        if st.button("Cancel & Return to Generator"):
            st.session_state.page = "Blueprint Generator"
            st.rerun()

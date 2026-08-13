import json
import streamlit as st
from google import genai
from google.genai import types

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
DEFAULT_API_KEY = "AQ.Ab8RN6LjR6T1NYYRZfXHcbzV1eQw860CXaUCOO1RgaCZjeA8zg"

st.set_page_config(
    page_title="EduSpark | AI Project Blueprint Generator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# Custom CSS (Fixes Code Blocks & Badges Visibility)
# -----------------------------------------------------------------------------
st.markdown(
    """
<style>
    /* Main Background */
    .stApp {
        background-color: #0b0f19;
        color: #ffffff !important;
    }

    /* Headings & Text High Contrast */
    h1, h2, h3, h4, h5, h6, label, p, span, div {
        color: #ffffff !important;
    }

    /* Glowing Title */
    .glowing-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #cbd5e1 !important;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    /* Glassmorphism Card Container */
    div[data-testid="stForm"] {
        background-color: #151d2a !important;
        border: 1px solid #334155 !important;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }

    /* Input Fields */
    .stTextInput input, .stSelectbox [data-baseweb="select"] {
        background-color: #1e293b !important;
        color: #ffffff !important;
        border: 1px solid #475569 !important;
        border-radius: 8px !important;
    }

    .stSelectbox [data-baseweb="select"] * {
        color: #ffffff !important;
    }

    /* Action Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4) !important;
    }

    /* Expander Output Cards */
    div[data-testid="stExpander"] {
        background-color: #151d2a !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }

    div[data-testid="stExpander"] * {
        color: #f8fafc !important;
    }

    /* 📌 CRITICAL FIX: Code Tags / Tech Stack Badges Visibility */
    code {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        border: 1px solid #334155 !important;
        border-radius: 6px !important;
        padding: 4px 8px !important;
        font-weight: 600 !important;
    }

    /* Sidebar Background */
    section[data-testid="stSidebar"] {
        background-color: #070a12 !important;
        border-right: 1px solid #1e293b;
    }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# Header Section
# -----------------------------------------------------------------------------
st.markdown(
    "<div class='glowing-title'>🎓 EduSpark AI</div>", unsafe_allow_html=True
)
st.markdown(
    "<div class='sub-title'>Next-Gen Project Blueprint & Learning Roadmap Generator</div>",
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.image(
        "https://img.icons8.com/fluency/96/artificial-intelligence.png",
        width=80,
    )
    st.title("⚙️ Control Panel")
    st.markdown("---")
    st.markdown("✨ **Features Enabled:**")
    st.markdown("• High-Contrast Dark Theme")
    st.markdown("• Gemini 2.0 Flash Engine")
    st.markdown("• Dynamic Roadmap Engine")
    st.markdown("---")
    st.caption("🚀 Designed for Academic Presentations")

# -----------------------------------------------------------------------------
# Form Section
# -----------------------------------------------------------------------------
with st.form("project_input_form"):
    st.markdown(
        "<h3 style='color: #ffffff !important; margin-bottom: 20px;'>🎯 Student Profile Settings</h3>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        subject = st.text_input(
            "Subject / Domain",
            placeholder="e.g. Computer Science, AI, Web Dev",
        )
    with col2:
        skill_level = st.selectbox(
            "Current Skill Level", ["Beginner", "Intermediate", "Advanced"]
        )
    with col3:
        interests = st.text_input(
            "Interests / Specialization",
            placeholder="e.g. Healthcare, Finance, Gaming",
        )

    num_ideas = st.slider(
        "Number of Blueprints to Generate", min_value=1, max_value=3, value=2
    )

    st.markdown("<br>", unsafe_allow_html=True)
    submit_btn = st.form_submit_button("🚀 Generate Industry Blueprints")

# -----------------------------------------------------------------------------
# Execution & Display
# -----------------------------------------------------------------------------
if submit_btn:
    if not subject:
        st.warning("⚠️ Kripya Subject / Domain field fill karein.")
    else:
        try:
            client = genai.Client(api_key=DEFAULT_API_KEY)

            prompt = f"""
            Act as a Senior Academic Mentor & Software Architect.
            Generate {num_ideas} unique academic project ideas.

            Student Details:
            - Subject: {subject}
            - Skill Level: {skill_level}
            - Interests: {interests}

            Respond STRICTLY in valid JSON format with key 'projects':
            {{
                "projects": [
                    {{
                        "title": "Project Name",
                        "difficulty": "{skill_level}",
                        "summary": "Clear, impactful 2-line summary",
                        "key_features": ["Feature 1", "Feature 2", "Feature 3"],
                        "tech_stack": ["Tech 1", "Tech 2", "Tech 3"],
                        "roadmap": [
                            "Phase 1: Step description",
                            "Phase 2: Step description",
                            "Phase 3: Step description"
                        ]
                    }}
                ]
            }}
            """

            with st.spinner("⚡ AI is crafting your blueprints..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            response_mime_type="application/json"
                        ),
                    )
                except Exception:
                    response = client.models.generate_content(
                        model="gemini-flash-latest",
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            response_mime_type="application/json"
                        ),
                    )

                data = json.loads(response.text)

                st.success("🎉 Project Blueprints Generated Successfully!")

                for idx, proj in enumerate(data.get("projects", []), 1):
                    with st.expander(
                        f"📌 Blueprint #{idx}: {proj['title']}", expanded=True
                    ):

                        st.markdown(
                            f"**Difficulty Level:** `{proj['difficulty']}`"
                        )
                        st.markdown(f"**Overview:** {proj['summary']}")
                        st.markdown("---")

                        c1, c2 = st.columns(2)
                        with c1:
                            st.markdown("##### ✨ Key Features")
                            for feat in proj.get("key_features", []):
                                st.write(f"🔹 {feat}")

                        with c2:
                            st.markdown("##### 🛠️ Tech Stack")
                            tech_badges = " ".join(
                                [f"`{t}`" for t in proj.get("tech_stack", [])]
                            )
                            st.write(tech_badges)

                        st.markdown("---")
                        st.markdown("##### 🗺️ Execution Roadmap")
                        for step_num, step in enumerate(
                            proj.get("roadmap", []), 1
                        ):
                            st.write(f"**Step {step_num}:** {step}")

        except Exception as e:
            st.error(f"❌ Error occurred: {str(e)}")
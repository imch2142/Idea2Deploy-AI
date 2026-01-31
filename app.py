import streamlit as st
from planning_agent import planning_agent_mock
from architecture_agent import architecture_agent_mock
from security_agent import security_agent_mock
from deployment_agent import deployment_agent_mock
from PIL import Image
import base64
from io import BytesIO


bg_image = Image.open("image/ima.jpg")

buffered = BytesIO()
bg_image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

st.set_page_config(page_title="Idea2Deploy AI", layout="wide")

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{img_str}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

h1, h2, h3 {{
    color: #0f4c81;
    font-family: 'Arial', sans-serif;
}}

.stButton>button {{
    background-color: #0f4c81;
    color: white;
    font-weight: bold;
    font-size: 16px;
    padding: 10px 20px;
}}

.stTextInput>div>input {{
    background-color: rgba(255,255,255,0.9);
    color: black;
    font-weight: bold;
}}
</style>
""", unsafe_allow_html=True)



st.title("💡 Idea2Deploy AI - Mock Version")


idea = st.text_input("Enter your project idea:")


if st.button("🚀 Generate Project Plan"):
    if idea.strip() == "":
        st.warning("⚠️ Please enter a project idea before generating the plan!")
    else:
        with st.expander("📝 Planning Agent Output", expanded=True):
            st.text(planning_agent_mock(idea))
        
        with st.expander("🏛️ Architecture Agent Output", expanded=True):
            st.text(architecture_agent_mock(idea))
        
        with st.expander("🔒 Security Agent Output", expanded=True):
            st.text(security_agent_mock(idea))
        
        with st.expander("🚀 Deployment Agent Output", expanded=True):
            st.text(deployment_agent_mock(idea))

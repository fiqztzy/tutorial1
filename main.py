import streamlit as st

# ----- PAGE SETUP -----
st.set_page_config(page_title="My Resume", page_icon="📄", layout="centered")

# ----- HEADER SECTION -----
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://via.placeholder.com/150", caption="Your Name", use_container_width=True)  # Replace with your image path or URL

with col2:
    st.title("MUHAMMAD SHAFIQ IQWAN BIN MOHD BASRI")
    st.write("📍 Location: DUNGUN, TERENGGANU")
    st.write("✉️ Email: shafiqiqwan35@gmail.com")
    st.write("📞 Phone: +60137780938")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)")

st.markdown("---")

# ----- EDUCATION SECTION -----
st.header("🎓 Education")
st.write("**Bachelor of infirmation technology**, Universiti Malaysia Kelantan (2022 – 2026)")
st.write("- Major in Artificial Intelligence")


st.markdown("---")

# ----- WORK EXPERIENCE SECTION -----
st.header("💼 Work Experience")
st.write("**Retail Assistant**, Kedai Runcit Nor Zaleha (2025 – 2026)")
st.write("- Assisted customers with purchases and provided good customer service")
st.write("- Managed inventory, restocked shelves, and ensured store cleanliness")

st.markdown("---")

# ----- SKILLS SECTION -----
st.header("🧠 Skills")
skills_col1, skills_col2 = st.columns(2)

with skills_col1:
    st.write("- Python")
    st.write("- HTML / CSS / JavaScript")
    st.write("- IOT")

st.markdown("---")

# ----- PROJECTS SECTION -----
st.header("🚀 Projects & Achievements")
st.write("**SMILYVY – Dental Care App**")
st.write("- Developed a mobile application to promote better dental care and oral hygiene")
st.write("- Implemented features for daily dental routine tracking and reminders")



st.markdown("---")

# ----- FOOTER -----
st.markdown(
    """
    <div style='text-align: center; color: grey; font-size: 0.9em;'>
        ©️ 2025 Your Name | Built with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

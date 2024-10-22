from pathlib import Path

import streamlit as st
from PIL import Image

# Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# General Settings
PAGE_TITLE = "Digital CV | Alexey Kuznetsov"
PAGE_ICON = ":wave:"
NAME = "Alexey Kuznetsov"
DESCRIPTION = """
Middle fullstack web-developer.
"""
EMAIL = "alexkuz2001@gmail.com"
PHONE_NUMBER = "+34 607 373 479"
PROJECTS = {
    "🏆 Construction Website - Developing from scratch": "https://www.kkontinent.ru/",
    "🏆 Crypto Front-end - Web app interface design": "https://www.cryptohall24.com/",
    "🏆 Desktop Application for dropshipping - Application that compares prices online, dowloads product info + images and prepares for CRM import in a csv file": "https://businesstool.streamlit.app/",
    "🏆 Web Application for dropshipping - Developed for Web-browsers":"https://businesstool.streamlit.app/",
    "🏆 Vape shop - Developed from scratch": "https://www.osmoke.fr/",
    "🏆 Rome store - Developed from scratch": "Not online yet",
    "🏆 Micromania online store - Developed from scratch": "https://www.micromania.fr/home",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📞", PHONE_NUMBER)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 Years expereince in web development
- ✔️ Strong hands on experience and knowledge in HTML, CSS, JavaScript, PHP, Python
- ✔️ Strong understanding of API, databases, UI/UX design, AI integration
- ✔️ Ability to develop any kind of websites
- ✔️ Ability to setup network systems and test their security
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: HTML, CSS, JavaScript, PHP, Python, SQL,
- 📊 Platforms: Figma, Wordpress, Tilda, Prestashop, Photoshop, Blender etc. 
- 🗄️ Databases: Postgres, MongoDB, MySQL
- 📚 Languages: English C1, Russian
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Junior Fullstack Developer | Rusagro (Russia)**")
st.write("02/2019 - 03/2022")
st.write(
    """
- ► Working in Rusagro in Moscow as internship, developing an application to improve logistics inside the company.
- ► I have developed multiple algoriths in python that optimises the application overall, I used a method called threading.
- ► Took part in a few start-ups VibeCheck social media app and EasyBuy to create a platform to simplify buying products online.
- ► Developing the interface for the company's application for drivers, to track their destinations and packages.
- ► Working with Google Maps API to set the routes for the drivers.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Middle Fullstack Web Developer | Osmoke.fr**")
st.write("02/2022 - 03/2023")
st.write(
    """
- ► Development of front-end and back-end of the website using HTML, CSS, Javascript. 
- ► Automating the import of products and adding new products.
- ► Editing the images for the website.
- ► Working with databases MySQL.
- ► Setting up the API for the payment system.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Middle Fullstack Web Developer | ProductInfo**")
st.write("03/2023 - 09/2024")
st.write(
    """
- ► Developed a desktop version of an application using Python.
- ► Constructing and coding modern UI/UX design.
- ► Optimised the app for faster scanning and formatting.
- ► Developed this app as a web-application.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
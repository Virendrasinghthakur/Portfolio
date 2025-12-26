import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title="My Portfolio", page_icon=":briefcase:", layout="wide")

# -------------------- Load Lottie Animation --------------------
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

lottie_coder = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_kyu7xb1v.json")
lottie_contact = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")

# -------------------- Helpers --------------------
def load_img(path):
    try:
        return Image.open(path)
    except:
        return None

def load_resume(path):
    try:
        with open(path, "rb") as f:
            return f.read()
    except:
        return None

# -------------------- Load Assets --------------------
profile_img = load_img("Profile.jpg")
dubify_img = load_img(r"D:\Project\Portfolio\Portfolio\UI_SS.png")
ecommerce_img = load_img(r"D:\Project\Portfolio\Portfolio\ecommerce_ui_ss.png")
bank_img = load_img(r"D:\Project\Portfolio\Portfolio\bank_ui_ss.png")

resume_bytes = load_resume(r"D:\Project\Portfolio\Portfolio\Virendra_Resume 2025.pdf")

LINKEDIN_URL = "https://www.linkedin.com/in/virendra-singh-7224522a0/"

# -------------------- Header --------------------
st.write("##")
st.subheader("Welcome to My Portfolio!")
st.title("My Portfolio Page")
st.write("This is where I showcase my projects and skills.")
st.write("___")

col_img, col_txt = st.columns([1, 3])

with col_img:
    if profile_img:
        st.image(profile_img, width=180)
    else:
        st.warning("Profile image not found")

with col_txt:
    st.markdown("### 👋 Hi, I am Virendra Singh")
    st.markdown("**Computer Science Undergraduate | AI and Backend Developer**")
    st.write(
        "I am a passionate fresher with strong fundamentals in Python and Data Structures, "
        "focused on building real-world projects in AI and scalable backend systems. "
        "I love learning fast, writing clean code, and turning ideas into working products."
    )

    c1, c2 = st.columns(2)
    with c1:
        if resume_bytes:
            st.download_button(
                "📄 Download Resume",
                resume_bytes,
                file_name="Virendra_Singh_Resume.pdf",
                mime="application/pdf"
            )
    with c2:
        st.markdown(
            f"[🔗 Visit my LinkedIn]({LINKEDIN_URL})",
            unsafe_allow_html=True
        )

# -------------------- Navigation --------------------
selected = option_menu(
    menu_title=None,
    options=['About', 'Projects', 'Tools & Stacks', 'Contact'],
    icons=['person', 'code-slash', 'tools', 'chat-left-text-fill'],
    orientation='horizontal'
)

# -------------------- About --------------------
if selected == 'About':
    st.write("##")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("I am Virendra Singh")
        st.title("Undergrad at Jaipur Engineering College")

    with col2:
        if lottie_coder:
            st_lottie(lottie_coder, height=300, key="coder")

    st.write("___")

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Education")
        st.markdown("""
- **Jaipur Engineering College**  
  B.E. in Computer Science (AI) | 2023–2027  

- **RV Public School**  
  12th Grade (PCM) | 2021–2023  

- **Sanskar Public School**  
  10th Grade | 2019–2021
""")
    with col4:
        st.subheader("Experience")
        st.markdown("Fresher with strong hands-on project experience.")

# -------------------- Projects --------------------
elif selected == 'Projects':
    st.header("My Projects")
    st.write("##")

    # Dubify
    col1, col2 = st.columns((1, 2))
    with col1:
        if dubify_img:
            st.image(dubify_img, width=230)
    with col2:
        st.subheader("🎙️ Dubify – AI Video Dubbing System")
        st.write(
            "AI-powered system that automates speech-to-text, multilingual translation, "
            "and text-to-speech to generate natural voiceovers and merge them back into videos."
        )
        st.markdown("**Technologies:** Python, Speech Recognition, NLP, TTS, FFmpeg")
        st.markdown("[🔗 View on GitHub](https://github.com/Virendrasinghthakur/Dubify_Project)")

    st.write("---")

    # E-commerce Backend
    col3, col4 = st.columns((1, 2))
    with col3:
        if ecommerce_img:
            st.image(ecommerce_img, width=230)
    with col4:
        st.subheader("🛒 E-commerce Backend System")
        st.write(
            "Scalable backend with secure REST APIs for authentication, product management, "
            "cart, and order processing using clean architecture."
        )
        st.markdown("**Technologies:** Python, FastAPI, MySQL, JWT, Pydantic, REST APIs")
        st.markdown("[🔗 View on GitHub](https://github.com/Virendrasinghthakur/Ecommerce_backend_project)")

    st.write("---")

    # Bank Management System
    col5, col6 = st.columns((1, 2))
    with col5:
        if bank_img:
            st.image(bank_img, width=230)
    with col6:
        st.subheader("🏦 Bank Management System")
        st.write(
            "Python-based system to manage bank accounts, customers, and transactions, "
            "focusing on OOP and data handling."
        )
        st.markdown("**Technologies:** Python, OOP, File Handling")
        st.markdown("[🔗 View on GitHub](https://github.com/Virendrasinghthakur/Banking_project_ver1.00)")

    st.write("---")
    st.subheader("📌 Additional Projects & Highlights")
    st.markdown("""
- 📊 **Power BI Dashboard:** Built interactive dashboards with KPIs, slicers, and drill-downs for business insights.  
- 📈 **Excel Dashboards:** Created dashboards using pivot tables, charts, formulas, and automation for reporting.  
- 🧠 **Multiple Mini Projects:** Developed projects using **Python, C++, DSA, OOP, FastAPI, ML, GenAI, and data visualization tools** to strengthen problem-solving and system design.
""")

# -------------------- Tools & Stacks --------------------
elif selected == 'Tools & Stacks':
    st.write("##")
    st.subheader("Tools & Stacks")
    st.title("Technologies I Work With")
    st.write("From backend systems to data, AI, and developer tools.")
    st.write("___")

    html_code = """
    <style>
    .tech-panel {
        border: 2px solid #333;
        border-radius: 20px;
        padding: 25px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 24px;
        background-color: rgba(255,255,255,0.05);
    }
    .tech-item {
        text-align: center;
        width: 110px;
        font-family: sans-serif;
        color: white;
    }
    .tech-item img {
        width: 60px;
        height: 60px;
        object-fit: contain;
        margin-bottom: 6px;
    }
    .tech-item span {
        font-weight: 600;
        font-size: 12px;
        display: block;
    }
    </style>

    <div class="tech-panel">
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"><span>Python</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"><span>C++</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg"><span>NumPy</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"><span>Pandas</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"><span>TensorFlow</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg"><span>FastAPI</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"><span>Git</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"><span>GitHub</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"><span>Docker</span></div>
        <div class="tech-item"><img src="https://streamlit.io/images/brand/streamlit-mark-color.png"><span>Streamlit</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg"><span>Jupyter</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"><span>VS Code</span></div>
        <div class="tech-item"><img src="https://colab.research.google.com/img/colab_favicon_256px.png"><span>Google Colab</span></div>
        <div class="tech-item"><img src="https://upload.wikimedia.org/wikipedia/en/d/d2/Sublime_Text_3_logo.png"><span>Sublime</span></div>
        <div class="tech-item"><img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg"><span>Power BI</span></div>
        <div class="tech-item"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftoffice/microsoftoffice-original.svg"><span>Excel</span></div>
        <div class="tech-item"><img src="https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png"><span>LeetCode</span></div>
        <div class="tech-item"><img src="https://media.geeksforgeeks.org/gfg-gg-logo.svg"><span>GeeksforGeeks</span></div>
    </div>
    """
    components.html(html_code, height=560, scrolling=True)

# -------------------- Contact --------------------
elif selected == 'Contact':
    st.header("Get in Touch")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/veersingh16400@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required><br><br>
        <input type="email" name="email" placeholder="Your email" required><br><br>
        <textarea name="message" placeholder="Your message here..." rows="4" required></textarea><br><br>
        <button type="submit">Send</button>
    </form>
    """

    left_col, right_col = st.columns((2, 1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        if lottie_contact:
            st_lottie(lottie_contact, height=300)

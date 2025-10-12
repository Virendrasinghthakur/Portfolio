import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image
import requests

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

# -------------------- Load Image --------------------
try:
    image = Image.open("C:/Users/Asus/Pictures/Camera Roll/WIN_20250227_00_02_06_Pro.jpg")
except:
    image = None

# -------------------- Header Section --------------------
st.write("##")
st.subheader("Welcome to My Portfolio!")
st.title("My portfolio page")
st.write("""
This is where I showcase my projects and skills.
""")
st.write("[read more >](link)")
st.write("___")

# -------------------- Navigation Menu --------------------
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Tools & Stacks', 'Contact'],
        icons=['person', 'code-slash', 'tools', 'chat-left-text-fill'],
        orientation='horizontal'
    )

# -------------------- About Section --------------------
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Virendra Singh")
            st.title('Undergrad at JEC')
        with col2:
            if lottie_coder:
                st_lottie(lottie_coder, height=300, key="coder")
            else:
                st.warning("⚠️ Animation could not be loaded. Check the URL.")

    st.write("___")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Education")
            st.markdown("""
- **JEC**
    - Bachelor of Engineering – Computer Science (Artificial Intelligence)
    - Grade: XYZ
    - Session: 2023-2027
- **RV Public School**
    - 12th Grade (PCM)
    - Grade: 61%
    - Year: 2022-2023
- **Sanskar Public School**
    - 10th Grade
    - Grade: 64%
    - Year: 2020-2021
""")
        with col4:
            st.subheader("Experiences")
            st.markdown("Currently building experience...")

# -------------------- Projects Section --------------------
elif selected == 'Projects':
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns((1, 2))

        with col5:
            if image:
                st.image(image)
            else:
                st.info("Project image not found")
        with col6:
            st.subheader("**Bank Managing System**")
            st.markdown("[Visit Github Repo](https://github.com/Virendrasinghthakur/Banking_project_ver1.00)")

# -------------------- Tools & Stacks Section --------------------
elif selected == 'Tools & Stacks':
    st.write("##")
    st.subheader("Tools & Stacks")
    st.title("Technologies I work with")
    st.write("""
    I've worked with a range of technologies in the Data Science world,
    from Back-end to Design.
    """)
    st.write("___")

    # CSS for the rounded rectangle
    st.markdown(
        """
        <style>
        .tech-panel {
            border: 2px solid #333;
            border-radius: 20px;
            padding: 20px;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            background-color: rgba(255,255,255,0.05);
            margin-bottom: 20px;
        }
        .tech-item {
            text-align: center;
            width: 100px;
        }
        .tech-item img {
            width: 60px;
            height: 60px;
            margin-bottom: 5px;
            object-fit: contain;
        }
        .tech-item span {
            display: block;
            font-weight: bold;
            font-size: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # HTML for all technology icons
    st.markdown(
        """
        <div class="tech-panel">
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python">
                <span>Python</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" alt="C++">
                <span>C++</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" alt="NumPy">
                <span>NumPy</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" alt="Pandas">
                <span>Pandas</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" alt="TensorFlow">
                <span>TensorFlow</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git">
                <span>Git</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub">
                <span>GitHub</span>
            </div>
            <div class="tech-item">
                <img src="https://avatars.githubusercontent.com/u/110818415?s=200&v=4" alt="Pydantic">
                <span>Pydantic</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" alt="FastAPI">
                <span>FastAPI</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Docker">
                <span>Docker</span>
            </div>
            <div class="tech-item">
                <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit">
                <span>Streamlit</span>
            </div>
            <div class="tech-item">
                <img src="https://python.langchain.com/img/brand/wordmark.png" alt="LangChain" style="width: 80px;">
                <span>LangChain</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- Contact Section --------------------
elif selected == 'Contact':
    st.header('Get in touch')
    st.write('##')

    # CSS for form styling
    st.markdown("""
        <style>
        input[type=text], input[type=email], textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            margin-top: 6px;
            margin-bottom: 16px;
            resize: vertical;
        }
        button[type=submit] {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button[type=submit]:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

    contact_form = """
    <form action="https://formsubmit.co/veersingh16400@email.com" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" placeholder="Enter your name" required><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" placeholder="Enter your email" required><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" placeholder="Your message here..." rows="4" required></textarea><br>

        <button type="submit">Send Message</button>
    </form>
    """

    left_col, right_col = st.columns((2, 1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        if lottie_contact:
            st_lottie(lottie_contact, height=300)
        else:
            st.info("Animation loading...")
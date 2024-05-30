import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Helper function to load image from URL
def load_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Function to display the portfolio header
def display_header():
    image_url = "images/profile.jpg"
    st.image(load_image(image_url), width=150)  # Add your profile photo
    st.title("Asef AHmed")
    st.subheader("Frontend Developer")
    st.write("Welcome to my portfolio website! I specialize in creating stunning and efficient web interfaces.")

# Function to display the about section
def display_about():
    st.header("About Me")
    st.write("""
    I am a passionate Frontend Developer with experience in creating responsive and user-friendly web applications.
    My skill set includes HTML, CSS, JavaScript, React, and more. I enjoy working on challenging projects and learning new technologies.
    """)

# Function to display the projects section
def display_projects():
    st.header("Projects")
    st.write("Here are some of the projects I've worked on:")
    
    # Example project 1
    st.subheader("Project 1: Emotion Detection  ")
    # project1_image_url = ""
    # st.image(load_image(project1_image_url))
    st.write("""
       Emotion Dectecion App . Live Link : https://asefahmed500-emotion-app--app-pz5jiu.streamlit.app/
    """)
    st.write("[GitHub Repository](https://github.com/asefahmed500/emotion-app-.git)")
    
    # Example project 2
    st.subheader("Project 2: Quantum Error Mitigation Using Machine learing ")
    # project2_image_url = "https://via.placeholder.com/300"
    # st.image(load_image(project2_image_url))
    st.write("""
    An e-commerce website with a fully functional shopping cart and checkout process. Built with React and Redux.
    """)
    st.write("[GitHub Repository](https://github.com/asefahmed500/Error-Mitigate-with-Blackwater-.git)")
    
    # Add more projects as needed
    # ...

# Function to display the contact section
def display_contact():
    st.header("Contact Me")
    st.write("Feel free to reach out to me via the following platforms:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("📧 Email: asefahmed500@gmail.com")
    with col2:
        st.write("💼 LinkedIn: [ LinkedIn](https://www.linkedin.com/in/asef-ahmed-213062201/)")
    
    st.write("🐙 GitHub: [ GitHub](https://github.com/asefahmed500)")

# Main function to control the layout
def main():
    # Customize the page
    st.set_page_config(page_title="Portfolio - Your Name", page_icon=":briefcase:", layout="centered")

    st.markdown("""
        <style>
        .main-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .main-header img {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
        }
        .main-header h1 {
            font-size: 2.5rem;
            margin-bottom: 0;
        }
        .main-header h2 {
            color: #888;
            margin-top: 0.5rem;
        }
        .st-bb { 
            border-bottom: 1px solid #ddd;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
        }
        .st-az {
            font-size: 1.2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="main-header">
        <img src="" alt="Profile Image">
        <h1>Asef Ahmed </h1>
        <h2>Frontend Developer</h2>
        <p>Welcome to my portfolio website! I specialize in creating stunning and efficient web interfaces.</p>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

    if page == "Home":
        st.markdown("<div class='st-bb st-az'>Welcome to my portfolio website! I specialize in creating stunning and efficient web interfaces.</div>", unsafe_allow_html=True)
    elif page == "About":
        display_about()
    elif page == "Projects":
        display_projects()
    elif page == "Contact":
        display_contact()

if __name__ == "__main__":
    main()

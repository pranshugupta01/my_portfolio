import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image
from pathlib import Path
from streamlit_lottie import st_lottie

PAGE_TITLE = "Portfolio | PRANSHU GUPTA"
PAGE_ICON = ":wave:"

st.set_page_config(layout="wide",page_title=PAGE_TITLE, page_icon=PAGE_ICON)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "CV.pdf"
css_file = current_dir / "styles" / "main.css"
EMAIL = "gpranshu482@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/pranshugupta01",
    "GitHub": "https://github.com/pranshugupta01",
    "Twitter": "https://twitter.com/pranshu_gupta01"
}

def loadUrl(url):
    response=requests.get(url)
    if response.status_code!=200:
        return None
    return response.json()

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


coder= loadUrl("https://lottie.host/120d4a92-ef4c-4b54-8d52-f965069e45ba/L8meiSr4kh.json")
contact_us= loadUrl("https://lottie.host/50af316e-8f92-46c2-94d3-ca354369d1a4/5oPpKCzznQ.json")
profile_pic = loadUrl("https://lottie.host/29721b90-34fe-4554-bf91-0391f38ed6c9/kRoX3IZIw2.json")



col1,col2=st.columns((2,1))
with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hello World!!! :wave:")
            st.header("""I am PRANSHU GUPTA, """)
            st.subheader("Welcome To My Data-Driven Wonderland :)")
            st.write("##")
            st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
             )
            st.write("📫", EMAIL)
            st.write('\n')
            cols = st.columns(len(SOCIAL_MEDIA))
            for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
                cols[index].write(f"[{platform}]({link})")
            with col2:
             st_lottie(profile_pic,height=300)
st.write("##")


st.write("---")

with st.container():
    selected=option_menu(
        menu_title=None,
        options=['About','Projects','Contact'],
        icons=['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
        )
if selected =='About':
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st_lottie(coder)
        with col4:
            st.write('##')
            st.write("""## Unveiling My Arsenal 

Here's a glimpse of what I bring to the tech table:

🐍 Python Power

🔮 Machine Learning Magician

📊 Data Sorcery

🌐 Web Wizardry

⛓️ Blockchain Enthusiast

💻 Code Conjurer

🔧 Problem-Solving Sorcerer

🎨 Art of Visualization

🚀 Lifelong Learner

So, let's embark on a magical journey together and witness the wonders we can create with technology!
""")
            
    st.write("---")  
    with st.container():
        st.header('Work Experiences :')
        st.write("##")
        st.subheader("""
►R&D INTERN
    -Internship @ CodSoft
    -Time Period : Nov 2023 - Dec 2023 
    -Bengaluru, Karnataka, India · Remote
    -Research and contribution in development of an NLP-based survey system, enhancing data analysis capabilities for improved insights.
    -Developed a platform similar to Kaggle, featuring real-life datasets for collaborative data projects.
                     """)  
        st.write("##")
        st.write("##")
        st.subheader("""
►ML Intern
    -Internship @ LGM 
    - Time Period : June 2023 - Aug 2023 
    -Bengaluru, Karnataka, India · Hybrid
    - Developed an OCR module using OpenCV and Pytesseract to accurately extract medical report details, with a specific focus on extracting tabular data directly to a CSV.
    - Created a Flask API that accepts images as input and returns the extracted data in JSON format.
    - Deployed the FlaskAPI in AWS server.
    """)
        st.write("##")
        st.write("##")
        st.subheader("""
►FULL STACK DEVELOPER
    -Internship @ TELUSKO 
    -Time Period : Nov 2022 - Apr 2023 · (6 months)
    -Bengaluru, Karnataka, India · Hybrid
    -I have worked on several web development projects including the development of Decentralized Quiz app.
    -I have worked on a project of developing a Etherscan clone.
                     """)
    st.write("---")  
    st.write("---") 
#     with st.container():
#         st.header('Education :') 
#         st.subheader("""
# ►BMS COLLEGE OF ENGINEERING
#     -B.TECH @ ELECTRONICS AND COMMUNICATIONS ENGINEERING
#     -Time Period : 2021-2025
#     -Bengaluru, Karnataka, India 
#     - CGPA - 8.05
#     -I have participated in various hackathons, in which I developed various projects like SecureProX and BookWise (more details
#     about these projects are available in projects section) 
#                      """) 

with st.container():
    st.header('My Recent Research Papers :')
    st.write('##')
    st.subheader(f"[📄 Blockchain-Based Risk Management and Transparency in Loan Disbursements](https://ieeexplore.ieee.org/document/10392836)")
    st.write("The Loan Market faces significant fraud risks due to practices like reusing collateral and inadequate bank assessments. To combat this, a Blockchain framework using Multi-Signature smart contracts is proposed. It improves transparency, reduces fraud, and synchronizes loan records. Financial institutions must use these contracts for large loans, confirmed by a Risk Management Score, ensuring efficient record-keeping and regulatory compliance.")
    st.write("---")  
    st.write("---") 

if selected == 'Projects':
    with st.container():
        st.header('MY Projects')
        st.write('##')
        st.subheader(f"[🏆 CareConnect](https://github.com/pranshugupta01/CareConnect)")
        st.write(f"[CareConnect is a browser extension designed to provide compassionate support and assistance to users who may be going through difficult emotional times. The extension monitors the user's browsing activities and messages, detecting distress signals related to depression and suicidal thoughts. When necessary, the extension offers a chatbot for emotional support or reaches out to the user's loved ones or relevant helpline services to ensure their well-being.](https://github.com/pranshugupta01/CareConnect)")
        
        st.write('##')
        
        st.subheader(f"[🏆 SecureProX](https://github.com/pranshugupta01/SecureProX)")
        st.write(f"[This is a browser extension which promptly alerts users if a site is potentially a phishing site or contains malware, allowing them to make informed decisions before visiting any risky pages. Furthermore, it also displays the number of ads present on the linked site, giving users insight into the ad density and helping them avoid excessive advertisement bombardment.](https://github.com/pranshugupta01/SecureProX)")
        
        st.write('##')
       
        st.subheader(f"[🏆 BookWise](https://github.com/pranshugupta01/BookWise)")
        st.write(f"[It is a NGO-focused library management system powered by NextJS, Nodejs and MongoDB . It leverages machine learning to oer personalized book recommendations and includes a dedicated notes section. With ecient cataloging and user management, BookWise enhances the library experience for both students and administrators.](https://github.com/pranshugupta01/BookWise)")
        
        st.write('##')
       
        st.subheader(f"[🏆 DecentricQuiz](https://github.com/pranshugupta01/DecentricQuiz)")
        st.write(f"[A trivia app powered by blockchain. Participants submit ethers to enter, answer questions, and compete fairly. The smart contract ensures the winner takes it all, offering a secure and rewarding experience. Join the future of quizzes now!](https://github.com/pranshugupta01/DecentricQuiz)")

if selected=='Contact':
    st.header("Get In Touch")
    st.write('##')
    st.write('##')
    
    contact_form="""
  <form target="_blank" action="https://formsubmit.co/gpranshu482@gmail.com" method="POST">
     <input type="text" name="name" class="form-control" placeholder="Enter Your Full Name"  required>
     
     <input type="email" name="email" class="form-control" placeholder="Enter Your Email Address"  required>   
     
    <textarea type="message" placeholder="Enter Your Message" class="text_area" name="input_message"  rows="10" required></textarea>
     
    <button type="submit" class="btn" >Send</button>
       
  </form>
    """
    left_col, right_col= st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(contact_us, height=300)
        
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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
EMAIL = "gpranshu482@email.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/pranshugupta01",
    "GitHub": "https://github.com/pranshugupta01",
    "Twitter": "https://twitter.com/pranshu_gupta01",
    "Instagram": "https://www.instagram.com/pranshu_gupta01"
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


# project=Image.open('/images/Screenshot 2023-07-20 at 12.01.18 PM.png')/
coder= loadUrl("https://lottie.host/120d4a92-ef4c-4b54-8d52-f965069e45ba/L8meiSr4kh.json")
contact_us= loadUrl("https://lottie.host/50af316e-8f92-46c2-94d3-ca354369d1a4/5oPpKCzznQ.json")
profile_pic = loadUrl("https://lottie.host/29721b90-34fe-4554-bf91-0391f38ed6c9/kRoX3IZIw2.json")



col1,col2=st.columns((2,1))
with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hey Guys :wave:")
            st.title("My Portfolio Website")
            st.write(""" hello guys myself pranshu gupta i am from ece branch and currently doing an internship as a data scientist""")
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
            st.subheader('I Am Pranshu Gupta')
            st.title('Machine Learning')
            
    st.write("---")  
    with st.container():
        st.header('Education :') 
        st.subheader("""
►BMS COLLEGE OF ENGINEERING
    -B.TECH @ ELECTRONICS AND COMMUNICATIONS ENGINEERING
    -Time Period : 2022-2025
    -Bengaluru, Karnataka, India 
    -I have worked on several Blockchain projects including the development of smart contracts and decentralized application.
    I have worked on several Frontend projects and I am also a part of content writing team.I have worked on several Blockchain projects including the development of 
      smart contracts and decentralized application. I have worked on several Frontend projects and I am 
         also a part of content writing team.
                     """)
    st.write("---")  
    st.write("---")  
    with st.container():
        st.header('Work Experiences :')
        st.write("##")
        st.subheader("""
►DATA SCIENCE INTERN
    -Internship @ LETS GROW MORE 
    -Time Period : JULY 2023 - PRESENT · 3 months
    -Bengaluru, Karnataka, India · Hybrid
    -I have worked on several Blockchain projects including the development of smart contracts and decentralized application.
    I have worked on several Frontend projects and I am also a part of content writing team.I have worked on several Blockchain projects including the development of 
      smart contracts and decentralized application. I have worked on several Frontend projects and I am 
         also a part of content writing team.
                     """)  
        st.write("##")
        st.write("##")
        st.subheader("""
►JUNIOR BLOCKCHAIN DEVELOPER
    -Internship @ TELUSKO 
    -Time Period : Nov 2022 - Jun 2023 · 8 months
    -Bengaluru, Karnataka, India · Hybrid
    -I have worked on several Blockchain projects including the development of smart contracts and decentralized application.
    I have worked on several Frontend projects and I am also a part of content writing team.I have worked on several Blockchain projects including the development of 
      smart contracts and decentralized application. I have worked on several Frontend projects and I am 
         also a part of content writing team.
                     """)
        
                         
    st.write("---")  
    st.write("---")  
    
    with st.container():
        st.header('Skills :') 
        st.write("##")
        st.subheader("""
►Languages
   Python, Javascript, C , C++ , Solidity
                     """)
        st.write("##")
        st.write("##")
        st.subheader("""
►Libraries/Framework:
    React.js, Web3.js,TailwindCss, Numpy, Pandas, Matplotlib, TensorFlow, Scikit-learn, Flask
                     """)
        st.write("##")
        st.write("##")
        st.subheader("""
►Tools/Technologies:
    Linux, Git, Github, Jupyter Notebook, Bootstrap, Google Colab, Visual Studio Code, Pycharm
                     """)
  
if selected == 'Projects':
    with st.container():
        st.header('MY Projects')
        st.write('##')
        # col7,col8=st.columns((1,2))
        # with col7:
            # st.image(project)
        # with col8:
        st.subheader(f"[🏆 SecureProX](https://github.com/pranshugupta01/SecureProX)")
        st.write(f"[This is a browser extension which promptly alerts users if a site is potentially a phishing site or contains malware, allowing them to make informed decisions before visiting any risky pages. Furthermore, it also displays the number of ads present on the linked site, giving users insight into the ad density and helping them avoid excessive advertisement bombardment.](https://github.com/pranshugupta01/SecureProX)")
        st.write('##')
        # col9,col10=st.columns((1,2))
        # with col9:
        #     st.image(project)
        # with col10:
        #     st.subheader(f"[🏆 TherraBuddy](https://github.com/pranshugupta01/SecureProX)")
        #     st.write(f"[This is a browser extension which promptly alerts users if a site is potentially a phishing site or contains malware, allowing them to make informed decisions before visiting any risky pages. Furthermore, it also displays the number of ads present on the linked site, giving users insight into the ad density and helping them avoid excessive advertisement bombardment.](https://github.com/pranshugupta01/SecureProX)")
        # st.write('##')
        # col11,col12=st.columns((1,2))
        # with col11:
        #     st.image(project)
        # with col12:
        #     st.subheader(f"[🏆 Warpspeed](https://github.com/pranshugupta01/SecureProX)")
        #     st.write(f"[This is a browser extension which promptly alerts users if a site is potentially a phishing site or contains malware, allowing them to make informed decisions before visiting any risky pages. Furthermore, it also displays the number of ads present on the linked site, giving users insight into the ad density and helping them avoid excessive advertisement bombardment.](https://github.com/pranshugupta01/SecureProX)")
        # st.write('##')
        # col13,col14=st.columns((1,2))
        # with col13:
        #     st.image(project)
        # with col14:
        #     st.subheader(f"[🏆 Bookwise](https://github.com/pranshugupta01/SecureProX)")
        #     st.write(f"[This is a browser extension which promptly alerts users if a site is potentially a phishing site or contains malware, allowing them to make informed decisions before visiting any risky pages. Furthermore, it also displays the number of ads present on the linked site, giving users insight into the ad density and helping them avoid excessive advertisement bombardment.](https://github.com/pranshugupta01/SecureProX)")

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

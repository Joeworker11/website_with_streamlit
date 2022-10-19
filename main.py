import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="My website", page_icon=":computer:", layout="wide")

#adding side bar menu
with st.sidebar:
    selected=option_menu(
        menu_title = "Main Menu",
        options=["Home", "Projects", "Contacts"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,

    )

if selected == "Home":
    st.title(f"My Home Page")
if selected == "Projects":
    st.title(f"My Projects")
if selected == "Contacts":
    st.title(f"Contacts")



def load_lottieurl(url):
    r = requests.get(url) # lekérjük az URL-t
    if r.status_code != 200:  # ha a státuszkód nem 200, semmi se jöjjön vissza
        return None
    return r.json()  # ha bekérhető akkor a json térjen vissza
## using local CSS file(prewritten)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("C:/Users/User/PycharmProjects/websitewithpython/style/style.css")

#Load Assets
lottie_coding =load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_coding2=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_dzn3alb1.json")
lottie_coding3=load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_puze7ucu.json")
img_contact_form=Image.open("C:/Users/User/PycharmProjects/websitewithpython/images/streamlit1.png")
img_lottie_animation = Image.open("C:/Users/User/PycharmProjects/websitewithpython/images/streamlit2.png")

# header szekció
with st.container():
    st.subheader("Hi, I am Joseph :wave: ")
    st.title("A Full-Stack Web-developer from Hungary")
    st.write("An ambitious and motivated Python and Flutter expert, "
             "who is continously looking for the greatest challenges.")

    st.write("[For more here>](https://kutedoryu.hu/)")
    # nyíllal hiperlinket csinálhatunk

# mit csinálok?

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("What I do?")
        st.write("Graduated in Master’s Degree focused in Japanese Studies,"
                 " Specialization in Translation and Linguistics from Károli"
                 " Gáspár University of the Reformed Church in Hungary. For "
                 "years of research at the fields of Japanese, Okinawan dialects."
                 " Experienced Translator and Interpreter and Moderator at Asian "
                 "cultural events, with diverse but deep knowledge in automotive, "
                 "and catering and tour industry. Skilled in Microsoft Word, Microsoft"
                 " Excel, Power Point at advance level. Excellent communication / "
                 "negotiation / presentation skills in both Japanese and English. "
                 "Self-motivated in learning new languages such as Chinese and German. "
                 "Always eager to learn new skills and strategies. Current self-improvement "
                 "at the field of Web-development and programming (such as Flutter, C++) "
                 "and Python languages).")
        st.write("[My Youtube Chanel >](https://www.youtube.com/channel/UCBrJqqGacVLwvh59zqGMEAA)")

with left_column:
    st_lottie(lottie_coding, height=500, width=500,  key="coding")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is my mission?")
        st.write("My goal is to obtain a fully expertise at all fields of,"
                 " Web-Development, Softwaire-development to all kind of "
                 " devices, platforms and systems. I am also aiming to gain more"
                 "prestige in the world of programmers and developers. From my childhood"
                 "I used to have a dream: It was as simply as It could be: To able to"
                 "write, create, debux, fix, test, design, develop, use any kind of softwares."
                 "Most people have no clue at all, what are the main differences between scripting,"
                 " programming or hypertext languages at all, so my other mission is to teach people"
                 "who lack the knowledge or at least unable to get this kind of education in the wolrd."
                 "I for one completely believe that, when learning a new programming language, "
                 "not the syntax itself, but rather the problem solvic skills, and way of thinking"
                 "what really makes the programmer a fearful thinking living being. Thus I want to do"
                 "nothing less as well.")

with right_column:
    st_lottie(lottie_coding2, height=300, key="coding2")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("My personal life")
        st.write("In my free-time I am trying my best to ensure the life-work balance attitude,"
                 "Training daily and improving myself in the field of interpretation, translation,"
                 "mastering new teaching methods, learning new languages, picking up new hobbies."
                 "Whether it is a programming activity, a web-development hobby, an exhausting "
                 "day in the plant with hardworking Asian clients, it matters not, because I will"
                 "always achieve at my best level. In order to ensure my 100% will, I meditate everyday"
                 "reading new books in the fields of psychology, self-improvement, investment and logic."
                 "Since problem solving is almost a key to every kind of problem arising daily, I do  "
                 "pay attention to various kind of logical activities and problem solving exercises."
                 "Real life problems mostly can be found anywhere, but the key is to be able to incorporate"
                 "the learnt and accumulated skills. Applying is just one part of the journey, but being able"
                 "to make distinctions is what really makes a developer remarkably outstanding compared to"
                 "other competitors. Consistency is crucial and applying the newly learnt skills is a must. ")
        st.write("[My fighter blog >](https://made4fighters.com/blog/)")

with left_column:
    st_lottie(lottie_coding3, height=500, width=500, key="coding3")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))  # azt jelenti, hogy a text oszlop 2x akkora mint a másik
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it.
            In this tutorial, I'll show you exactly how to do it
            """
        )

        st.markdown("[Watch video here...](https://www.youtube.com/watch?v=72qbebvwxnY&ab_channel=DesignPilot)")

with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How to do a Machine Learning Web App with using Streamlit?")
        st.write(
            """
            Want to become professinal in Machine Learning with the combination of Python and Streamlit?
            In this video, I am going to show you how to master these skills and create your own web app.
    
            """
        )
        st.markdown("[Watch video here...](https://www.youtube.com/watch?v=Klqn--Mu2pE&ab_channel=PythonEngineer)")

# contact from

with st.container():
    st.write("---")
    st.header("Message me!")
    st.write("##")

    # documentation formsubmit.co (don't forget to change the e-mail adress!

    contact_form ="""
    <form action="https://formsubmit.co/eckertjozsef5@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="text" name="phone" placeholder="Your phone number" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column =st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()  # nem lesz semmi a jobb oldali oszlopban




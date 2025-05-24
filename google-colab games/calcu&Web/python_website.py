import streamlit as st

st.set_page_config(page_title="My Simple Python Website", page_icon="🌐", layout="centered")

st.title("🌟 Welcome to My Streamlit Website!")
st.write("This is a simple web app built using Streamlit. Let's explore some cool widgets!")

st.markdown("---")  

# About
st.header("👩‍💻 About Me")
st.write("I'm excited to create my first Streamlit web app. It's super easy and fun!")

st.image("https://via.placeholder.com/300x150.png?text=Streamlit+Website", caption="A Cool Placeholder Image")


st.header("📝 Tell Me About You")

name = st.text_input("What's your name?")
bio = st.text_area("Tell us a little about yourself:")
st.write("You can write anything here!")

language = st.selectbox(
    "Choose your favorite programming language:",
    ["Python", "JavaScript", "Java", "C++", "Other"]
)

agree = st.checkbox("I agree to the terms and conditions")

color = st.radio("Select your favorite color:", ["Red", "Green", "Blue"])

number = st.slider("Select a number between 1 and 100:", 1, 100, 50)

date = st.date_input("Select a date:")


if name:
    st.success(f"Hello, {name}! 👋 Thanks for visiting.")
    st.write(f"**About you:** {bio}")
    st.write(f"**Favorite language:** {language}")
    st.write(f"**Favorite color:** {color}")
    st.write(f"**Chosen number:** {number}")
    st.write(f"**Selected date:** {date}")
    st.write(f"**Terms agreed:** {'Yes' if agree else 'No'}")

st.markdown("---")

st.write("Thanks for trying out my Streamlit app! 🚀")
st.write("Feel free to explore and interact with the widgets above.")
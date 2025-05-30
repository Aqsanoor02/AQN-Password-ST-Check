import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    return strength, feedback

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength, feedback = check_password_strength(password)
    strength_percentage = (strength / 5) 

    st.progress(strength_percentage)

    if strength == 5:
        st.success("Your password is strong!")
    else:
        st.error("Your password could be stronger. Here are some tips:")
        for tip in feedback:
            st.write(f"- {tip}")

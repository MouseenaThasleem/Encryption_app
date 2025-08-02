
import streamlit as st
import base64

st.title("🔐 Text Encryption & Decryption App")

mode = st.selectbox("Choose Mode:", ["Encrypt", "Decrypt"])
method = st.selectbox("Choose Method:", ["Caesar Cipher", "Base64"])
text = st.text_area("Enter your text:")

shift = st.slider("Caesar Cipher Shift", 1, 25, 3)

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if encrypt else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

def process():
    if method == "Caesar Cipher":
        result = caesar_cipher(text, shift, encrypt=(mode=="Encrypt"))
    else:
        if mode == "Encrypt":
            result = base64.b64encode(text.encode()).decode()
        else:
            try:
                result = base64.b64decode(text.encode()).decode()
            except:
                result = "Invalid Base64 input!"
    st.text_area("Result:", result)

if st.button("Run"):
    process()

import streamlit as st
import base64 

# Judul halaman
st.title("3. Data dan Media Elements")

# Menampilkan identitas kelompok
st.subheader("Kelompok Visualisasi Data")
st.write("Anggota:")
st.write("1. Chika Karena - 0110222015")
st.write("2. Chery Renata - 0110222011")
st.write("3. Ira Pratiwi - 0110222162")

# ----------------------------
# Menampilkan Gambar
# ----------------------------
st.header("Menampilkan Gambar")

# Menampilkan gambar dari file lokal
st.image("asset/bunga-lily.jpg", caption="Bunga Lily", use_container_width=True)

import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")

# Panggil gambar kamu
add_local_background_image("asset/bg-pink.jpg")

import streamlit as st
from PIL import Image

original_image = Image.open("asset/bunga-lily.jpg")
# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))
# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)



import streamlit as st 

st.title("4. Buttons and Sliders")

# Menampilkan identitas kelompok
st.subheader("Kelompok Visualisasi Data")
st.write("Anggota:")
st.write("1. Chika Karena - 0110222015")
st.write("2. Chery Renata - 0110222011")
st.write("3. Ira Pratiwi - 0110222162")

st.title('Creating a Button')
#defining a button
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

st.title('Creating Radio Button')
#defining a radio button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Other'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female' :
    st.write('You have selected Female.')
else:
    st.write('You have selected Others.')


st.title('Creating Checkboxes')
st.write('Select your Hobies:')
#defining checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

st.title('Creating Dropdown')
hobby = st.selectbox('Choose yor hobby:',
('Books', 'Movies', 'Sports'))

st.title('Multi-Select')
hobbies = st.multiselect(
    'What are you Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Serie', 'Playing', 'Drawing'], 
    ['Reading', 'Playing'])

st.title("Download Button")
donw_btn = st.download_button(
    label="Download Image",
    data=open("asset/bunga-lily.jpg", "rb"),
    file_name="bunga.jpg",
    mime="image/jpg"
)

import time
st.title('Progress Bar')
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')


st.title('Spinner')
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')

import streamlit as st
import time

# ============================================================
# IDENTITAS PRAKTIKUM
# ============================================================
st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 4: Buttons & Sliders (Interaktif)")
st.markdown("""
**Anggota Kelompok:**
1. Chika Karena – 0110222015  
2. Chery Renata – 0110222011  
3. Ira Pratiwi – 01102222162  

Kelas: VISUALISASI DATA (7TI01)  
Dosen Pengampu: Pak IMAM HAROMAIN, S.Si., M.Kom. 
STT Terpadu Nurul Fikri
""")

# ============================================================
# BUTTON
# ============================================================
st.subheader("1. Button")
if st.button("Klik ini untuk menampilkan pesan"):
    st.success(" sehat-sehat anak semester 7!")

# ============================================================
# RADIO BUTTON
# ============================================================
st.subheader("2. Radio Button")
pilihan_bahasa = st.radio(
    "Pilih bahasa pemrograman favorit:",
    ("Python", "Java", "C++")
)
st.write("Bahasa yang kamu pilih adalah:", pilihan_bahasa)

# ============================================================
# CHECKBOX
# ============================================================
st.subheader("3. Checkbox")
if st.checkbox("Tampilkan informasi tambahan"):
    st.info("Checkbox sedang aktif ✅")

# ============================================================
# SELECTBOX
# ============================================================
st.subheader("4. SelectBox (Dropdown)")
jurusan = st.selectbox(
    "Pilih Program Studi:",
    ["Teknik Informatika", "Sistem Informasi", "Bisnis Digital"]
)
st.write("Program studi yang dipilih:", jurusan)

# ============================================================
# MULTISELECT
# ============================================================
st.subheader("5. Multiselect")
hobi = st.multiselect(
    "Pilih hobi:",
    ["Membaca", "Ngoding", "Gaming", "Traveling", "Nonton film"]
)
st.write("Hobimu adalah:", hobi)

# ============================================================
# SLIDER
# ============================================================
st.subheader("6. Slider")
nilai = st.slider("Atur nilai:", 0, 100, 50)
st.write("Nilai yang dipilih:", nilai)

# ============================================================
# DOWNLOAD BUTTON
# ============================================================
st.subheader("7. Download Button")
st.download_button(
    label="Download File chika,ira,chery",
    data="chika,ira,chery.",
    file_name="cic.txt"
)

# ============================================================
# PROGRESS BAR & SPINNER
# ============================================================
st.subheader("8. Progress Bar & Spinner (Loading Process)")

if st.button("Mulai proses loading"):
    with st.spinner("Sedang memproses..."):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)
    st.success("Proses selesai ✅")

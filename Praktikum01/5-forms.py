import streamlit as st 
import datetime
import pandas as pd 
st.title("Text Box")
name = st.text_input("Enter your Name")
st.write("Your Name is ", name)
name=st.text_input("Enter your Name", max_chars=10)
password = st.text_input("Enter your password", type='password')

input_text = st.text_area("Enter your Review")
st.write("""You entered: \n""",input_text)

st.number_input("Enter your Number")
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

st.title("Time")
st.time_input("Select Your Time")

st.title("Date")
st.date_input("Select Date")

st.title("Date")
st.date_input("Select Your Date", 
value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))

st.title("Select Color")
color_code = st.color_picker("Select your Color")
st.header(color_code)

st.title("CSV Data")
data_file = st.file_uploader("Upload CSV",type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type, "file_size":data_file.size}
        st.writer(file_details)
        df = pd.read.csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
submit_button = my_form.form_submit_button(label='Submit')
st.write(a)

import streamlit as st
import pandas as pd
from datetime import date
import os

# Judul halaman
st.title("📝 Form Input Data Pengguna")

# ======================
# 📋 FORM INPUT DATA
# ======================
with st.form("form_pengguna"):
    st.subheader("Isi Data Anda")

    # Kolom input teks
    nama = st.text_input("Nama Lengkap")

    # Kolom input angka
    usia = st.number_input("Usia", min_value=0, max_value=120, step=1)

    # Kolom input tanggal
    tanggal_lahir = st.date_input("Tanggal Lahir", min_value=date(1900, 1, 1))

    # Kolom upload file
    file_upload = st.file_uploader("Upload File (opsional)", type=["jpg", "png", "pdf", "docx"])

    # Tombol submit
    submitted = st.form_submit_button("Kirim Data")

# ======================
# ✅ PROSES SETELAH SUBMIT
# ======================
if submitted:
    if nama.strip() == "":
        st.warning("⚠️ Nama tidak boleh kosong!")
    else:
        st.success("✅ Data berhasil dikirim!")
        st.write("### Data yang Anda masukkan:")
        st.write(f"**Nama:** {nama}")
        st.write(f"**Usia:** {usia} tahun")
        st.write(f"**Tanggal Lahir:** {tanggal_lahir.strftime('%d %B %Y')}")

        # Simpan file upload ke folder uploads
        if file_upload is not None:
            folder_path = "uploads"
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, file_upload.name)

            with open(file_path, "wb") as f:
                f.write(file_upload.read())

            st.write(f"**Nama File:** {file_upload.name}")
            st.success("📁 File berhasil diunggah dan disimpan di folder 'uploads'")
        else:
            file_path = "Tidak ada file"
            st.write("**File:** Tidak ada file diunggah.")

        # -----------------------------
        # 💾 Simpan ke file CSV
        # -----------------------------
        data = pd.DataFrame({
            "Nama": [nama],
            "Usia": [usia],
            "Tanggal Lahir": [tanggal_lahir],
            "Nama File": [file_upload.name if file_upload else "Tidak ada"]
        })

        if not os.path.exists("data_pengguna.csv"):
            data.to_csv("data_pengguna.csv", index=False)
        else:
            data.to_csv("data_pengguna.csv", mode='a', header=False, index=False)

        st.success("💾 Data berhasil disimpan ke file `data_pengguna.csv`!")

# ======================
# 📊 TAMPILKAN DATA
# ======================
st.subheader("📋 Data Pengguna yang Sudah Masuk")

if os.path.exists("data_pengguna.csv"):
    df = pd.read_csv("data_pengguna.csv")
    st.dataframe(df)

    # Tampilkan file yang sudah diupload
    st.write("### 📂 File yang Telah Diupload:")
    upload_folder = "uploads"
    if os.path.exists(upload_folder):
        files = os.listdir(upload_folder)
        if files:
            for file in files:
                st.write(f"- {file}")
        else:
            st.info("Belum ada file yang diupload.")
else:
    st.info("Belum ada data yang tersimpan.")

# ======================
# 🧹 FITUR HAPUS DATA
# ======================
st.divider()
st.subheader("🧹 Hapus Semua Data")

if st.button("Hapus Semua Data dari CSV dan Folder Uploads"):
    if os.path.exists("data_pengguna.csv"):
        os.remove("data_pengguna.csv")
    if os.path.exists("uploads"):
        for file in os.listdir("uploads"):
            os.remove(os.path.join("uploads", file))
        os.rmdir("uploads")
    st.success("🗑️ Semua data dan file berhasil dihapus!")
import streamlit as st 
import pandas as pd 
import numpy as np 
#define random values in a dataframe using pandas and numpy

st.subheader("Bagian 1 : Data Frames")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
st.dataframe(df)

import streamlit as st 
import pandas as pd 
import numpy as np 
#define random values in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
st.dataframe(df.style.highlight_min(axis=0))

import streamlit as st
import pandas as pd

# ============================================================
# HEADER & INFORMASI KELOMPOK
# ============================================================
st.title("Praktikum Visualisasi Data")
st.subheader("Segmen 2: Elemen Data")
st.markdown("""
**Daftar Anggota Kelompok:**  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162  

Kelas: VISUALISASI DATA (7TI01)  
Dosen Pengampu: Pak IMAM HAROMAIN, S.Si., M.Kom. 
STT Terpadu Nurul Fikri
""")

# ============================================================
# DATAFRAME INTERAKTIF
# ============================================================
st.subheader("Tampilan DataFrame Interaktif")

data = {
    "Nama": ["Chika", "Chery", "Ira"],
    "Nilai": [90, 85, 95]
}
df = pd.DataFrame(data)

# Menampilkan dataframe interaktif
st.dataframe(df)

# ============================================================
# TABEL STATIS
# ============================================================
st.subheader("Tabel Statis")
st.table(df)

# ============================================================
# METRICS
# ============================================================
st.subheader("Contoh Metrics")
st.metric(label="Peningkatan Nilai", value="90%", delta="5%")

# ============================================================
# WRITE / MAGIC FUNCTION
# ============================================================
st.subheader("Demonstrasi st.write() & Magic Function")

st.write("Contoh penggunaan **st.write()** untuk menampilkan teks dan dataframe:")
st.write(df)

"Contoh Magic Function — langsung menampilkan teks tanpa st.write()"

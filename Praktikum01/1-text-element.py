#import library yang dibutuhkan
import streamlit as st

#BAGIAN 1 - text element
#header - untuk membuat tulisan header
st.header("ini header")
st.subheader("ini sub header")
st.text("ini teks biasa tanpa format") #teks biasa
st.markdown("*ini teks blod* dan ini teks italic")
st.caption("ini caption") #biasanya dibawah gambar untuk penjelasan
st.markdown("""
- ini baris 1 
- ini menggunakan markdown multi baris            
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini mengguanakan markdown multibaris                  
""")

#coba mandiri
#tulisakan :
# 1. Judul pakai pratikumc pakai header
# 2. bagian pratikum pakai subheader
# 3. nama lengkap anggota - nim pakai markdown multibaris

st.header("Pratikum 1 Visualisasi Datas")
st.subheader("Bagian 1 : Teks Element")
st.markdown("""
1. Chika Karena -             
2. Chery Renata - 
3. Ira Pratiwi - 0110222162
""")


#BAGIAN 2 - Menampilkan rumus (LaTex)
st.header("Displaying Latex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta''') #rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus kuadrat binomonal

#BAGIAN 3 - Menampilkan kode program
st.header("Displaying Code")
st.subheader("Python Code")

#Simpan ke variabel
code = '''
def hello ():
    print("Hello, Streamlit!")
    '''

# st.code() untuk nampilin potongan kode dengan format rapi dan syntax highligtting
st.code(code, language='python')

st.subheader("Java Code")
st.code(""""
    public class GFG{
        public static void main(string arg[]){
            system.out.printIn("Hello World!");
        }
    }
""", language='java')
# Fungsi st.code() bisa digunakan untuk bahasa pemrograman lain 
# seperti java, javascript, c++, HTML. DLL

st.subheader("JavaScript code")
st.code("""
<script>
try {
    addalert("Wellcome  guest!); // kesalahan ketik (addalaert)
    sengaja dibuat untuk menimbulkan eror
}
catch(err) {
    document.getElementById ("demo").innerHTML = err.message; //
    menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>           
""", language='javascript')
# kode ini menunjukan contoh bagaimana menangani eror (exception) di javascript.
#Hasilnya tidak dijalankan di streamlit, tapi ditampilan sebagai contoh code 

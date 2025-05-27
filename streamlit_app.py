import streamlit as st

st.title("Selamat Datang di Web Adit")
st.write("ngodingseru bersama Aditya Harun")

st.title("Saksikanlah Pertandingan kkjahe vs aziz gagak") 
st.image("WhatsApp Image 2025-05-26 at 20.48.22.jpeg", width=200)

st.title("Buronan!!!") 
st.write("Foto tersebut adalah foto pelaku maling di daerah gasibu, dia mengambil sebuah dompet di daerah gasibu di saat ibu itu sedang mengeluarkan HP") 

st.image("IMG-20250524-WA0118.jpg", width=200) 

st.title("Pelaku Bom Bunuh Diri") 
st.write("motif bom bunuh diri belum diketahuinya oleh polisi setempat, namun menurut keluarga pelaku tersebut sakit hati karena diputusin oleh kekasihnya sendiri") 

st.image("IMG-20250524-WA0069.jpg", width=300) 

st.title("Korban Bullying") 
st.write("Foto diatas adalah korban bullying di sman monokotobo, menurut teman kelasnya dia trauma karena di bully dan tidak masuk sekoalah") 

st.image("IMG-20250519-WA0096.jpg", width=300) 

st.title("Pandoy M200") 
st.header("Harga m200 tiap toko") 
angka = st.number_input("70:", value=0, step=1) 

if(angka % 2) == 0:
  st.write(f"{200,350,400} adalah harga Centaurus di lodaya") 
else:
  st.write(f"{300,325,450} adalah harga Centaurus di siliwangi") 

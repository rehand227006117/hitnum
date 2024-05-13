import streamlit as st


st.set_page_config(
    page_title = "Aplikasi Hitung Anum"

)

st.header("Cara Penggunaan ")

st.subheader("Aplikasi Hitung Anum ")
with st.container():
    st.write("Aplikasi Hitnum merupakan kalkulator untuk menghitung dan menampilkan hasil iterasi metode terbuka dan tertutup. Aplikasi Hitung Anum ini adalah aplikasi yang digunakan untuk menghitung solusi akar x untuk berbagai metode baik metode terbuka dan metode tertutup pada SPNL")
    st.write("Tujuan aplikasi ini untuk mengetahui solusi terbaik dengan cara membandingkan antara dua metode  baik terbuka dan tertutup")


st.write("Cara penggunaan pada aplikasi : ")
st.write("1. Pilih metode Terbuka, Tertutup, atau Campuran")
st.write("2. Masukkan Persamaan")
st.write("3. Masukkan batas bawah dan batas atas.")
st.write("4. Masukkan Toleransi error")
st.write("Lalu hasil iterasi akan muncul beserta grafik dan kesimpulan perbandingannya.")

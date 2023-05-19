import streamlit as st

st.title("APLIKASI PENGHITUNG MOLALITAS DAN FRAKSI MOL ZAT")


st.write("APA ITU MOLALITAS?")
st.write("Molalitas adalah ukuran konsentrasi dari suatu zat terlarut dalam suatu larutan, jumlah zat, dan jumlah massa tertentu dari pelarut. Zat terlarut adalah zat yang dilarutkan ke dalam pelarut sedangkan pelarut adalah suatu zat yang dipakai untuk melarutkan zat terlarut. Molalitas dinyatakan sebagai jumlah mol suatu zat terlarut di dalam 1000 gram pelarut. Satuan untuk molalitas yaitu m.")


st.write("APA ITU FRAKSI MOL?")
st.write("fraksi mol merupakan bagian dari zat terlarut atau zat pelarut dari mol totalnya.")

         

st.write('Rumus Menghitung Molalitas Suatu Larutan')
                                    
st.latex(r'''
    \left(\frac{mol}{massa}\right)''')


st.write('Rumus Menghitung Fraksi Mol Suatu Larutan')
st.latex(r'''
    \left(\frac{mol(A)}{Jumlah mol total}\right)''')

st.write('A = zat terlarut atau zat pelarut')

st.write("APLIKASI PENGHITUNG MOLALITAS DAN FRAKSI MOL")


pilihan = st.selectbox('Pilih jenis perhitungan', ["molalitas","fraksi mol"])
if pilihan == "molalitas" :
    num1 = st.number_input('mol zat terlarut : ')
    num2 = st.number_input('massa zat pelarut : ')
    st.write()


    st.write('Hasil dari',num1,'/',num2,'=',round(num1/num2,2))


if pilihan == "fraksi mol" :
    num3 = st.number_input('mol zat A : ')
    num4 = st.number_input('Jumlah mol total pelarut dan pelarut : ')
    st.write()


    st.write('Hasil dari',num3,'/',num4,'=',round(num3/num4,2))
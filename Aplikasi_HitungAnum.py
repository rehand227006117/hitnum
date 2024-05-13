import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Aplikasi HitNum")
with st.container():
    st.write("Aplikasi Hitnum merupakan kalkulator untuk menghitung dan menampilkan hasil iterasi metode terbuka dan tertutup")
    st.write("Tujuan aplikasi ini untuk mengetahui solusi terbaik dengan cara membandingkan antara dua metode  baik terbuka dan tertutup")

menentukan1  = st.selectbox("Silahkan pilih metode", ["None", "Metode Terbuka", "Metode Tertutup", "Metode Campuran"])

#METODE TERBUKA
def biseksi_regula_falsi():
    
    if menentukan1 == ("Metode Terbuka") :
        menentukan2  = st.selectbox("Jenis metode", ["None", "Biseksi & Regula Falsi"])
        if menentukan2 == "Biseksi & Regula Falsi" :
            f_input = st.text_input("Input function f(x)", "x**3 - x - 1")
            f = lambda x: eval(f_input)

            col1, col2, col3 = st.columns(3)
            with col1:
                a = st.number_input("Batas Bawah (a)", value=0.0, format="%.2f")
            with col2:
                b = st.number_input("Batas Atas (b), ",  value=0.0, format="%.2f")
            with col3:    
                e = st.number_input("Tolerance error (e)",  value=0.0, format="%.4f")

    def bisection(f, a, b, e, N=100):
        data_biseksi = []
        ya = f(a)  
        yb = f(b)  
        
        if ya * yb >= 0:
            print("Metode biseksi gagal: Tanda dari f(a) dan f(b) harus berbeda.")
            return None, None
        
        for i in range(N):
            row = {}
            row["Iteration"] = i
            row["a"] = a
            row["b"] = b
            row["f(a)"] = ya
            row["f(b)"] = yb
            
            c = (a + b) / 2
            yc = f(c)
            row["c"] = c
            row["f(c)"] = yc

            if abs(yc) < e:
                row["Result"] = c
        
                return c, pd.DataFrame(data_biseksi + [row])

            if ya * yc < 0:
                b = c
                yb = yc
            else:
                a = c
                ya = yc
            row["Result"] = "-"
            data_biseksi.append(row)

        print("Metode biseksi gagal: Jumlah iterasi maksimum tercapai.")
        return None, pd.DataFrame(data_biseksi)
    
    def regula_falsi(f, a, b, e, N=100):
        data_regula_falsi = []
        ya = f(a)  
        yb = f(b)  
        
        
        for i in range(N):
            row = {}
            row["Iteration"] = i
            row["a"] = a
            row["b"] = b
            row["f(a)"] = f(a)
            row["f(b)"] = f(b)
            
            c = b - (((b - a) * f(b) )/ (f(b) - f(a)))  
            yc = f(c)
            row["c"] = c
            row["f(c)"] = yc

            if abs(yc) < e:
                row["Result"] = c
                
                return c, pd.DataFrame(data_regula_falsi + [row])

            if ya * yc < 0:
                b = c
                yb = yc
            else:
                a = c
                ya = yc
            row["Result"] = "-"
            data_regula_falsi.append(row)

        print("Metode Regula Falsi gagal: Jumlah iterasi maksimum tercapai.")
        return None, pd.DataFrame(data_regula_falsi)
        

    
    def plot_iteration_b(data_biseksi, data_regula_falsi: pd.DataFrame):
        fig, ax = plt.subplots()
        ax.plot(data_biseksi["Iteration"], data_biseksi["a"], label="biseksi")
        ax.plot(data_regula_falsi["Iteration"], data_regula_falsi["a"], label="regula_falsi")
        ax.legend()
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Value")
        st.pyplot(fig)

    if menentukan2 ==  "Biseksi & Regula Falsi":
        if st.button("Submit"):
            st.header("Hasil Metode Biseksi : ")
            result1, table1 = bisection(f, a, b, e)
            st.table(table1)
            st.write(f"Akar terletak di x = {result1}")

            st.header("Hasil Metode Regula Falsi : ")
            result2, table2 = regula_falsi(f, a, b, e)
            st.table(table2)
            st.write(f"Akar terletak di x = {result2:.6f}")

            plot_iteration_b(table1, table2)
           
            
            
            st.write("---")  
            st.header("Kesimpulan : ")
        
            if table1.shape[0]> table2.shape[0]:
                st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunakan metode")
                st.subheader("Regula Falsi")
            if table1.shape[0]< table2.shape[0]:
                st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunnakan metode ")
                st.subheader("Biseksi")
            if table1.shape[0]== table2.shape[0]:
                st.write("Kedua Metode adalah solusi terbaik")
# METODE TERTUTUP
def newton_raphson_secant():
    if menentukan1 == ("Metode Tertutup") :
        menentukan2  = st.selectbox("Jenis metode", ["None", "Newton Raphson & Secant"])
        if menentukan2 == "Newton Raphson & Secant" :
            f_input = st.text_input("Input Fungsi f(x)", "x**3 - x - 1")
            f_input_turunan = st.text_input("Input fungsi  f'(x)")
            f = lambda x: eval(f_input)
            df = lambda x: eval(f_input_turunan)

            col1, col2, col3 = st.columns(3)
            with col1:
                a = st.number_input("Batas Bawah (a)", value=0.0, format="%.2f")
            with col2:
                b = st.number_input("Batas Atas (b), ",  value=0.0, format="%.2f")
            with col3:    
                e = st.number_input("Tolerance error (e)",  value=0.0, format="%.4f")
    
    def secant(f, a, b, e, N=100):
        data_secant = []

        for i in range(N):
            row = {}
            row["Iteration"] = i
            row["a"] = a
            row["b"] = b
            row["f(b)"] = f(b)
            if abs(f(b)) < e:
                row["Result"] = b
                return b, pd.DataFrame(data_secant+[row])
            c = b - f(b) * (b - a) / (f(b) - f(a))
            a = b
            b = c
            row["Result"] = "-"
            data_secant.append(row)
        return b, pd.DataFrame(data_secant)
    
    def newton_raphson(f, df, a, e,  N=100):
        data_newton_raphson = []
        for i in range(N):
            row = {}
            row["Iteration"] = i
            row["a"] = a
            row["f(a)"] = f(a)
            row["f'(a)"] = df(a)

            if abs(f(a)) < e:
                row["Result"] = a
                return a, pd.DataFrame(data_newton_raphson + [row])

            b = a - f(a) / df(a)
            a = b
            row["Result"] = "-"
            data_newton_raphson.append(row)
        return a, pd.DataFrame(data_newton_raphson)

    def plot_iteration_b(data_newton_raphson, data_secant: pd.DataFrame):
        fig, ax = plt.subplots()
        ax.plot(data_newton_raphson["Iteration"], data_newton_raphson["a"], label="ewton_raphson")
        ax.plot(data_secant["Iteration"], data_secant["a"], label="secant")
        ax.legend()
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Value")
        st.pyplot(fig)
    
    if menentukan2 ==  "Newton Raphson & Secant":
        if st.button("Submit"):
            st.header("Hasil Metode Newton Raphson : ")
            result1, table1 = newton_raphson(f,df, a, e)
            st.table(table1)
            st.write(f"Akar terletak di x = {result1:.6f}")

            st.header("Hasil Metode Secant : ")
            result2, table2 = secant(f, a, b, e)
            st.table(table2)
            st.write(f"Akar terletak di x = {result2:.6f}")

            st.write("---")  
            plot_iteration_b(table1, table2)
            st.header("Kesimpulan : ")
        
            if table1.shape[0] < table2.shape[0]:
                st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunakan metode")
                st.subheader("Newton Raphson")
            if table1.shape[0]> table2.shape[0]:
                st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunnakan metode ")
                st.subheader("Secant")
            if table1.shape[0]== table2.shape[0]:
                st.write("Kedua Metode adalah solusi terbaik")


#METODE CAMPURAN
def metode_campuran():
    menentukan2  = st.selectbox("Jenis metode", ["None", "Biseksi & Secant" , "Regula Falsi & Secant", "Biseksi & Newton Raphson","Regula Falsi & Newton Raphson"])
    def biseksi_secant():
        if menentukan1 == ("Metode Campuran") :
            if menentukan2 == "Biseksi & Secant" :
                f_input = st.text_input("Input function f(x)", "x**3 - x - 1")
                f = lambda x: eval(f_input)

                col1, col2, col3 = st.columns(3)
                with col1:
                    a = st.number_input("Batas Bawah (a)", value=0.0, format="%.2f")
                with col2:
                    b = st.number_input("Batas Atas (b), ",  value=0.0, format="%.2f")
                with col3:    
                    e = st.number_input("Tolerance error (e)",  value=0.0, format="%.4f")

        def bisection(f, a, b, e, N=100):
            data_biseksi = []
            ya = f(a)  
            yb = f(b)  
            
            if ya * yb >= 0:
                print("Metode biseksi gagal: Tanda dari f(a) dan f(b) harus berbeda.")
                return None, None
            
            for i in range(N):
                row = {}
                row["Iteration"] = i
                row["a"] = a
                row["b"] = b
                row["f(a)"] = ya
                row["f(b)"] = yb
                
                c = (a + b) / 2
                yc = f(c)
                row["c"] = c
                row["f(c)"] = yc

                if abs(yc) < e:
                    row["Result"] = c
            
                    return c, pd.DataFrame(data_biseksi + [row])

                if ya * yc < 0:
                    b = c
                    yb = yc
                else:
                    a = c
                    ya = yc
                row["Result"] = "-"
                data_biseksi.append(row)

            print("Metode biseksi gagal: Jumlah iterasi maksimum tercapai.")
            return None, pd.DataFrame(data_biseksi)
        
        def secant(f, a, b, e, N=100):
            data_secant = []

            for i in range(N):
                row = {}
                row["Iteration"] = i
                row["a"] = a
                row["b"] = b
                row["f(b)"] = f(b)
                if abs(f(b)) < e:
                    row["Result"] = b
                    return b, pd.DataFrame(data_secant+[row])
                c = b - f(b) * (b - a) / (f(b) - f(a))
                a = b
                b = c
                row["Result"] = "-"
                data_secant.append(row)
            return b, pd.DataFrame(data_secant)
        
        def plot_iteration_b(data_biseksi, data_secant: pd.DataFrame):
            fig, ax = plt.subplots()
            ax.plot(data_biseksi["Iteration"], data_biseksi["a"], label="biseksi")
            ax.plot(data_secant["Iteration"], data_secant["a"], label="secant")
            ax.legend()
            ax.set_xlabel("Iteration")
            ax.set_ylabel("Value")
            st.pyplot(fig)

        if menentukan2 ==  "Biseksi & Secant":
            if st.button("Submit"):
                st.header("Hasil Metode Biseksi : ")
                result1, table1 = bisection(f, a, b, e)
                st.table(table1)
                st.write(f"Akar terletak di x = {result1:.6f}")

                st.header("Hasil Metode Secant : ")
                result2, table2 = secant(f, a, b, e)
                st.table(table2)
                st.write(f"Akar terletak di x = {result2:.6f}")

                plot_iteration_b(table1, table2)
            
                
                
                st.write("---")  
                st.header("Kesimpulan : ")
            
                if table1.shape[0]> table2.shape[0]:
                    st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunakan metode")
                    st.subheader("Secant")
                if table1.shape[0]< table2.shape[0]:
                    st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunnakan metode ")
                    st.subheader("Biseksi")
                if table1.shape[0]== table2.shape[0]:
                    st.write("Kedua Metode adalah solusi terbaik")


    def biseksi_newton_raphson():
        
        if menentukan1 == ("Metode Campuran") :
            if menentukan2 == "Biseksi & Newton Raphson" :
                f_input = st.text_input("Input function f(x)", "x**3 - x - 1")
                f_input_turunan = st.text_input("Input fungsi  f'(x)")
                f = lambda x: eval(f_input)
                df = lambda x: eval(f_input_turunan)

                col1, col2, col3 = st.columns(3)
                with col1:
                    a = st.number_input("Batas Bawah (a)", value=0.0, format="%.2f")
                with col2:
                    b = st.number_input("Batas Atas (b), ",  value=0.0, format="%.2f")
                with col3:    
                    e = st.number_input("Tolerance error (e)",  value=0.0, format="%.4f")

        def bisection(f, a, b, e, N=100):
            data_biseksi = []
            ya = f(a)  
            yb = f(b)  
            
            if ya * yb >= 0:
                print("Metode biseksi gagal: Tanda dari f(a) dan f(b) harus berbeda.")
                return None, None
            
            for i in range(N):
                row = {}
                row["Iteration"] = i
                row["a"] = a
                row["b"] = b
                row["f(a)"] = ya
                row["f(b)"] = yb
                
                c = (a + b) / 2
                yc = f(c)
                row["c"] = c
                row["f(c)"] = yc

                if abs(yc) < e:
                    row["Result"] = c
            
                    return c, pd.DataFrame(data_biseksi + [row])

                if ya * yc < 0:
                    b = c
                    yb = yc
                else:
                    a = c
                    ya = yc
                row["Result"] = "-"
                data_biseksi.append(row)

            print("Metode biseksi gagal: Jumlah iterasi maksimum tercapai.")
            return None, pd.DataFrame(data_biseksi)
        
        def newton_raphson(f, df, a, e,  N=100):
            data_newton_raphson = []
            for i in range(N):
                row = {}
                row["Iteration"] = i
                row["a"] = a
                row["f(a)"] = f(a)
                row["f'(a)"] = df(a)

                if abs(f(a)) < e:
                    row["Result"] = a
                    return a, pd.DataFrame(data_newton_raphson + [row])

                hasil = a - f(a) / df(a)
                a = hasil
                row["Result"] = "-"
                data_newton_raphson.append(row)
            return a, pd.DataFrame(data_newton_raphson)
        
        def plot_iteration_b(data_biseksi, data_newton_raphson: pd.DataFrame):
            fig, ax = plt.subplots()
            ax.plot(data_biseksi["Iteration"], data_biseksi["a"], label="biseksi")
            ax.plot(data_newton_raphson["Iteration"], data_newton_raphson["a"], label="newton_raphson")
            ax.legend()
            ax.set_xlabel("Iteration")
            ax.set_ylabel("Value")
            st.pyplot(fig)

        if menentukan2 ==  "Biseksi & Newton Raphson":
            if st.button("Submit"):
                st.header("Hasil Metode Biseksi : ")
                result1, table1 = bisection(f, a, b, e)
                st.table(table1)
                st.write(f"Akar terletak di x = {result1:.6f}")

                st.header("Hasil Metode Newton Raphson : ")
                
                result2, table2 = newton_raphson(f,df, a, e)
                st.table(table2)
                st.write(f"Akar terletak di x = {result2:.6f}")

                plot_iteration_b(table1, table2)
            
                
                st.write("---")  
                st.header("Kesimpulan : ")
            
                if table1.shape[0]> table2.shape[0]:
                    st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunakan metode")
                    st.subheader("Newton Raphson")
                if table1.shape[0]< table2.shape[0]:
                    st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunnakan metode ")
                    st.subheader("Biseksi")
                if table1.shape[0]== table2.shape[0]:
                    st.write("Kedua Metode adalah solusi terbaik")
                    
    def regula_falsi_newton_raphson():
        
        if menentukan1 == ("Metode Campuran") :
            if menentukan2 == "Regula Falsi & Newton Raphson" :
                f_input = st.text_input("Input function f(x)", "x**3 - x - 1")
                f_input_turunan = st.text_input("Input fungsi  f'(x)")
                f = lambda x: eval(f_input)
                df = lambda x: eval(f_input_turunan)
            
                col1, col2, col3 = st.columns(3)
                with col1:
                    a = st.number_input("Batas Bawah (a)", value=0.0, format="%.2f")
                with col2:
                    b = st.number_input("Batas Atas (b), ",  value=0.0, format="%.2f")
                with col3:    
                    e = st.number_input("Tolerance error (e)",  value=0.0, format="%.4f")

        def newton_raphson(f, df, a, e,  N=100):
            data_newton_raphson = []
            for i in range(N):
                row = {}
                row["Iteration"] = i
                row["a"] = a
                row["f(a)"] = f(a)
                row["f'(a)"] = df(a)

                if abs(f(a)) < e:
                    row["Result"] = a
                    return a, pd.DataFrame(data_newton_raphson + [row])

                hasil = a - f(a) / df(a)
                a = hasil
                row["Result"] = "-"
                data_newton_raphson.append(row)
            return a, pd.DataFrame(data_newton_raphson)

        
        def regula_falsi(f, a, b, e, N=100):
            data_regula_falsi = []
            ya = f(a)  
            yb = f(b)  
            
            
            for i in range(N):
                row = {}
                row["Iteration"] = i
                row["a"] = a
                row["b"] = b
                row["f(a)"] = f(a)
                row["f(b)"] = f(b)
                
                c = b - (((b - a) * f(b) )/ (f(b) - f(a)))  
                yc = f(c)
                row["c"] = c
                row["f(c)"] = yc

                if abs(yc) < e:
                    row["Result"] = c
                    
                    return c, pd.DataFrame(data_regula_falsi + [row])

                if ya * yc < 0:
                    b = c
                    yb = yc
                else:
                    a = c
                    ya = yc
                row["Result"] = "-"
                data_regula_falsi.append(row)

            print("Metode Regula Falsi gagal: Jumlah iterasi maksimum tercapai.")
            return None, pd.DataFrame(data_regula_falsi)
        
        def plot_iteration_b(data_newton_raphson, data_regula_falsi: pd.DataFrame):
            fig, ax = plt.subplots()
            ax.plot(data_newton_raphson["Iteration"], data_newton_raphson["a"], label="Newton Raphson")
            ax.plot(data_regula_falsi["Iteration"], data_regula_falsi["a"], label="Regula Falsi")
            ax.legend()
            ax.set_xlabel("Iteration")
            ax.set_ylabel("Value")
            st.pyplot(fig)

        if menentukan2 ==  "Regula Falsi & Newton Raphson":
            if st.button("Submit"):
                st.header("Hasil Metode Regula Falsi : ")
                result1, table1 = regula_falsi(f, a, b, e)
                st.table(table1)
                st.write(f"Akar terletak di x = {result1:.6f}")
                st.header("Hasil Metode Newton Raphson : ")
                result2, table2 = newton_raphson(f,df, a, e)
                st.table(table2)
                st.write(f"Akar terletak di x = {result2:.6f}")

                plot_iteration_b(table1, table2)
            
                st.write("---")  
                st.header("Kesimpulan : ")
            
                if table1.shape[0]> table2.shape[0]:
                    st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunakan metode")
                    st.subheader("Newton Raphson")
                if table1.shape[0]< table2.shape[0]:
                    st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunnakan metode ")
                    st.subheader("Regula Falsi")
                if table1.shape[0]== table2.shape[0]:
                    st.write("Kedua Metode adalah solusi terbaik")

    def regula_falsi_secant():
        if menentukan1 == ("Metode Campuran") :
            if menentukan2 == "Regula Falsi & Secant" :
                f_input = st.text_input("Input function f(x)", "x**3 - x - 1")
                f = lambda x: eval(f_input)

                col1, col2, col3 = st.columns(3)
                with col1:
                    a = st.number_input("Batas Bawah (a)", value=0.0, format="%.2f")
                with col2:
                    b = st.number_input("Batas Atas (b), ",  value=0.0, format="%.2f")
                with col3:    
                    e = st.number_input("Tolerance error (e)",  value=0.0, format="%.4f")

        def regula_falsi(f, a, b, e, N=100):
            data_regula_falsi = []
            ya = f(a)  
            yb = f(b)  
            
            
            for i in range(N):
                row = {}
                row["Iteration"] = i
                row["a"] = a
                row["b"] = b
                row["f(a)"] = f(a)
                row["f(b)"] = f(b)
                
                c = b - (((b - a) * f(b) )/ (f(b) - f(a)))  
                yc = f(c)
                row["c"] = c
                row["f(c)"] = yc

                if abs(yc) < e:
                    row["Result"] = c
                    
                    return c, pd.DataFrame(data_regula_falsi + [row])

                if ya * yc < 0:
                    b = c
                    yb = yc
                else:
                    a = c
                    ya = yc
                row["Result"] = "-"
                data_regula_falsi.append(row)


            return None, pd.DataFrame(data_regula_falsi)
        
        def secant(f, a, b, e, N=100):
            data_secant = []

            for i in range(N):
                row = {}
                row["Iteration"] = i
                row["a"] = a
                row["b"] = b
                row["f(b)"] = f(b)
                if abs(f(b)) < e:
                    row["Result"] = b
                    return b, pd.DataFrame(data_secant+[row])
                c = b - f(b) * (b - a) / (f(b) - f(a))
                a = b
                b = c
                row["Result"] = "-"
                data_secant.append(row)
            return b, pd.DataFrame(data_secant)
        
        def plot_iteration_b(data_secant, data_regula_falsi: pd.DataFrame):
            fig, ax = plt.subplots()
            ax.plot(data_secant["Iteration"], data_secant["a"], label="Secant")
            ax.plot(data_regula_falsi["Iteration"], data_regula_falsi["a"], label="Regula Falsi")
            ax.legend()
            ax.set_xlabel("Iteration")
            ax.set_ylabel("Value")
            st.pyplot(fig)

        if menentukan2 ==  "Regula Falsi & Secant":
            if st.button("Submit"):
                st.header("Hasil Metode Regula Falsi : ")
                result1, table1 = regula_falsi(f, a, b, e)
                st.table(table1)
                st.write(f"Akar terletak di x = {result1:.6f}")

                st.header("Hasil Metode Secant : ")
                result2, table2 = secant(f, a, b, e)
                st.table(table2)
                st.write(f"Akar terletak di x = {result2:.6f}")

                plot_iteration_b(table1, table2)
            
                
                
                st.write("---")  
                st.header("Kesimpulan : ")
            
                if table1.shape[0]> table2.shape[0]:
                    st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunakan metode")
                    st.subheader("Secant")
                if table1.shape[0]< table2.shape[0]:
                    st.write("Maka solusi terbaik dari fungsi yang telah diinput adalah menggunnakan metode ")
                    st.subheader("Regula Falsi")
                if table1.shape[0]== table2.shape[0]:
                    st.write("Kedua Metode adalah solusi terbaik")
                
    if (menentukan2 == "Biseksi & Secant") :
        biseksi_secant()
    if (menentukan2 == "Biseksi & Newton Raphson") :
        biseksi_newton_raphson()
    if (menentukan2 == "Regula Falsi & Secant") :
        regula_falsi_secant()
    if (menentukan2 == "Regula Falsi & Newton Raphson") :
        regula_falsi_newton_raphson()            

if (menentukan1 == "Metode Terbuka") :
    biseksi_regula_falsi()
if (menentukan1 == "Metode Tertutup") :
    newton_raphson_secant()
if (menentukan1 == "Metode Campuran") :
    metode_campuran()



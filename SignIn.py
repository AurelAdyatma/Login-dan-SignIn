import streamlit as st

def login_page():
    """
    Menampilkan halaman Sign In/Login untuk aplikasi GetCareer.
    """
    
    st.title("🔑 Sign In") 
    
    with st.form(key='login_form'):
        username = st.text_input("Username", placeholder="Masukkan Username Anda") # [cite: 94]
        
        password = st.text_input("Password", type="password", placeholder="Masukkan Password Anda") # [cite: 96]
        
        sign_in_button = st.form_submit_button("Sign In") # [cite: 97]

        if sign_in_button:
            if username == "admin" and password == "adminpass":
                st.success("Login Berhasil! Selamat datang admin.")
            else:
                st.error("Username atau Password salah.")
    st.markdown("---") 
    st.markdown("Belum punya akun? (Simulasi) Klik tombol di bawah ini untuk Sign Up") # [cite: 98]
    
    if st.button("Sign Up"): 
        st.info("Fitur Sign Up (Registrasi) dipicu.")


if __name__ == "__main__":
    st.set_page_config(
        page_title="GetCareer - Sign In",
        layout="centered",
    )
    
    login_page()

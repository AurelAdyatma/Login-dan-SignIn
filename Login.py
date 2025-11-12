import streamlit as st

# Menginisialisasi session state untuk mengelola tampilan halaman
if 'page_state' not in st.session_state:
    st.session_state.page_state = 'login' # Bisa 'login' atau 'forgot_password'

def login_page_pure_python():
    """
    Menampilkan halaman login GetCareer.
    """
    
    # --- 1. Konfigurasi Halaman ---
    st.set_page_config(
        page_title="GetCareer - Masuk",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # --- 2. Header Aplikasi ---
    st.title("💼 GetCareer") 
    st.subheader("Temukan peluang karir Anda berikutnya.")
    st.divider()

    # --- Logika Tampilan Halaman (State Management) ---
    if st.session_state.page_state == 'login':
        display_login_form()
    elif st.session_state.page_state == 'forgot_password':
        display_forgot_password_form()

# --- FUNGSI LOGIN UTAMA ---
def display_login_form():
    """
    Menampilkan formulir login dan tombol Lupa Kata Sandi.
    """
    
    with st.container(border=True):
        st.header("Masuk ke Akun Anda")

        with st.form(key='login_form'):
            
            # Input Email/Username
            credential = st.text_input(
                "Email/Username", 
                placeholder="Masukkan alamat email atau username Anda"
            )

            # Input Kata Sandi
            password = st.text_input(
                "Kata Sandi", 
                type="password", 
                placeholder="Masukkan kata sandi"
            )
            
            # Tombol Masuk ke Akun
            login_button = st.form_submit_button(
                "Masuk ke Akun", 
                type="primary", 
                use_container_width=True
            ) 

            # Logika Simulasi Otentikasi
            if login_button:
                if (credential.lower() == "admin" or credential.lower() == "user@example.com") and password == "12345":
                    st.success("✅ Login Berhasil! Selamat datang.")
                    st.balloons()
                else:
                    st.error("❌ Email/Username atau Kata Sandi salah.")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        # Tombol Lupa Kata Sandi (Mengubah state ke 'forgot_password')
        if st.button("Lupa Kata Sandi?", key="forgot_pass_btn"):
            st.session_state.page_state = 'forgot_password'
            st.rerun()

    with col2:
        # Tombol Daftar Akun Baru
        if st.button("Daftar Akun Baru", key="signup_btn"):
            st.success("Simulasi: Mengarahkan ke halaman registrasi...")


# --- FUNGSI LUPA KATA SANDI ---
def display_forgot_password_form():
    """
    Menampilkan formulir untuk fitur Forgot Password.
    """
    st.header("Lupa Kata Sandi ❓")
    
    with st.container(border=True):
        st.write("Masukkan email yang terdaftar untuk menerima tautan reset kata sandi.")
        
        with st.form(key='forgot_password_form'):
            reset_email = st.text_input(
                "Email Terdaftar", 
                placeholder="misalnya: user@example.com"
            )
            
            # Tombol Kirim Tautan Reset
            send_link_button = st.form_submit_button(
                "Kirim Tautan Reset", 
                type="primary", 
                use_container_width=True
            )
            
            if send_link_button:
                if "@" in reset_email and "." in reset_email:
                    st.success(f"✅ Tautan reset telah dikirim ke **{reset_email}**. Cek email Anda!")
                else:
                    st.error("Masukkan alamat email yang valid.")

        st.divider()
        # Tombol kembali ke halaman login
        if st.button("⬅️ Kembali ke Halaman Login", key='back_to_login_btn'):
            st.session_state.page_state = 'login'
            st.rerun()


if __name__ == "__main__":
    login_page_pure_python()

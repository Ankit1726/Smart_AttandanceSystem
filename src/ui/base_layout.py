import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
        .stApp {
            background: radial-gradient(circle at top, #0f172a, #020617) !important;
        }

        /* Card Style */
        .stApp div[data-testid="stColumn"]{
            background: rgba(255, 255, 255, 0.04) !important;
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            padding: 2rem !important;
            border-radius: 1.5rem !important;
            border: 1px solid rgba(255,255,255,0.08);
            transition: all 0.3s ease;
        }

        .stApp div[data-testid="stColumn"]:hover{
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(99,102,241,0.2);
        }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(160deg, #020617, #0f172a) !important;
        }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@200..900&display=swap');

        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.2rem !important;
        }

        /* 🔥 Project Branding */
        .main-title {
            font-family: 'Outfit', sans-serif;
            font-size: 3rem;
            font-weight: 800;
            color: #6366f1;
            text-align: center;
            letter-spacing: 1px;
        }

        .subtitle {
            text-align: center;
            color: #94a3b8;
            font-size: 1rem;
            margin-bottom: 2rem;
        }

        /* Headings */
        h1, h2, h3 {
            font-family: 'Outfit', sans-serif;
            color: #f1f5f9;
        }

        p {
            color: #cbd5f5;
        }

        /* Buttons */
        button {
            border-radius: 10px !important;
            background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
            color: white !important;
            padding: 10px 18px !important;
            border: none !important;
            transition: all 0.25s ease !important;
            box-shadow: 0 4px 15px rgba(99,102,241,0.3);
        }

        button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 25px rgba(139,92,246,0.5);
        }

        button[kind="secondary"]{
            background: linear-gradient(135deg, #ec4899, #f43f5e) !important;
        }

        button[kind="tertiary"]{
            background: #111827 !important;
        }

        /* Inputs */
        input, textarea {
            background: rgba(255,255,255,0.05) !important;
            color: white !important;
            border-radius: 8px !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
        }

        </style>
    """, unsafe_allow_html=True)
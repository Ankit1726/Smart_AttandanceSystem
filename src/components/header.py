import streamlit as st 

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin:30px 0;">
            <img src="{logo_url}" style="height:100px; margin-bottom:12px;"/>
            <h1 style="
                text-align:center;
                font-size:42px;
                font-weight:800;
                letter-spacing:2px;
                line-height:1.2;
                text-transform:uppercase;
                font-family:sans-serif;
                color:#ffffff;
            ">
                SMART<br/>
                <span style="color:#8A9EFF;">CLASS</span></h1>
</div>
""", unsafe_allow_html=True)

def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#ffffff'>SMART
            <br/>
            <span style="color:#8A9EFF;">CLASS</span></h1>
        </div>   
                
                """, unsafe_allow_html=True)
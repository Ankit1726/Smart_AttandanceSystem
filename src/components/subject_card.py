import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:#1E1B2E; border-left: 8px solid #EB459E; padding:25px; border-radius: 20px; border: 1px solid #2D2A40; margin-bottom:20px;">
        <h3 style="margin:0; color:#F1F5F9; font-size: 1.5rem ">{name}</h3>
        <p style="color:#CBD5F5; margin:10px 0;">Code : <span style="background:#2A2540; color:#8B9DFF; padding:2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background:#2A2540; color:#CBD5F5; padding:5px 12px; border-radius:12px; font-size:0.9rem; border:1px solid #3A3555;">{icon} <b style="color:#F1F5F9;">{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
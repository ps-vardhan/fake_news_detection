import streamlit as st

def render_header():
    st.markdown("""
    <style>
        .main .block-container {
            padding-top: 0 !important;
        }
        
        .header{
            background-color:#2E7D32;
            padding:0.75rem 1rem;
            border-radius: 0.75rem; 
        }
        
        .header-inner {
            max-width:32rem;
            display: flex;
            gap:0.75rem;
            align-items:center; 
            margin: 0 auto;
        }
        
        .header-icon {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 0.5rem;
            width: 36px;
            height: 36px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
        }
        .header-title {
            font-size:16px;
            font-weight:700;
            margin:0;
            color:white;
        }
        .header-subtitle {
            color: rgba(255, 255, 255, 0.8);
            margin: 0;
            font-size: 12px;
        }
    </style>
    <header class="header">
    <div class="header-inner">
        <div class="header-icon">🌱</div>
        <div>
            <p class="header-title">Crop Advisor</p>
            <p class="header-subtitle">
                Smart Recommendations for your Region
            </p>
        </div>
        </div>
    </header>
    """, unsafe_allow_html=True)
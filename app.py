import streamlit as st
import pandas as pd
import plotly.express as px
from assets.header import render_header
from assets.detect_location import render_location_bar


st.set_page_config(
    page_title="LTR AGRI",
    page_icon="🌾",
    layout="wide",
)

render_header()

location_status = "loading"   # "loading" | "success" | "denied"
location_name = "India"
render_location_bar(location_status,location_name)
# st.markdown("""
# <style>
# .main .block-container{padding-top:2rem;}
# h1{color:#2E7D32;} 
# div[data-testid="stMetricValue"] {font-size:1.6rem;}
# </style>
# """,unsafe_allow_html=True)

# with st.container(border=True):
#     col1,col2=st.columns([1,5])
#     with col1:
#         st.markdown("# 🌾")
#     with col2:
#         st.title("LTR AGRI")
#         st.markdown("**Smart recommendations for your region**")


# col_loc_btn,col_loc_text=st.columns([1,3])

# if 'region' not in st.session_state:
#     st.session_state.region="East Godavari(Default)"
    
# with col_loc_btn:
#     if st.button("Detect Location"):
#         st.session_state.region="West Godavari"
#         st.success("Location Updated!")
        
# with col_loc_text:
#     st.markdown(f"**Current Region:**{st.session_state.region}")
#     selected_region=st.selectbox(
#         "Change Region:",
#         ["East Godavari","West Godavari"],
#         index=0,
#         label_visibility="collapsed"
#     )
#     if selected_region!=st.session_state.region.split(" (")[0]:
#         st.session_state.region=selected_region
        
# st.markdown("-----")


# st.subheader("Top Suitability Ranking")

# crop_data=[
#     {"name":"rice","score":"92%","trend":"+2.1%","yeild":6.2},
# ]
# cols=st.columns(5)  
# for idx,crop in enumerate(crop_data):
#     with cols[idx]:
#         st.metric(
#             label=crop["name"],
#             value=crop["score"],
#             delta=crop["trend"],
#         )
# st.markdown("-----")


# st.subheader("Yeild and Feature Analysis")

# df_crops=pd.DataFrame(crop_data)
# df_features=pd.DataFrame({
#     "Crop":["Rice","Chilli","Onion","Wheat","Cotton"],
#     "Water Need (mm)": [1200, 600, 450, 400, 700],
#     "Market Price (₹/q)": [2040, 18000, 1800, 2275, 6500]
# })

# tab1,tab2=st.tabs(["Expected Yeild","Market Potential"])

# with tab1:
#     fig_yeild=px.bar(
#         df_crops, 
#         x="name", 
#         y="yield", 
#         color="name",
#         title="Projected Yield (tonnes/hectare)",
#         labels={"yield": "Yield (t/ha)", "name": "Crop"},
#         height=350
#     )
#     st.plotly_chart(fig_yeild,use_container_width=True)
    
# with tab2:
#     fig_price=px.scatter(
#         df_features,
#         x="Crop",
#         y="Market Price (₹/q)",
#         size="Water Need (mm)",
#         color="Crop",
#         title="Market Price vs Water Need (Size)",
#         height=350
#     )
#     st.plotly_chart(fig_price,use_container_width=True)
    
#     st.subheader("Smart REcommendations")
    
#     col_rec_main,col_rec_details=st.columns([2,1])
    
#     with col_rec_main:
#         with st.expander(" Best Action:Fertilizer Application",expanded=True):
#             st.markdown("""
#         **Recommendation:** Apply **Urea (46% N)**.
#         - **Timing:** Split application (50% basal, 25% tillering).
#         - **Reasoning:** Soil nitrogen is currently reported as **Low**.
#         - **Risk:** 🌦️ Rain forecast in 2 days. Apply *after* rain to prevent leaching.
#         """)
            
#             st.info("💡 Tip: Add Zinc Sulfate for better grain filling.")
            
            
#             with st.expander("🐛 Pest Control Alert"):
#                 st.markdown("""
#         **Alert:** High risk of **Stem Borer** in this region.
#         - **Action:** Install pheromone traps @ 5/ha.
#         - **Organic Option:** Neem Oil Spray (5%).
#         """)
            
#     with col_rec_details:
#         st.warning("⚠️ **Weather Advisory**")
#         st.caption("Heavy rainfall expected in next 48 hours.")
#         st.markdown("- Delay irrigation.")
#         st.markdown("- Ensure drainage channels are clear.")
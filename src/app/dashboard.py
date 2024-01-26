import streamlit as st

st.set_page_config(
    page_title='Generate blogs',
    page_icon="🤖",
    layout='centered',
    initial_sidebar_state='collapsed'
    )

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
      
col1, col2 = st.columns(2)

with col1:
  st.title("Dashboard")
  st.write()

with col2:
  st.image()

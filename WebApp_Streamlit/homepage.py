import streamlit as st

st.set_page_config(
    page_title='Multipage App',
    page_icon='🏠',
)

hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)
st.title('Product Info Gathering')
st.sidebar.success('Select a page above.')
st.subheader('Developed by DARKHOOD')
st.text('This is a BETA version of the tool.')
st.write('In todays fast-paced online marketplace, staying updated with product information is crucial for smart decision-making. Our Product Web Scraping Tool is designed to simplify the process of gathering detailed product data from multiple websites in real-time. Whether you are tracking prices, monitoring competitors, or collecting product details for analysis, our tool automates and streamlines the entire process, saving you valuable time and effort.')
st.write('With an easy-to-use interface, simply input the URLs, and let our tool do the heavy lifting—fetching and organizing product names, prices, descriptions, and more. Empower your business with accurate, up-to-date data to make informed decisions with confidence.')
st.subheader('Functionality')
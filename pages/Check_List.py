import streamlit as st

st.set_page_config(
    page_title="Checking list",
    page_icon="👋",
)

st.header('Dev Tool')

st.subheader('Communication:')
tool1 = st.empty()
tool1.checkbox('OpenProject')
if tool1:
    tool1.empty()
    st.checkbox('OpenProject', value=True)
    
if tool1==False:
    tool1.empty()
    st.checkbox('OpenProject', value=False)

tool1 = st.checkbox('Mattermost')

st.subheader('Deployment:')
tool = st.checkbox('Docker')
tool = st.checkbox('Git — .gitignore')
tool = st.checkbox('GitHub')

st.subheader('App dev:')
tool = st.checkbox('Android studio — Flutter')

st.subheader('Web dev:')
tool = st.checkbox('VSCode — Flutter')
tool = st.checkbox('Django (Python)')
tool = st.checkbox('Flask')

st.subheader('Package:')
tool = st.checkbox('Anaconda')

st.subheader('Backend/Data science:')
tool = st.checkbox('Pycharm')
tool = st.checkbox('tfile -- Flutter')

st.subheader('Data analysis:')
tool = st.checkbox('RStudio')
tool = st.checkbox('Tableau')
tool = st.checkbox('Google analytics')
tool = st.checkbox('D3.is (D3 chart python)')

st.subheader('API:')
tool = st.checkbox('Fastapi/Flask')

st.subheader('API testing:')
tool = st.checkbox('Postman')

st.subheader('API deploy:')
tool = st.checkbox('Heroku')
tool = st.checkbox('VM (PVE — Proxmox — ubuntu)')
tool = st.checkbox('Google Cloud Run')
tool = st.checkbox('AWS gateways')

st.subheader('Database:')
tool = st.checkbox('Firebase')
tool = st.checkbox('MySQL')
tool = st.checkbox('PostgreSQL')
tool = st.checkbox('Redis')

st.subheader('Multi-Cloud Storage:')
tool = st.checkbox('MinIO')

st.subheader('Animation:')
tool = st.checkbox('Unity -- VS')
tool = st.checkbox('Unreal Engine -- VS')
tool = st.checkbox('Rive (To flutter)')

st.subheader('Terminal:')
tool = st.checkbox('iTerm 2')
tool = st.checkbox('Zsh')
tool = st.checkbox('Flutter doctor')

st.subheader('Version control, A/B Testing:')
tool = st.checkbox('Flagsmith')

st.subheader('Data science web app:')
tool = st.checkbox('Streamlit — .streamlit')

st.subheader('Mail API:')
tool = st.checkbox('MailGun')

st.subheader('Web Scrapping:')
tool = st.checkbox('Beautiful Soap')
tool = st.checkbox('Scrappy')
tool = st.checkbox('URLLIB')
tool = st.checkbox('Selenium (harder)')

st.subheader('UI/UX:')
tool = st.checkbox('Adobe XD (To flutter)')
tool = st.checkbox('Figma (To flutter)')

st.subheader('App Marketing:')
tool = st.checkbox('Apple connect')
tool = st.checkbox('Google play console')

st.subheader('Web Services, System Development:')
tool = st.checkbox('Rust (Ruff)')

st.subheader('Big Data Sources:')
tool = st.checkbox('[https://www.finereport.com/tw/data-analysis/freedata.html]')

"""
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
"""

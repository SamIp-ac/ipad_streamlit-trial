import streamlit as st

st.set_page_config(
    page_title="Checking list",
    page_icon="👋",
)

st.header('Dev Tool')

st.subheader('Communication:')

tool1 = st.checkbox('OpenProject', value=True)
tool1 = st.checkbox('Mattermost', value=True)

st.subheader('Deployment:')
tool = st.checkbox('Docker', value=True)
tool = st.checkbox('Git — .gitignore', value=True)
tool = st.checkbox('GitHub', value=True)

st.subheader('App dev:')
tool = st.checkbox('Android studio — Flutter')

st.subheader('Web dev:')
tool = st.checkbox('VSCode — Flutter')
tool = st.checkbox('Django (Python)')
tool = st.checkbox('Flask')

st.subheader('Package:')
tool = st.checkbox('Anaconda', value=True)

st.subheader('Backend/Data science:')
tool = st.checkbox('Pycharm', value=True)
tool = st.checkbox('tfile -- Flutter')

st.subheader('Data analysis:')
tool = st.checkbox('RStudio', value=True)
tool = st.checkbox('Tableau', value=True)
tool = st.checkbox('Google analytics')
tool = st.checkbox('D3.is (D3 chart python)')

st.subheader('API:')
tool = st.checkbox('Fastapi/Flask', value=True)

st.subheader('API testing:')
tool = st.checkbox('Postman', value=True)

st.subheader('API deploy:')
tool = st.checkbox('Heroku (need sign up by VPN -- US address)')
tool = st.checkbox('VM (PVE — Proxmox — ubuntu)')
tool = st.checkbox('Google Cloud Run', value=True)
tool = st.checkbox('AWS gateways')

st.subheader('Database:')
tool = st.checkbox('Firebase', value=True)
tool = st.checkbox('MySQL', value=True)
tool = st.checkbox('PostgreSQL', value=True)
tool = st.checkbox('Redis')

st.subheader('Multi-Cloud Storage:')
tool = st.checkbox('MinIO')

st.subheader('Animation:')
tool = st.checkbox('Unity -- VS')
tool = st.checkbox('Unreal Engine -- VS')
tool = st.checkbox('Rive (To flutter)')

st.subheader('Terminal:')
tool = st.checkbox('iTerm 2', value=True)
tool = st.checkbox('Zsh', value=True)
tool = st.checkbox('Flutter doctor', value=True)

st.subheader('Version control, A/B Testing:')
tool = st.checkbox('Flagsmith')

st.subheader('Data science web app:')
tool = st.checkbox('Streamlit — .streamlit', value=True)

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
tool = st.checkbox('[Sources](https://www.finereport.com/tw/data-analysis/freedata.html)')

"""
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
"""

from PIL import Image
import os
import streamlit as st

for file_ in os.listdir('Roadmap'):
  image = Image.open('Roadmap/' + file_)
  st.image(image, caption='Data_Science_Map')

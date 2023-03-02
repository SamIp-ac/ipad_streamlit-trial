from PIL import Image

for file_ in os.listdir('Roadmap'):
  image = Image.open(file_)
  st.image(image, caption='Data_Science_Map')

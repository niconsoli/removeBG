from rembg import remove, new_session
from PIL import Image

modelo = new_session("u2net")
foto = Image.open("foto.jpg")
sem_fundo = remove(foto, session=modelo)
sem_fundo.save("removeBG.png")
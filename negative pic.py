from PIL import Image
import PIL.ImageOps    

image = Image.open('minion.jpg')

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('hola.jpg')

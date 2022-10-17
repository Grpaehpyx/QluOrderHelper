import tesserocr
from PIL import Image
image = Image.open('check (2).png')
result = tesserocr.image_to_text(image)
print(result.replace(" ",""))
from PIL import Image

base_image = Image.open('./images/base.jpg')
base_image.thumbnail((500, 500), Image.ANTIALIAS)

logo_image = Image.open('./images/logo.png')

w = ((base_image.size[0] - logo_image.size[0]) / 2)
h = ((base_image.size[1] - logo_image.size[1]) / 2)

base_image.paste(logo_image, (int(w), int(h)), mask=logo_image)

base_image.save('./pasteimages/paste.png', 'PNG', quality=100)

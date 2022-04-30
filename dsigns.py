from PIL import Image, ImageFont, ImageDraw 

my_image = Image.open("image.jpeg")

# title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)


title_text = "The Beauty of Nature"


image_editable = ImageDraw.Draw(my_image)


image_editable.text((60,60), title_text, (237, 230, 211))

my_image.save("result.jpg")


from PIL import Image, ImageFont, ImageDraw 

my_image = Image.open("nature.jpg")

title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)


title_text = "The Beauty of Nature"


image_editable = ImageDraw.Draw(my_image)


image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)

save("result.jpg")


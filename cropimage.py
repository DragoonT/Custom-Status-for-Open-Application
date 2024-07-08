from PIL import Image, ImageDraw, ImageOps

image_path = "yourimage.png" # .png, .jpg, or .jpeg
img = Image.open(image_path).convert("RGBA")

img = img.resize((1024, 1024), Image.LANCZOS)

# 369 1024, 1024 pixel
corner_radius = 369 

mask = Image.new("L", img.size, 0)
draw = ImageDraw.Draw(mask)
width, height = img.size
draw.rounded_rectangle([(0, 0), (width, height)], radius=corner_radius, fill=255)

rounded_img = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
rounded_img.putalpha(mask)

output_path = "yourcropimage.png" # .png, .jpg, or .jpeg
rounded_img.save(output_path)

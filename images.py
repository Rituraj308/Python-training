# 1st install pillow from cmd
from PIL import Image, ImageFilter
img = Image.open( 'C:\\Users\\ritur\\OneDrive\\Desktop\\RITURAJ\\Git hub proj\\Python-training\\pokidesk\\pikachu.jpg')
print(img)
print(img.size)
print(img.format)
print(img.mode)
print(dir(img))
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")
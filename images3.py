from PIL import Image,ImageFilter
img =Image.open('C:\\Users\\ritur\\OneDrive\\Desktop\\RITURAJ\\Git hub proj\\Python-training\\pokidesk\\astro.jpg')
print(img.size)
new_img = img.resize((400,200)) #image becomes small but image appeares all squzed up
new_img.save('thumbnail.jpg')
img.thumbnail((400,200)) #image becomes small and it looks normal
img.save('thumbnail2.jpg')
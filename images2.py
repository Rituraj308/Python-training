from PIL import Image, ImageFilter
img = Image.open( 'C:\\Users\\ritur\\OneDrive\\Desktop\\RITURAJ\\Git hub proj\\Python-training\\pokidesk\\pikachu.jpg')
filtered_img2 = img.convert('L')
croocked = filtered_img2.rotate(90) #rotates the images
croocked.save('greys.png','png')
resize = filtered_img2.resize((300,300))
resize.save('resized grey.png', 'png') #we can increase or decrease the size of the pic
box = (100, 100, 400, 400)
region = filtered_img2.crop(box)
region.save('cropedimg.png','png')# for croping the pic
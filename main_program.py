from PIL import Image
myself = Image.open ('me.png')
background = Image.open ('mount_fiji.jpg')
background.paste (myself, (0,0), myself)
background.show()
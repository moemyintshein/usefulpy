from rembg import remove
from PIL import Image

print("Program for remove image background\n")
#Filename of image with backgroundd
input_path = input("Enter input image name: ")
#Filename of output image without background
output_path = input("Enter output image name: ")

in_image = Image.open(input_path)
out_image = remove(in_image)
out_image.save(output_path)
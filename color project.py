from PIL import Image

# RGB values for recoloring.
orchid =(218,112,214)
firebrick = (178, 34, 34)
salmon = (250, 128, 114)
cyan = (0, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)


# Import image.
my_image = Image.open("minion.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for color in image_list:
    intensity = color[0] + color[1] +color[2]

    if intensity < 182:
        recolored.append(blue)
    if intensity >= 182 and intensity < 364:
        recolored.append(red)
    if intensity >= 364 and intensity < 546:
        recolored.append(green)
    if intensity >= 546:
        recolored.append(yellow)


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"

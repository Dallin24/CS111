from byuimage import Image


def iron_puzzle(filename):
    """Write your code here"""
    iron_image = Image(filename)
    for y in range(iron_image.height):
        for x in range(iron_image.width):
            pixel = iron_image.get_pixel(x,y)
            pixel.blue = pixel.blue * 10
            pixel.red = 0
            pixel.green = 0
    return iron_image     

def west_puzzle(filename):
    """Write your code here"""
    west_image = Image(filename)
    for y in range(west_image.height):
        for x in range(west_image.width):
            pixel = west_image.get_pixel(x,y)
            
            if(pixel.blue < 16):
                pixel.blue = pixel.blue * 16
            else:
                pixel.blue = 0

            pixel.red = 0
            pixel.green = 0
    return west_image     

def darken(filename, percent):
    """Write your code here"""
    darker_image = Image(filename)
    for y in range(darker_image.height):
        for x in range(darker_image.width):
            pixel = darker_image.get_pixel(x,y)

            pixel.blue = pixel.blue * (1 - percent)
            pixel.red = pixel.red * (1 - percent)
            pixel.green = pixel.green * (1 - percent)
    return darker_image    

def grayscale(filename):
    """Write your code here"""
    gray_iamge = Image(filename)
    for y in range(gray_iamge.height):
        for x in range(gray_iamge.width):
            pixel = gray_iamge.get_pixel(x,y)

            average = (pixel.red + pixel.green + pixel.blue) / 3
            pixel.red = average 
            pixel.green = average
            pixel.blue = average
    return gray_iamge 

def sepia(filename):
    """Write your code here"""
    sepia_iamge = Image(filename)
    for y in range(sepia_iamge.height):
        for x in range(sepia_iamge.width):
            pixel = sepia_iamge.get_pixel(x,y)

            true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
            true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
            true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue

            if(true_red > 255):
                true_red = 255
            if(true_green > 255):
                true_red = 255
            if(true_red > 255):
                true_blue = 255

            pixel.red = true_red
            pixel.green= true_green
            pixel.blue = true_blue

    return sepia_iamge

def create_left_border(filename, weight):
    """Write your code here"""
    old_image = Image(filename)
    new_image = Image.blank(old_image.width + weight, old_image.height)

    for y in range(old_image.height):
        for x in range(old_image.width):
            old_pixel = old_image.get_pixel(x,y)
            new_pixel = new_image.get_pixel(x + weight,y)

            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    for y in range(new_image.height):
        for x in range(new_image.width):
            pixel = new_image.get_pixel(x,y)
            if(x < weight):
                pixel.blue = 255
                pixel.red = 0
                pixel.green = 0

    return new_image

###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    """Write your code here"""


def copper_puzzle(filename):
    """Write your code here"""

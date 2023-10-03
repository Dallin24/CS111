import sys
from byuimage import Image

def validate_commands(input):
    if (input[0] == '-d' and len(input) == 2):
        return True
    elif (input[0] == '-k' and len(input) == 4):
        return True
    elif (input[0] == '-s' and len(input) == 3):
        return True
    elif (input[0] == '-g' and len(input) == 3):
        return True
    elif (input[0] == '-b' and len(input) == 7):
        return True
    elif (input[0] == '-f' and len(input) == 3):
        return True
    elif (input[0] == '-m' and len(input) == 3):
        return True
    elif (input[0] == '-c' and len(input) == 7):
        return True
    elif (input[0] == '-y' and len(input) == 6):
        return True
    else:
        return False
    
def change_pixel(pixel, r, g, b):
    pixel.red = r
    pixel.green = g
    pixel.blue = b
    
    return pixel

def change_whole_pixel(old_pixel, new_pixel):
    new_pixel.red = old_pixel.red
    new_pixel.green = old_pixel.green
    new_pixel.blue = old_pixel.blue
    
    return new_pixel


def darken(darker_image, percent):
    darker_image = Image(darker_image)
    for y in range(darker_image.height):
        for x in range(darker_image.width):
            pixel = darker_image.get_pixel(x,y)

            pixel = change_pixel(pixel, pixel.red * (1 - percent), pixel.green * (1 - percent),pixel.blue * (1 - percent))
    
    return darker_image  

def sepia(filename):
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

            pixel = change_pixel(pixel, true_red, true_green, true_blue)

    return sepia_iamge

def grayscale(filename):
    gray_image = Image(filename)
    for y in range(gray_image.height):
        for x in range(gray_image.width):
            pixel = gray_image.get_pixel(x,y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            pixel = change_pixel(pixel, average, average, average)
            
    return gray_image 

def make_borders(filename, border_thickness, red, green, blue):
    original_image = Image(filename)
    new_image = Image.blank(original_image.width + border_thickness * 2, original_image.height + border_thickness * 2)
    
    for y in range(original_image.height):
        for x in range(original_image.width):
            old_pixel = original_image.get_pixel(x,y)
            new_pixel = new_image.get_pixel(x + border_thickness, y + border_thickness)
            
            new_pixel = change_whole_pixel(old_pixel, new_pixel)
            
    for y in range(new_image.height):
        for x in range(new_image.width):
            pixel = new_image.get_pixel(x,y)
            
            if((x < border_thickness) or (y < border_thickness) or (x >= original_image.width + border_thickness) or (y >= original_image.height + border_thickness)):
                pixel = change_pixel(pixel, red, green, blue)
            
    return new_image
    
def flipped(filename):
    old_image = Image(filename)
    height = old_image.height
    width = old_image.width
    new_image = Image.blank(width, height)

    for y in range(height):
        for x in range(width):
            old_pixel = old_image.get_pixel(x,y)
            new_pixel = new_image.get_pixel(x,(height - 1) - y)
            
            new_pixel = change_whole_pixel(old_pixel, new_pixel)
    
    return new_image

def mirror(filename):
    old_image = Image(filename)
    width = old_image.width
    height = old_image.height
    new_image = Image.blank(width, height)

    for y in range(height):
        for x in range(width):
            old_pixel = old_image.get_pixel(x,y)
            new_pixel = new_image.get_pixel((width - 1) - x,y)
            
            new_pixel = change_whole_pixel(old_pixel, new_pixel)
    
    return new_image

def collage(file_one, file_two, file_three, file_four, border_thickness):
    image_one = Image(file_one)
    image_two = Image(file_two)
    image_three = Image(file_three)
    image_four = Image(file_four)
    
    width = image_one.width
    height = image_one.height
    
    total_width = width * 2 + border_thickness * 3
    total_height = height * 2 + border_thickness * 3
    
    collage_image = Image.blank(total_width, total_height)
    
    for y in range(height):
        for x in range(width):
            old_pixel_one = image_one.get_pixel(x,y)
            old_pixel_two = image_two.get_pixel(x,y)
            old_pixel_three = image_three.get_pixel(x,y)
            old_pixel_four = image_four.get_pixel(x,y)
            
            new_pixel_one = collage_image.get_pixel(x + border_thickness, y + border_thickness)
            new_pixel_two = collage_image.get_pixel(x + border_thickness * 2 + width, y + border_thickness)
            new_pixel_three = collage_image.get_pixel(x + border_thickness, y + border_thickness * 2 + height)
            new_pixel_four = collage_image.get_pixel(x + border_thickness * 2 + width, y + border_thickness * 2 + height)
            
            new_pixel_one = change_whole_pixel(old_pixel_one, new_pixel_one)
            new_pixel_two = change_whole_pixel(old_pixel_two, new_pixel_two)
            new_pixel_three = change_whole_pixel(old_pixel_three, new_pixel_three)
            new_pixel_four = change_whole_pixel(old_pixel_four, new_pixel_four)
    
    for y in range(total_height):
        for x in range(total_width):
            pixel = collage_image.get_pixel(x,y)
            
            if((x < border_thickness) or (y < border_thickness) or (x >= total_width - border_thickness) or (y >= total_height - border_thickness)):
                pixel = change_pixel(pixel, 0, 0, 0)
            
            if((border_thickness + width <= x < total_width - width - border_thickness) or (border_thickness + height <= y < total_height - height - border_thickness)):
                pixel = change_pixel(pixel, 0, 0, 0)
                
    return collage_image

def detect_green(pixel, factor, threshold):
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False

def greenscreen(back_image_file, fore_image_file, threshold, factor):
    back_image = Image(back_image_file)
    fore_image = Image(fore_image_file)
    
    width = fore_image.width
    height = fore_image.height
    
    for y in range(height):
        for x in range(width):
            back_pixel = back_image.get_pixel(x,y)
            fore_pixel = fore_image.get_pixel(x,y)
            
            if detect_green(back_pixel, factor, threshold):
                back_pixel = change_whole_pixel(fore_pixel, back_pixel)
    
    return back_image
    
def main():
    args = sys.argv[1:]

    if(validate_commands(args)):
        current_image = Image(args[1])
        
        if (args[0] == '-d'):
            current_image.show()
        elif (args[0] == '-k'):
            current_image = darken(args[1], float(args[3]))     
            current_image.save(args[2]) 
        elif (args[0] == '-s'):
            current_image = sepia(args[1])
            current_image.save(args[2])
        elif (args[0] == '-g'):
            current_image = grayscale(args[1])
            current_image.save(args[2])
        elif (args[0] == '-b'):
            current_image = make_borders(args[1], int(args[3]), int(args[4]), int(args[5]), int(args[6]))
            current_image.save(args[2])
        elif (args[0] == '-f'):
            current_image = flipped(args[1])
            current_image.save(args[2])
        elif (args[0] == '-m'):
            current_image = mirror(args[1])
            current_image.save(args[2])
        elif (args[0] == '-c'):
            current_image = collage(args[1], args[2], args[3], args[4], int(args[6]))
            current_image.save(args[5])
        elif (args[0] == '-y'):
            current_image = greenscreen(args[1], args[2], float(args[4]), float(args[5]))
            current_image.save(args[3])
        
        
    

if __name__ == "__main__":
    main()
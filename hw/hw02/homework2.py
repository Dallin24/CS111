from byuimage import Image 

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
    
if __name__ == "__main__":
    pass
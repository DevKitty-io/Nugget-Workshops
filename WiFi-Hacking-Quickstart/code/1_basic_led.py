# Alex Lynd, 2023
# fill in the variables and make the code work!

# import libraries
import board
import neopixel
import time

# NeoPixel pin & number of NeoPixels
pixel_pin = # IO Pin here! 
pixel_num = # Number of Pixels here! 

#initialize NeoPixels
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=) # brightness here! 0-1


# CHALLENGE: create an infinite loop that also resets the pixels

# cycle through pixels and set to solid color
for i in range(0,pixel_num):
    pixels[i] = (,,)
    time.sleep(1)

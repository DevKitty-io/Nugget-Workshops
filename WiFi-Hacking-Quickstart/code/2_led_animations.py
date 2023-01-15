# Alex Lynd, 2023
# Basic script to test Adafruit LED animations!

import board
import neopixel

# import a bunch of animations!
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.colorcycle import ColorCycle

# import preset colors!
# RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, WHITE, BLACK, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE
from adafruit_led_animation.color import *

# NeoPixel Pin & Number
pixel_pin = board.IO12
pixel_num = 11

# initialize NeoPixel strip
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.1, auto_write=False)

# initialize some animations!
# try modifying the parameters to see how they change!

# PERIOD: num of seconds for total animation, SPEED: refresh rate for each pixel

rainbow = Rainbow(pixels, speed=.01, period=5)
#sparkle_pulse = SparklePulse(pixels, speed=0.05, period=4, color=JADE)
#rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3, step=50)
#rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=, bounce=True)
#colorcycle = ColorCycle(pixels, 0.5, colors=[#color, #color, #color])

# uncomment these to try out an animation!
while True:
    #rainbow_chase.animate()
    #rainbow_comet.animate()
    #sparkle_pulse.animate()
    rainbow.animate()
    #colorcycle.animate()
    

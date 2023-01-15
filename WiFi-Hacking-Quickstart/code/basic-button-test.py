# Nugget Demo, by @AngelinaTsuboi using Adafruit CircuitPython
# Objective: A gentle introduction into the Nugget OLED interface, button input, and Neopixel programming
# Functionality: Change Nugget Faces and Neopixel Color when a specific arrow key is pressed
import time
import random
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from board import SCL, SDA
import busio
import displayio
import adafruit_framebuf
import adafruit_displayio_sh1106

## Screen setup and function to change image on the screen
faceImage = "faces/spooky-nugg-inv.bmp"
displayio.release_displays()
WIDTH = 130 # Change these to the right size for your display!
HEIGHT = 64

i2c = busio.I2C(SCL, SDA) # Create the I2C interface.
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT) # Create the SH1106 OLED class.

def NugFace(faceImage): ## Make a function to put cat face onto screen
    bitmap = displayio.OnDiskBitmap(faceImage) # Setup the file as the bitmap data source
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader) # Create a TileGrid to hold the bitmap
    group = displayio.Group() # Create a Group to hold the TileGrid
    group.append(tile_grid) # Add the TileGrid to the Group
    display.show(group) # Add the Group to the Display

NugFace(faceImage) #@# Show menu

## Neopixel Setup

pixel_pin = board.IO12    # Specify the pin that the neopixel is connected to (GPIO 12)
num_pixels = 1; delay = .1   # Set number of neopixels & delay between color changes in seconds
pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3)   # Create neopixel and set brightness to 30%

def SetColor(color):   # Define function with one input (color we want to set)
    for i in range(0, num_pixels):   # Addressing all 1 neopixels in a loop
        pixel[i] = (color)   # Set all neopixels a color

## Button Setup

#ButtonDict = {'up': 'IO9', 'down': 'IO18', 'left': 'IO11', 'right': 'IO14'} man these suck to use for indexing what was I thinking
LabelList = ['up', 'down', 'left', 'right']
PinList = ['IO9', 'IO18', 'IO11', 'IO14']

# Set up Arrow Keys

upBtn = DigitalInOut(board.IO9)
upBtn.direction = Direction.INPUT
upBtn.pull = Pull.UP
up_prev_state = upBtn.value

downBtn = DigitalInOut(board.IO18)
downBtn.direction = Direction.INPUT
downBtn.pull = Pull.UP
down_prev_state = downBtn.value

leftBtn = DigitalInOut(board.IO11)
leftBtn.direction = Direction.INPUT
leftBtn.pull = Pull.UP
left_prev_state = leftBtn.value

rightBtn = DigitalInOut(board.IO7)
rightBtn.direction = Direction.INPUT
rightBtn.pull = Pull.UP
right_prev_state = rightBtn.value

## Set up variables to check on the state of buttons and see if they have been pressed

ButtonList = [upBtn, downBtn, leftBtn, rightBtn]
StateList = [up_prev_state, down_prev_state, left_prev_state, right_prev_state]
SetColor([0,0, 255])

while True:
    for i in range(0,4):
        cur_state = ButtonList[i].value
        if cur_state != StateList[i]:
            if not cur_state:
                print(LabelList[i], "is pressed")
                if LabelList[i] == 'up':
                    faceImage = "faces/spooky-nugg-inv.bmp"
                    SetColor([255,0,0])
                elif LabelList[i] == 'down':
                    faceImage = "faces/spooky-nugg-inv.bmp"
                    SetColor([0,255,0])
                elif LabelList[i] == 'right':
                    faceImage = "faces/jack-o-nugg-right-inv.bmp"
                    SetColor([0,0, 255])
                else:
                    faceImage = "faces/jack-o-nugg-left-inv.bmp"
                    SetColor([247,158,240])
                NugFace(faceImage)
        StateList[i] = cur_state


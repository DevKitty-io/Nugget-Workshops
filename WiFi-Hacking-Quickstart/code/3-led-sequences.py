from led_animations import *
from adafruit_led_animation.sequence import AnimationSequence

animations = AnimationSequence(
    rainbow, rainbow_chase, colorcycle, advance_interval=5, auto_clear=True, random_order=True
)

while True:
    animations.animate()

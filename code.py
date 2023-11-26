import board
import touchio
import rotaryio
import usb_hid
import time
import neopixel
import digitalio
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout

# Constants
NUM_BLINKS = 0
PAUSE_DURATION = 1
LED_COLOR_RED = (255, 0, 0)
LED_OFF = (0, 0, 0)

# Setup
kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(kbd)
touch1 = touchio.TouchIn(board.TOUCH)
encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB, 4)
switch = digitalio.DigitalInOut(board.SWITCH)
switch.switch_to_input(pull=digitalio.Pull.DOWN)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.4, auto_write=False)

# Blink function
def blink(num_blinks, pause_duration):
    for _ in range(num_blinks):
        pixels[0] = LED_COLOR_RED
        pixels.show()
        time.sleep(0.1)
        pixels[0] = LED_OFF
        pixels.show()
        time.sleep(0.3)
    time.sleep(pause_duration)

# Main loop
last_position = None
switch_state = None
counter = 0

while True:
    position = encoder.position
    if touch1.value:
        # Wait for touch release and reset position
        while touch1.value: 
            time.sleep(0.1)
        position = 0

    # Check if position changed
    if position != last_position:
        print(position)
        counter = 0
    else:
        counter += 1
        if counter > 1000:
            blink(position, PAUSE_DURATION)
            counter = 0

    # Handle switch state
    if not switch.value and switch_state is None:
        switch_state = "pressed"
    elif switch.value and switch_state == "pressed":
        with open(f"/{position}.txt", "r") as file:
            text = file.read().replace('\r\n', '\n')
            #text = file.read().replace('\n', ' ') # For Unix/Linux newline characters
        keyboard_layout.write(text)
        switch_state = None

    last_position = position

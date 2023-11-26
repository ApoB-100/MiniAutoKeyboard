import board
import touchio
import rotaryio
import usb_hid
import time
import neopixel
import digitalio
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout

# Not necessary at the moment but can be used for special keys
# from keycode_win_de import Keycode

time.sleep(1)

kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(kbd)

touch1 = touchio.TouchIn(board.TOUCH)

encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB, 4)
last_position = None

# Initialize the switch as an input
switch = digitalio.DigitalInOut(board.SWITCH)
switch.switch_to_input(pull=digitalio.Pull.DOWN)
switch_state = None

num_blinks = 0  # Number of blinks
pause_duration = 1  # Pause duration in seconds

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.4, auto_write=False)

def blink(num_blinks, pause_duration):
    for i in range(num_blinks):
        pixels[0] = (255, 0, 0)  # Red color
        pixels.show()
        time.sleep(0.1)
        pixels[0] = (0, 0, 0)  # LED off
        pixels.show()
        time.sleep(0.3)
    time.sleep(pause_duration)

counter = 0

while True:
    position = encoder.position
    if touch1.value:
        while touch1.value:  # Wait for release...
            time.sleep(0.1)
        encoder.deinit()
        encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB, 4)
        position = 1
    if last_position is None or position != last_position:
        print(position)
        #keyboard_layout.write(str(position))
    if position == last_position and counter > 1000:
        blink(position, 1)
        counter = 0
        pass
    counter += 1
    last_position = position
    # Handle switch state
    if not switch.value and switch_state is None:
        switch_state = "pressed"
    if switch.value and switch_state == "pressed":
        print(str(position))
        
        with open(f"/{position}.txt", "r") as file:
            text = file.read()
        text = text.replace('\r\n', '\n') # For Windows newline characters
        # text = text.replace('\n', ' ') # For Unix/Linux newline characters
        keyboard_layout.write(text)
        switch_state = None
    
    

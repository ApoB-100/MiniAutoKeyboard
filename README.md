# MiniAutoKeyboard

MiniAutoKeyboard is a CircuitPython script designed for the [Adafruit Rotary Trinkey](https://learn.adafruit.com/adafruit-rotary-trinkey/overview) with the [ATSAMD21E18 32-bit Cortex M0+ SoC](https://www.microchip.com/en-us/product/atsamd21e18). The rotary encoder can be used to select a numbered *.txt file on the CircuitPython USB flashdrive of the Trinkey and output them as a regular USB HID device (e.g. a keyboard).

## Features
<img src="logo_miniautokeyboard.png" alt="MiniAutoKeyboard Logo" width="300" align="right">

1. **Text File Selection via Rotary Encoder**: Utilizes rotary encoder to scroll through and select numbered `.txt` files stored on the CircuitPython USB flash drive of the Trinkey. The NeoPixel LED will flash x times based on the file number currently selected.
2. **Automated Text Typing**: Once a `.txt` file is selected, pushing the switch on the rotary encoder triggers the script to type out the contents of the selected text file to the connected device, emulating a regular USB HID device like a keyboard.
3. **USB HID Device Emulation**: The script emulates keyboard inputs, allowing the typed contents to be inputted to any device that recognizes standard USB keyboards.
4. **Customizable Keyboard Layout**: Comes pre-configured for the Central European QWERTZ keyboard layout but can be adapted for other keyboard layouts, offering flexibility in different regional settings.

## Instructions

### Installation Instructions

1. **Flash CircuitPython onto the Trinkey**:
   - Visit the [CircuitPython Download page](https://circuitpython.org/board/adafruit_rotary_trinkey_m0/) and download the latest version of CircuitPython for the Adafruit Trinkey Rotary.
   - Connect the Trinkey to your computer via USB.
   - Double-press the reset button on the Trinkey to enter the bootloader mode.
   - A drive named `BOOT` should appear on your computer.
   - Drag and drop the `.uf2` file you downloaded onto this drive.
   - The Trinkey will reboot and a new drive named `CIRCUITPY` should appear.

2. **Copy Required Libraries**:
   - Create a folder named `lib` on the `CIRCUITPY` drive.
   - Copy the following libraries into this folder:
     - `board`
     - `touchio`
     - `rotaryio`
     - `usb_hid`
     - `neopixel`
     - `digitalio`
     - `time`
     - `adafruit_hid.keyboard`
     - `keyboard_layout_win_de`
     - `keycode_win_de`

### Usage Instructions

1. **Adding and Editing Text Files**:
   - Connect the NeoTrinkey to your computer.
   - It will appear as a USB flash drive named `CIRCUITPY`.
   - Create and save `.txt` files on this drive, naming them numerically (e.g., `1.txt`, `2.txt`, etc.).
   - You can edit these files directly on the drive using any text editor.

2. **Using the Script to Type Out Text Files**:
   - Connect the Trinkey to your computer.
   - Turn the rotary encoder to select a file based on its number.
   - The NeoPixel LED will flash x times based on the file number currently selected.
   - Press the switch on the Trinkey to start typing out the contents of the selected `.txt` file as keyboard input.

### Required Libraries

To run this script on the Adafruit Trinkey Rotary, the following libraries need to be copied onto the device:

- `board`
- `touchio`
- `rotaryio`
- `usb_hid`
- `neopixel`
- `digitalio`
- `time`
- `adafruit_hid.keyboard`
- `keyboard_layout_win_de`
- `keycode_win_de`

Ensure these libraries are included in your `lib` folder on the Trinkey.

## License

This script is distributed under the Affero General Public License (AGPL). The AGPL license ensures that all modifications and derived works based on this script are also open source and distributed under the same terms. For more information about the AGPL license, please visit [GNU's AGPL License page](https://www.gnu.org/licenses/agpl-3.0.html).


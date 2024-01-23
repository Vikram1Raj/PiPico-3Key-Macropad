print("Starting")

import board
import storage
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
keyboard.extensions.append(MediaKeys())

# Encoder wiring configuration
encoder_handler.pins = ((board.GP4, board.GP5, False),) 

# Keyboard matrix configuration
keyboard.col_pins = (board.GP18, board.GP19, board.GP20, board.GP21)
keyboard.row_pins = [board.GP16]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.Z, KC.X, KC.C, KC.MUTE]
]

encoder_handler.map = [((KC.VOLU,KC.VOLD),)]

if __name__ == '__main__':
    keyboard.go()

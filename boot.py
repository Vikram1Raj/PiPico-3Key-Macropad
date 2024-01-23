import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP18,  # column
    source=board.GP16, # row
    midi=False,
    mouse=False,
    storage=False,
    usb_id=('Pi-Pico Keypad', 'Custom 3 Key Macropad'),
)

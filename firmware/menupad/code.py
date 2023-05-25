import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence

# inits
keyboard = KMKKeyboard()
keyboard.debug_enabled = True
keyboard.col_pins = (board.D6, board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Key Defines
CMDSPC = simple_key_sequence((KC.LGUI(no_release=True), KC.SPACE, KC.LGUI(no_press=True)))

keyboard.keymap = [
    [
        KC.MPLY,      KC.MSTP,    KC.MRWD,      KC.MFFD,          KC.KP_1,
        KC.LALT,      KC.VOLD,    KC.VOLU,      KC.DELETE,        KC.KP_2,
        KC.LCTRL,     CMDSPC,     KC.UP,        KC.KP_ENTER,      KC.KP_3,
        KC.LGUI,      KC.LEFT,    KC.DOWN,      KC.RIGHT,         KC.KP_4,
    ]
]

if __name__ == '__main__':
    keyboard.go()
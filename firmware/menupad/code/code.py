import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence
#from kmk.modules.layers import Layers
#from kmk.modules.tapdance import TapDance
#from kmk.modules.sticky_mod import StickyMod
#from kmk.modules.modtap import ModTap

# inits
keyboard = KMKKeyboard()
keyboard.debug_enabled = True
keyboard.col_pins = (board.D6, board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# modules
#layers = Layers()
#LAYER_1 = KC.TG(1)
#keyboard.modules.append(layers)
#tapdance = TapDance()
#tapdance.tap_time = 150
#keyboard.modules.append(tapdance)
#stickymod = StickyMod()
#keyboard.modules.append(stickymod)
#modtap = ModTap()
#modtap.mod_time = 150
#keyboard.modules.append(modtap)

# Key Defines
CMDSPC = simple_key_sequence( KC.LGUI(no_release=True),KC.SPACE,KC.LGUI(no_press=True))

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
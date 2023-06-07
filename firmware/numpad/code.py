import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.sticky_mod import StickyMod
from kmk.modules.modtap import ModTap

# TODO: Make PASTE into PASTE_TT_PASTEVALUES

# inits
keyboard = KMKKeyboard()
keyboard.debug_enabled = True
keyboard.col_pins = (board.D6, board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# modules
layers = Layers()
LAYER_1 = KC.TG(1)
keyboard.modules.append(layers)
tapdance = TapDance()
tapdance.tap_time = 150
keyboard.modules.append(tapdance)
stickymod = StickyMod()
keyboard.modules.append(stickymod)
modtap = ModTap()
modtap.mod_time = 150
keyboard.modules.append(modtap)

# key defines
# simple
UNDO_Z = KC.LGUI(KC.Z)
REDO_Y = KC.LGUI(KC.Y)
COPY = KC.LGUI(KC.C)
PASTE = KC.LGUI(KC.V)
REDO_Z = simple_key_sequence(( KC.LGUI(KC.LSFT,no_release=True), KC.Z, KC.LGUI(KC.LSFT,no_press=True), ))
# TapDance
# Tap once for = and twice for numlock layer
EQUAL_TT_NUMLOCK = KC.TD(KC.KP_EQUAL,LAYER_1)
DELETE_TT_CLEAR = KC.DELETE # KC.TD(KC.DELETE,KC.SLCK)
ENTER_TT_TAB = KC.TD(KC.KP_ENTER,KC.TAB)
REDO_Y_TT_Z = KC.TD(REDO_Y,REDO_Z)
SLASH_TTT_PRNS = KC.TD(KC.KP_SLASH,KC.LPRN,KC.RPRN)
ZERO_H_WASD = KC.LT(2, KC.KP_0)
CMD_L = KC.LGUI(KC.LEFT)
CMD_R = KC.LGUI(KC.RIGHT)
DOT_H_LSFT = KC.MT(KC.KP_DOT, KC.LSFT, prefer_hold=True)
LHCL = KC.MT(KC.LEFT, KC.LGUI(KC.LEFT), prefer_hold=True)
RHCL = KC.MT(KC.RIGHT, KC.LGUI(KC.RIGHT), prefer_hold=True)
UHCL = KC.MT(KC.UP, KC.LGUI(KC.UP), prefer_hold=True)
DHCL = KC.MT(KC.DOWN, KC.LGUI(KC.DOWN), prefer_hold=True)
# StickyMod
CMD_TAB = KC.SM(kc=KC.TAB, mod=KC.LGUI)
CMD_SFTTAB = KC.SM(KC.TAB, KC.LSFT(KC.LGUI))

keyboard.keymap = [
    [
        KC.KP_7,      KC.KP_8,    KC.KP_9,      SLASH_TTT_PRNS,   EQUAL_TT_NUMLOCK,
        KC.KP_4,      KC.KP_5,    KC.KP_6,      KC.KP_ASTERISK,   DELETE_TT_CLEAR,
        KC.KP_1,      KC.KP_2,    KC.KP_3,      KC.KP_MINUS,      UNDO_Z,
        ZERO_H_WASD,  DOT_H_LSFT, ENTER_TT_TAB, KC.KP_PLUS,       REDO_Y_TT_Z,
    ],
    [
        KC.TRNS,      KC.UP,      KC.TRNS,      KC.TRNS,          KC.TRNS,
        KC.LEFT,      KC.TRNS,    KC.RGHT,      KC.TRNS,          KC.BSPC,
        KC.TRNS,      KC.DOWN,    KC.TRNS,      KC.TRNS,          COPY,
        KC.TRNS,      KC.TRNS,    KC.TAB,       KC.KP_ENTER,      PASTE,
    ],
    [
        KC.HOME,      CMD_L,      CMD_R,       KC.TRNS,          KC.TRNS,
        KC.END,       UHCL,       KC.END,      KC.TRNS,          KC.BSPC,
        LHCL,         DHCL,       RHCL,        KC.TRNS,          COPY,
        ZERO_H_WASD,  KC.TRNS,    CMD_TAB,     KC.KP_ENTER,      PASTE,
    ]
]


if __name__ == '__main__':
    keyboard.go()

""""
Xiao RP2040 Pin Assignments
#      D6   D3  D2  D1  D0
#  D10
#  D9
#  D8
#  D7

Keypad Layout

Base Layer
---------------------------
Numpad      :   As written
△           :   Tab
□           :   Plus
/           :   /
//, ///     :   (, )
✕           :   Undo
○, ○ ○      :   Redo (Cmd+Y) /(Cmd+Shft+Z)
==          :   Switch to Arrow Layer
Hold 0      :   Activates WASD / CmdTab layer while held

Arrow Layer ( [=][=] )
---------------------------
Arrow keys  :   Per numpad
Del         :   Backspace
[✕]         :   Copy
[○]         :   Paste
Square      :   Enter

WASD / CmdTab Layer (Momentary while 0 held)
---------------------------
  W               5
A S D       :   1 2 3
.           :   Cmd Tab
△           :   Cmd Shift Tab
□           :   Enter
✕           :   Copy
○           :   Paste
"""

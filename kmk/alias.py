from kmk.keys import KC
import unicode as UC
import macros as MC

________ = KC.TRNS
XXXXXXXX = KC.NO

# Layers
BASE    = 0
SHIFT   = 1
GREEK   = 2
SGREEK  = 3
SUPERS  = 4
SUBS    = 5
MC_PLY  = 6
MC_REC  = 7
B_BSPC  = 8
B_BRC   = 9

# Layer Switches
CLEAR       = KC.TO(0)
LM_LSFT    = KC.LM(SHIFT, KC.LSFT)
LM_RSFT    = KC.LM(SHIFT, KC.RSFT)

# Hold-Taps
KC_FRAC     = KC.HT(UC.FRACTION_SLASH, KC.LEADER)

# Modified Keys
BOT     = KC.LCTL(KC.END)
COPY    = KC.LCTL(KC.C)
CUT     = KC.LCTL(KC.X)
PASTE   = KC.LCTL(KC.V)
REDO    = KC.LCTL(KC.Y)
REPL    = KC.LCTL(KC.H)
TOP     = KC.LCTL(KC.HOME)
UNDO    = KC.LCTL(KC.Z)
WRDL    = KC.LCTL(KC.LEFT)
WRDR    = KC.LCTL(KC.RGHT)

# Custom Modified Keys
from customModifiedKey import CustomModifiedKey

N9      = CustomModifiedKey(KC.N9   , UC.DEG)
N0      = CustomModifiedKey(KC.N0   , MC.TRIPLE0)
LPRN    = CustomModifiedKey(KC.LPRN , KC.LCBR)
RPRN    = CustomModifiedKey(KC.RPRN , KC.RCBR)

P0      = CustomModifiedKey(KC.P0   , MC.DOUBLE0)
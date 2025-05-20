print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.scanners.digitalio import MatrixScanner
from kmk.scanners import digitalio

class MyKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()

        # create and register the scanner
        self.matrix = MatrixScanner(
            cols=self.col_pins,
            rows=self.row_pins,
            diode_orientation=self.diode_orientation,
            pull=digitalio.Pull.DOWN,
            rollover_cols_every_rows=None, # optional
        )

from kmk.modules.macros import Macros

macros = Macros()
keyboard.modules.append(macros)

keyboard = KMKKeyboard()

keyboard.col_pins = (
	board.GP17, 
	board.GP18, 
	board.GP19, 
	board.GP20, 
	board.GP21, 
	board.GP22, 
	board.GP23, 
	board.GP24, 
	board.GP25, 
	board.GP26,
	board.GP27,
	board.GP28,
	board.GP29,
	board.GP30)

keyboard.row_pins = (
	board.GP10,
	board.GP11,
	board.GP12,
	board.GP13,
	board.GP14,
	board.GP15,
	board.GP16)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
		MACRO_06	, MACRO_07	, MACRO_08	, MACRO_09	, MACRO_10	, MACRO_11	, MACRO_12	, MACRO_13	, MACRO_14	, MACRO_15	, MACRO_16	, MACRO_17	, MACRO_18	, MACRO_19	,
		KC.ESC		, KC.1		, KC.2		, KC.3		, KC.4		, KC.5		, KC.6		, KC.7		, KC.8		, KC.9		, KC.0		, KC.DASH	, KC.EQ		, MACRO_20	,
		KC.TAB		, KC.Q		, KC.W		, KC.E		, KC.R		, KC.T		, KC.Y		, KC.U		, KC.I		, KC.O		, KC.P		, KC.LBRK	, KC.RBRK	, KC.CAPS	,
		KC.BSPC		, KC.A		, KC.S		, KC.D		, KC.F		, KC.G		, KC.H		, KC.J		, KC.K		, KC.L		, KC.SCLN	, KC.QUOT	, KC.ENT	, KC.DEL	,
		KC.LSFT		, KC.NO		, KC.Z		, KC.X		, KC.C		, KC.V		, KC.B		, KC.N		, KC.M		, KC.COMM	, KC.DOT	, KC.SLSH	, KC.RSFT	, KC.NO		,
		KC.LALT		, KC.LGUI	, KC.LCTL	, KC.GRK	, KC.NO		, KC.LSFT	, KC.SPC	, KC.TAB	, KC.ENT	, KC.GRK	, KC.RCTL	, KC.RGUI	, KC.APPS	, KC.RALT
]

if __name__ == '__main__':
    keyboard.go()
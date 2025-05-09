# *Excelsior*
>![Excelsior](assets/excelsior.png)
>Tentative layout and design for *Excelsior*.

*Excelsior* is a 150% (153 keys) 3-section hand-wired keyboard (optionally) using uniform keycaps in a curved plate.

The main section is based on a standard ANSI 60% keyboard, but with a row of 15 function/programmable-macro keys at the top and 5 keys below the 7u spacebar.

The peripheral sections are each 6x6 ortholinear boards and can be placed on either side of the main section, including placing both on the same side of the main. They are connected to the main section by USB-C cables or male-male adapters. In the default keymap one section is an extended numpad and the other is a large navigation/macro pad. The top row of each peripheral is dedicated to additional function/programmable-macro keys for a total of 27.

The microcontroller is a Pro-Micro-compatible board located in the main section. The columns of the matrix are addressed by 74HC595 shift registers – two for the 14 columns of the main section and one in each peripheral for their 6 columns. The USB-C cables carry Vcc, Gnd, CLK, and OE for the shift registers plus one data line for each peripheral. The USB-C cables also carry 6 lines for the matrix rows. 

The matrix of the main section also has a seventh row that can be used for up to 14 momentary, toggle, or rotary switches on the top bezel of the keyboard. Note that the keys below the spacebar are on the sixth (spacebar) row of the matrix, so the seventh row is completely open.

Because of the shift registers the matrix only uses 12 pins, leaving at least 5 on a Pro-Micro controller for LEDs, rotary encoders, OLED screens, or even more switches if so desired.

For those interested, I have designed a [custom set](https://yuzukeycaps.com/c/f0f376b7-9989-43ee-8800-8b28918fe4d5) of KAM keycaps with a white-on-black-with-blue-accents *Wall Street Journal*-inspired aesthetic for *Excelsior* at YUZU Keycaps. They also feature secondary legends for a Greek alphabet/symbol layer and the macro keys are labeled with Greek numerals. There are a number of extra keys for alternative layouts too. Since the keycaps have a uniform profile any key can be placed on any row.
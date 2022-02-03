from adafruit_hid.keycode import Keycode
# You can still import Keycode and/or ConsumerControl as well if a macro file
# mixes types! See other macro files for typical Keycode examples.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Stream', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x200000, 'Switch', []),
        (0x202000, 'Switch', []),
        (0x002000, 'Switch', []),
        # 2nd row ----------
        (0x000000, '-----', []),
        (0x202020, '-----', []),
        (0x000000, '-----', []),
        # 3rd row ----------
        (0x000000, 'Discord', []),
        (0x200000, 'Mute', [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, 'm']),
        (0x000020, 'Deafen', [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, 'd']),
        # 4th row ----------
        (0x000000, 'Stream', []),
        (0x202020, 'Mute', []),
        (0x000000, 'Deafen', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

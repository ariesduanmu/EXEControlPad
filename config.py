# -*- coding: utf-8 -*-

from prompt_toolkit.styles import Style

DEFAULT_KEY_BINDINGS = {
    "focus_previous": ("s-tab", "left", "h", "j"),
    "focus_next": ("tab", "right", "l", "k"),
    "exit_clicked": ("q",),
}

style = Style(
    [
        ("left-pane", "bg:#888800 #000000"),
        ("right-pane", "bg:#00aa00 #000000"),
        ("button", "#000000"),
        ("button-arrow", "#000000"),
        ("button focused", "bg:#ff0000"),
        ("red", "#ff0000"),
        ("green", "#00ff00"),
    ]
)

EXE_DIR = ""
EXE_NAME = ""



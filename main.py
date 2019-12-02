# -*- coding: utf-8 -*-


from prompt_toolkit.application import Application

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next
from prompt_toolkit.key_binding.bindings.focus import focus_previous

from controllers import Controllers
from config import DEFAULT_KEY_BINDINGS
from config import style

from utils import exit_clicked

from view import basic_view

def act_rule():
    actions = {
        "focus_next": focus_next,
        "focus_previous": focus_previous,
        "exit_clicked": exit_clicked,
    }

    kb = KeyBindings()

    for action, keys in DEFAULT_KEY_BINDINGS.items():
        for key in keys:
            kb.add(key)(actions[action])
    return kb


controller = Controllers()
layout = basic_view(controller)

application = Application(layout=layout, key_bindings=act_rule(), style=style, full_screen=False)
application.run()
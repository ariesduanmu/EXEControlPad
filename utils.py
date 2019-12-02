# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import win32api

from prompt_toolkit.application.current import get_app

def exit_clicked():
    get_app().exit()


def run_exe(exe_path):
    '''run in bg
    '''
    try:
        win32api.ShellExecute(0, 'open', exe_path, '', '', 0)
        return True
    except:
        return False

def kill_exe(exe_name):
    _, err = subprocess.Popen(["taskkill", "/f", "/im", exe_name],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT).communicate()
    if not err:
        return None
    return err
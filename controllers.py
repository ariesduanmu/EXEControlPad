# -*- coding: utf-8 -*-
import os
import sys

from config import EXE_DIR
from config import EXE_NAME

from utils import run_exe
from utils import kill_exe

from model import exe_start
from model import exe_stop
from model import exe_config
from model import exe_log



class Controllers:
    def __init__(self):
        self.text_area = None
        self.label_exe_port = None

    def set_text_area(self, text_area):
        self.text_area = text_area

    def set_label_exe_port(self, label_exe_port):
        self.label_exe_port = label_exe_port

    # 控制方法
    def exe_start(self):
        
        if run_exe(os.path.join(EXE_DIR, EXE_NAME)):
            response = "success"
        else:
            response = "fail"

        if self.text_area:
            self.text_area.text = exe_start(response)

    def exe_stop(self):
        '''停止db服务
        '''
        err = kill_exe(EXE_NAME)

        if not err:
            response = "success"
        else:
            response = f"err:{err}"

        if self.text_area:
            self.text_area.text = exe_stop(response)

    def exe_config(self):
        if self.text_area:
            self.text_area.text = exe_config()

    def exe_logs(self):
        if self.text_area:
            self.text_area.text = exe_log()
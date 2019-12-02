# -*- coding: utf-8 -*-

from prompt_toolkit.layout import Window
from prompt_toolkit.layout import VSplit
from prompt_toolkit.layout import HSplit
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout import FormattedTextControl

from prompt_toolkit.widgets import Box
from prompt_toolkit.widgets import Button
from prompt_toolkit.widgets import Label

from utils import exit_clicked


def basic_view(controller):

    # 动态变化的控件，文本框/dbserver的端口/server的端口
    text_area = FormattedTextControl(focusable=False, show_cursor=False)
    label_exe_port = Label(text="", style="fg:#000000")

    controller.set_text_area(text_area)
    controller.set_label_exe_port(label_exe_port)

    text_window = Window(
        content=text_area, dont_extend_height=True, height=11, style="bg:#ffffff #000000"
    )

    # 退出按钮
    btn_exit = Button("Exit", handler=exit_clicked)

    # exe的控制按键
    btn_exe_start = Button("Start", handler=controller.exe_start)
    btn_exe_stop = Button("Stop", handler=controller.exe_stop)
    btn_exe_config = Button("Config", handler=controller.exe_config)
    btn_exe_log = Button("Logs", handler=controller.exe_logs)

    # 占位label
    label_empty = Label(text="", style="fg:#000000")

    # 主页面
    root_container = Box(
        HSplit(
            [
                VSplit(
                    [Label(text="Local Server",style="bg:#000000"), btn_exit],
                    padding=1, 
                    style="bg:#cccccc",
                ),

                VSplit(
                    [Label(text="EXE", style="fg:#000000"),
                     Label(text="PID", style="fg:#000000"),
                     Label(text="Actions", style="fg:#000000"),
                     label_empty,
                     label_empty,
                     label_empty],
                    padding=1, 
                    style="bg:#cccccc",
                ),
                
                VSplit(
                    [Label(text="EXE1", style="fg:#000000"),
                     label_exe_port,
                     btn_exe_start, 
                     btn_exe_stop, 
                     btn_exe_config, 
                     btn_exe_log], 
                    padding=1, 
                    style="bg:#cccccc",
                ),
                
                text_window
                
            ]
        )
    )
        
    layout = Layout(container=root_container, focused_element=btn_exe_start)

    return layout
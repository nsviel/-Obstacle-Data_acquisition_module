#! /usr/bin/python
#---------------------------------------------

from param import param_py
from src import device
from src import io
from src import lidar
from src import saving
from src import loop
from src import connection

from gui import gui_callback
from gui import gui_runtime
from gui import gui_parameter
from gui import gui_loop
from gui import scheme

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def start():
    dpg.create_context()

    #Build GUI
    with dpg.window(tag="window", label="Pywardium"):
        scheme.build_scheme()
        gui_parameter.build_parameter()
        gui_runtime.build_runtime()
        build_end()
        #demo.show_demo()

    #Main GUI theme
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (20, 20, 20), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (20, 20, 20))

    dpg.bind_theme(global_theme)
    dpg.create_viewport(title='Pywardium', width=param_py.gui_width, height=param_py.gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)

    # Init variables
    loop.init()

    # Start main loop program
    while param_py.run_loop and dpg.is_dearpygui_running():
        loop.loop()
        gui_loop.loop()
        dpg.render_dearpygui_frame()

    # End thread
    loop.end()

    # Finish program
    dpg.destroy_context()

def build_end():
    dpg.add_separator()
    dpg.add_button(label="close", tag="bclo", callback=gui_callback.callback_close)

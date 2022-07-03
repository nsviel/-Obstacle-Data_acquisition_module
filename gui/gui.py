#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import device
from src import io
from src import lidar
from src import saving
from src import loop
from src import connection

from gui import callback_gui
from gui import gui_connection
from gui import gui_runtime
from gui import gui_parameter
from gui import gui_scheme
from gui import gui_loop

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def start():
    dpg.create_context()

    #Build GUI
    with dpg.window(tag="window", label="Pywardium"):
        gui_scheme.build_scheme()
        gui_parameter.build_parameter()
        gui_connection.build_connection()
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
    dpg.create_viewport(title='Pywardium', width=parameter.gui_width, height=parameter.gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)

    # Init variables
    loop.init()

    # Start main loop program
    while parameter.run and dpg.is_dearpygui_running():
        loop.loop()
        gui_loop.loop()
        dpg.render_dearpygui_frame()

    # End thread
    connection.stop_thread()

    # Finish program
    dpg.destroy_context()

def build_end():
    dpg.add_separator()
    dpg.add_button(label="close", tag="bclo", callback=callback_gui.callback_event)
#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import device
from src import callback
from src import io
from src import lidar
from src import saving
from src import loop

from src import gui_connection
from src import gui_runtime
from src import gui_parameter

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def start():
    dpg.create_context()

    #Build GUI
    with dpg.window(tag="window", label="Pywardium"):
        gui_parameter.build_parameter()
        gui_connection.build_connection()
        gui_runtime.build_runtime()
        build_end()
        #demo.show_demo()

    dpg.create_viewport(title='Pywardium', width=parameter.gui_width, height=parameter.gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)

    # Init variables
    loop.init()

    # Start main loop program
    while parameter.run and dpg.is_dearpygui_running():
        loop.loop()
        dpg.render_dearpygui_frame()

    # Finish program
    dpg.destroy_context()

def build_end():
    dpg.add_separator()
    dpg.add_button(label="close", tag="bclo", callback=callback.callback_event)

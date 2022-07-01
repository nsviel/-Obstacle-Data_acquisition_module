#! /usr/bin/python
#---------------------------------------------

import dearpygui.dearpygui as dpg


def build_state():
    draw_size = 36
    square_idle = [150, 150, 150]
    link_idle = [150, 150, 150]
    space = 80

    #Pywardium
    draw_x = 4
    draw_y = 4
    dpg.draw_rectangle([draw_x, draw_y], [draw_size + draw_x, draw_size + draw_y], color=square_idle, fill=square_idle, tag="square_py")
    dpg.draw_line([draw_x + draw_size, (draw_size + draw_y)/2], [draw_x + draw_size + space, (draw_size + draw_y)/2], color=link_idle)

    #Hubium
    draw_x += draw_size + space
    dpg.draw_rectangle([draw_x, draw_y], [draw_size + draw_x, draw_size + draw_y], color=square_idle, fill=square_idle)
    dpg.draw_line([draw_x + draw_size, (draw_size + draw_y)/2], [draw_x + draw_size + space, (draw_size + draw_y)/2], color=link_idle)

    #Velodium
    draw_x += draw_size + space
    dpg.draw_rectangle([draw_x, draw_y], [draw_size + draw_x, draw_size + draw_y], color=square_idle, fill=square_idle)

    with dpg.theme() as square_idle:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 0, 0), category=dpg.mvThemeCat_Core)

    dpg.bind_item_theme("square_py", square_idle)

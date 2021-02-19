import numpy as np
from PIL import Image # For reading files
import matplotlib.pyplot as plt
from scipy import misc # image of a racoon
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from turtle import Turtle, Screen, shape, onscreenclick, mainloop
from turtle_clr import TurtleClr, PodiumPosition, ShowColor

TOP_COLORS = 5

def identify_colors(np_array):
    """Iterates over each pixel and stores the colors in a dictionary, value stores the count"""
    clr_dict = {}
    for i in np_array:
        for j in i:
            rgb_string = ""
            for k in j:
                if len(rgb_string) == 0:
                    rgb_string += str(k)
                else:
                    rgb_string += "-" + str(k)
            # Check if color exists in color dictionary and log occurrence
            if rgb_string not in clr_dict:
                clr_dict[rgb_string] = 1
            else:
                clr_dict[rgb_string] += 1
    return clr_dict


def sort_dict(input_dict):
    """sort dictionary by values in reverse order"""
    return {k: v for k, v in sorted(input_dict.items(), key=lambda item: item[1],reverse=True)}

def str_to_rgb(str_input):
    """takes a rgb concatenated string and returns an rgb set"""
    arr = str_input.split("-")
    return int(arr[0]), int(arr[1]), int(arr[2])

def get_top_colors(dict,num_cols):
    x = 0
    output_list = []
    for key in dict.keys():
        x += 1
        output_list.append(str_to_rgb(key))
        if x < num_cols:
            pass
        else:
            break
    return output_list

# Store Image
img = misc.face()
clr_dict = sort_dict(identify_colors(img))  # Store colors in sorted dictionary

# SHOW ORIGINAL IMAGE
# root = tk.Tk()
# root_panel = tk.Frame(root)
# fig = Figure()
# a = fig.add_subplot(111)
# a.imshow(img)
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.draw()
# canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
# canvas._tkcanvas.pack(side="top", fill="both", expand=1)
#
# root.mainloop()

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.title(f"Top {TOP_COLORS} most common colors in picture")

top_colors = get_top_colors(dict=clr_dict,num_cols=TOP_COLORS)

print(len(top_colors))

pos = 0
for clr in top_colors:
    pos += 1
    # Show color (np)
    ShowColor(clr=clr, position=pos)
    # Show color
    TurtleClr(clr=clr, position=pos)
    # Show Podium Position
    PodiumPosition(position=pos)

screen.exitonclick()

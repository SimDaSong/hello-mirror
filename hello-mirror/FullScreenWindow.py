from tkinter import *

from BusTimeSchedule import BusTimeSchedule
from Calendar import Calendar
from Clock import Clock
from News import News
from Weather import Weather

from constants import bg_color


class FullscreenWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background=bg_color)

        self.rightFrame = Frame(self.tk, background=bg_color)
        Clock(self.rightFrame).pack(side=TOP, anchor=E, padx=80, pady=50)
        Calendar(self.rightFrame).pack(side=BOTTOM, anchor=E, padx=80, pady=50)
        BusTimeSchedule(self.rightFrame).pack(side=BOTTOM, anchor=E, padx=80, pady=50)
        self.rightFrame.pack(side=RIGHT, fill=Y)

        self.leftFrame = Frame(self.tk, background=bg_color)

        Weather(self.leftFrame).pack(side=TOP, anchor=NW, padx=80, pady=50)
        News(self.leftFrame).pack(side=BOTTOM, anchor=SW, padx=80, pady=50)
        self.leftFrame.pack(side=LEFT, fill=Y)

        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        Weather.get_weather()
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        Weather.get_weather()
        return "break"

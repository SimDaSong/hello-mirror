from tkinter import *

from CalendarEvent import CalendarEvent
from constants import medium_text_size, bg_color, font_color, font


class Calendar(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg=bg_color)

        self.title = "캘린더"
        self.calendarLbl = Label(self, text=self.title, font=(font, medium_text_size), fg=font_color,
                                 bg=bg_color)
        self.calendarLbl.pack(side=TOP, anchor=E)
        self.calendarEventContainer = Frame(self, bg=bg_color)
        self.calendarEventContainer.pack(side=TOP, anchor=E)
        self.get_events()

    def get_events(self):
        # remove all children
        for widget in self.calendarEventContainer.winfo_children():
            widget.destroy()

        calendar_event = CalendarEvent(self.calendarEventContainer)
        calendar_event.pack(side=TOP, anchor=E)
        pass

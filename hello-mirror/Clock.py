from tkinter import *
import time

from constants import *
from helpers import setLocale


class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg=bg_color)
        # initialize time label
        self.day_week1 = None
        self.time1 = ""
        self.timeLbl = Label(self, font=(font, large_text_size), fg=font_color, bg=bg_color)
        self.timeLbl.pack(side=TOP, anchor=E)
        # initialize day of week
        self.day_of_week1 = ""
        self.dayOWLbl = Label(self, text=self.day_of_week1, font=(font, medium_text_size), fg=font_color,
                              bg=bg_color)
        self.dayOWLbl.pack(side=TOP, anchor=E)
        self.date1 = ""
        self.dateLbl = Label(self, text=self.date1, font=(font, medium_text_size), fg=font_color, bg=bg_color)
        self.dateLbl.pack(side=TOP, anchor=E)
        self.tick()

    def tick(self):

        with setLocale(ui_locale):
            if time_format == 12:
                time2 = time.strftime("%p %I시 %M분")  # hour in 12h format
            else:
                time2 = time.strftime("%H:%M")  # hour in 24h format

            day_of_week2 = weekday_kr[time.localtime().tm_wday] + "요일"
            date2 = time.strftime(date_format)
            # 실시간으로 바꾸는 코드
            if day_of_week2 != self.day_of_week1:
                self.day_week1 = day_of_week2
                self.dayOWLbl.config(text=day_of_week2)
            if time2 != self.time1:
                self.time1 = time2
                self.timeLbl.config(text=time2)
            if date2 != self.date1:
                self.date1 = date2
                self.dateLbl.config(text=date2)
            # calls itself every 200 milliseconds
            # to update the time display as needed
            # could use >200 ms, but display gets jerky
            self.timeLbl.after(200, self.tick)

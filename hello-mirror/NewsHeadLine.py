from tkinter import *
from PIL import Image, ImageTk

from constants import small_text_size, bg_color, font_color, font


class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg=bg_color)

        image = Image.open("assets/Newspaper.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert("RGB")
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg=bg_color, image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=N)

        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=(font, small_text_size), fg=font_color,
                                  bg=bg_color)
        self.eventNameLbl.pack(side=LEFT, anchor=N)

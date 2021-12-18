from tkinter import *
from PIL import Image, ImageTk

from constants import bg_color


class BusTimeSchedule(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg=bg_color)

        self.title = "셔틀버스운행시간표"
        image = Image.open("assets/BusTimeSchedule.png")  # 원본 해상도: 1280x2676
        image = image.resize((287, 600), Image.ANTIALIAS)
        image = image.convert("RGB")
        photo = ImageTk.PhotoImage(image)

        self.imageLbl = Label(self, bg=bg_color, image=photo)
        self.imageLbl.image = photo
        self.imageLbl.pack(side=RIGHT)

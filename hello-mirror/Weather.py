from tkinter import *
import requests
import json
import traceback
from PIL import Image, ImageTk

from constants import *


class Weather(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg=bg_color)
        self.temperature = ""
        self.forecast = ""
        self.location = ""
        self.currently = ""
        self.icon = ""
        self.degreeFrm = Frame(self, bg=bg_color)
        self.degreeFrm.pack(side=TOP, anchor=W)
        self.temperatureLbl = Label(self.degreeFrm, font=(font, temperture_text_size), fg=font_color, bg=bg_color)
        self.temperatureLbl.pack(side=LEFT, anchor=N)
        self.iconLbl = Label(self.degreeFrm, bg=bg_color)
        self.iconLbl.pack(side=LEFT, anchor=N, padx=20)
        self.currentlyLbl = Label(self, font=(font, medium_text_size), fg=font_color, bg=bg_color)
        self.currentlyLbl.pack(side=TOP, anchor=W)
        self.forecastLbl = Label(self, font=(font, small_text_size), fg=font_color, bg=bg_color)
        self.forecastLbl.pack(side=TOP, anchor=W)
        self.locationLbl = Label(self, font=(font, small_text_size), fg=font_color, bg=bg_color)
        self.locationLbl.pack(side=TOP, anchor=W)
        self.get_weather()

    def get_ip(self):
        try:
            ip_url = "http://ip.jsontest.com"
            ip = requests.get(ip_url).json()["ip"]

            return ip
        except Exception as e:
            traceback.print_exc()
            return "Error: %s. Cannot get ip." % e

    def get_weather(self):
        try:
            if latitude is None and longitude is None:
                # get location
                location_req_url = "http://api.ipstack.com/%s?access_key=%s" % (self.get_ip(), ipstack_access_key)
                r = requests.get(location_req_url)
                location_obj = json.loads(r.text)

                lat = location_obj["latitude"]
                lon = location_obj["longitude"]

                location2 = "%s, %s" % (location_obj["city"], location_obj["region_code"])

                # get weather
                weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s?lang=%s&units=%s" % (
                    weather_api_token, lat, lon, weather_lang, weather_unit)
            else:
                location2 = "?????? ????????? ????????????"
                # get weather
                weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s?lang=%s&units=%s" % (
                    weather_api_token, latitude, longitude, weather_lang, weather_unit)

            r = requests.get(weather_req_url)
            weather_obj = json.loads(r.text)

            degree_sign = '\u2103'
            temperature2 = "%s%s" % (
            str(int(self.convert_kelvin_to_celsius(weather_obj['currently']['temperature']))), degree_sign)
            currently2 = weather_obj['currently']['summary']
            forecast2 = weather_obj["hourly"]["summary"]

            icon_id = weather_obj['currently']['icon']
            icon2 = None

            if icon_id in icon_lookup:
                icon2 = icon_lookup[icon_id]

            if icon2 is not None:
                if self.icon != icon2:
                    self.icon = icon2
                    image = Image.open(icon2)
                    image = image.resize((100, 100), Image.ANTIALIAS)
                    image = image.convert('RGBA')
                    photo = ImageTk.PhotoImage(image)

                    self.iconLbl.config(image=photo)
                    self.iconLbl.image = photo
            else:
                # remove image
                self.iconLbl.config(image='')

            # ??????????????? ????????? ??????
            if self.currently != currently2:
                self.currently = currently2
                self.currentlyLbl.config(text=currently2)
            if self.forecast != forecast2:
                self.forecast = forecast2
                self.forecastLbl.config(text=forecast2)
            if self.temperature != temperature2:
                self.temperature = temperature2
                self.temperatureLbl.config(text=temperature2)
            if self.location != location2:
                if location2 == ", ":
                    self.location = "Cannot Pinpoint Location"
                    self.locationLbl.config(text="Cannot Pinpoint Location")
                else:
                    self.location = location2
                    self.locationLbl.config(text=location2)
        except Exception as e:
            traceback.print_exc()
            print(("Error: %s. Cannot get weather." % e))

        self.after(600000, self.get_weather)

    @staticmethod
    def convert_kelvin_to_celsius(kelvin_temp):
        return (kelvin_temp - 32) / 1.8

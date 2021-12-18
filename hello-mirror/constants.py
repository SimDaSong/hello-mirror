import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

ui_locale = ""  # e.g. 'fr_FR' fro French, '' as default
time_format = 24  # 12 or 24
date_format = "%Y년 %m월 %d일"  # check python doc for strftime() for options
news_country_code = "kr"
weather_api_token = os.getenv("WEATHER_API_TOKEN")  # create account at https://darksky.net/dev/
weather_lang = "ko"  # see https://darksky.net/dev/docs/forecast for full list of language parameters values
weather_unit = "us"  # see https://darksky.net/dev/docs/forecast for full list of unit parameters values
latitude = None  # "36.604303"  # Set this if IP location lookup does not work for you (must be a string)
longitude = None  # "127.298525"  # Set this if IP location lookup does not work for you (must be a string)
xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18
temperture_text_size = 60
bg_color = "black"
font_color = "white"
font = "NanumBarunGothic"
ipstack_access_key = os.getenv("IPSTACK_ACCESS_KEY")
weekday_kr = ["월", "화", "수", '목', '금', '토', '일']

# 날씨 아이콘 이미지
# maps open weather icons to
# icon reading is not impacted by the 'lang' parameter
icon_lookup = {
    'clear-day': "assets/Sun.png",  # clear sky day
    'wind': "assets/Wind.png",  # wind
    'cloudy': "assets/Cloud.png",  # cloudy day
    'partly-cloudy-day': "assets/PartlySunny.png",  # partly cloudy day
    'rain': "assets/Rain.png",  # rain day
    'snow': "assets/Snow.png",  # snow day
    'snow-thin': "assets/Snow.png",  # sleet day
    'fog': "assets/Haze.png",  # fog day
    'clear-night': "assets/Moon.png",  # clear sky night
    'partly-cloudy-night': "assets/PartlyMoon.png",  # scattered clouds night
    'thunderstorm': "assets/Storm.png",  # thunderstorm
    'tornado': "assets/Tornado.png",  # tornado
    'hail': "assets/Hail.png"  # hail
}

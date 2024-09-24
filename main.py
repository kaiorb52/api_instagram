# main.py

# Instagram	 https://console.apify.com/actors/shu8hvrXbJbY3Eb9W/input
# facebook   https://console.apify.com/actors/KoJrdxJCTtpon81KY/input

from google_sheet import *
from api_key import client
from constants import dia_atual,ontem, run
from midia_scraper import midia_sraper

# insta_urls_test = insta_urls[0:2]
# face_urls_test  = face_urls[0:2]

while run == True:
    midia_sraper(client, instagram_test, "instagram", data = "2024-09-16", daily = False)
    midia_sraper(client, facebook_test,  "facebook", data = "2024-09-16", daily = False)
    run = False


# main.py

# Instagram	 https://console.apify.com/actors/shu8hvrXbJbY3Eb9W/input
# facebook   https://console.apify.com/actors/KoJrdxJCTtpon81KY/input

from google_sheet import *
from api_key import client
from constants import dia_atual,ontem, run, x
from midia_scraper import midia_sraper

insta_urls_test = insta_urls[0:2]
face_urls_test  = face_urls[0:2]

while run == True:
    midia_sraper(client, insta_urls_test, "instagram")
    midia_sraper(client, face_urls_test,  "facebook")
    run = False

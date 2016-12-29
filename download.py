#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from emojis import emojis
from bs4 import BeautifulSoup
import PIL
from PIL import Image
import json
import os

if not os.path.exists("emojis/"):
    os.mkdir("emojis")

emojis_pngs = {}
if os.path.exists("emojis.json"):
    f = open("emojis.json", "r")
    emojis_pngs = json.load(f)
    f.close()

count = 0
for emoji in emojis:
    if emoji in emojis_pngs:
        print "Emoji '%s' already downloaded" % emoji
        continue

    count += 1
    url = 'http://emojipedia.org/search/?q=%s' % emoji
    try:
        redirect_url = requests.get(url).url
        content_html = requests.get(redirect_url)
        content = BeautifulSoup(content_html.text, "lxml")
        divs = content.find_all(
            "div", class_="vendor-container vendor-rollout-target")
        emoji_url = None

        for div in divs:
            subdiv = div.find_all("div", class_="vendor-info")
            suburl = div.find_all("div", class_="vendor-image")
            img = suburl[0].find_all("img")
            h2 = subdiv[0].find_all("h2")
            vendor = h2[0].text
            if vendor == "Messenger":
                emoji_url = img[0].get('src')
                break

        emoji_path = "emojis/%s.png" % count
        emojis_pngs[emoji] = emoji_path
        emoji_data = requests.get(emoji_url)
        f = open(emoji_path, "w")
        f.write(emoji_data.content)
        f.close()

        # Resized to 32x32
        # https://opensource.com/life/15/2/resize-images-python
        img = Image.open(emoji_path)
        wpercent = (32 / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((32, hsize), PIL.Image.ANTIALIAS)
        img.save(emoji_path)
    except Exception as e:
        emojis_pngs[emoji] = "Not available"

    f = open("emojis.json", "w")
    json.dump(emojis_pngs, f, indent=4)
    f.close()

    print "Emoji '%s' downloaded to '%s'" % (emoji, emoji_path)

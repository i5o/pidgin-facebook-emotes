#!/usr/bin/env python
# -*- coding:utf-8 -*-

import zipfile
import json
import os

header = """Name=Facebook Messenger
Description=Messenger smileys for Pidgin
Icon=1.png
Author=ignacio

[default]
"""
theme = header

f = open("emojis.json", "r")
data = json.load(f)
f.close()

if os.path.exists("theme.zip"):
    os.remove("theme.zip")

zf = zipfile.ZipFile("theme.zip", "w", zipfile.ZIP_DEFLATED)
for key in data.keys():
    if data[key] == "Not available":
        continue

    theme += "%s\t%s\n" % (data[key][7:], key)
    try:
        zf.write(data[key], "FacebookMessenger/%s" % data[key][7:])
    except:
        print "Error"

print theme
f = open("theme", "w")
f.write(theme.encode("utf-8"))
f.close()

zf.write("theme", "FacebookMessenger/theme")
zf.close()

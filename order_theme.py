#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

f = open("theme", "r")
data = f.read()
f.close()

w = open("theme_backup", "w")
w.write(data)
w.close()

lines = data.splitlines()
new_theme_file = ""
limit = 6
current = 0
while current < limit:
    new_theme_file += lines[current] + "\n"
    current += 1

emojis = lines[6:]

emojis_data = {}
for emoji in emojis:
    s = emoji.split("\t")
    emojis_data[int(s[0][:-4])] = s[1]

for emoji in sorted(emojis_data):
    if os.path.exists(
        "/usr/share/pixmaps/pidgin/emotes/FacebookMessenger/%d.png" %
            emoji):
        new_theme_file += "%d.png\t%s\n" % (emoji, emojis_data[emoji])

w = open("theme", "w")
w.write(new_theme_file)
w.close()

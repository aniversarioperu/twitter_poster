# -*- coding: utf-8 -*-
import re
import codecs
import json
"""Input emoji in JSON, output for our script twitter_poster"""

out = ""
f = codecs.open("emoji.json")
for i in f.readlines():
    i = json.loads(i)
    out += "'" + i['description'].lower() + "': "
    out += "u'\U000" + re.sub("U\+", "", i['code']) + "',\n"
f.close()

print out

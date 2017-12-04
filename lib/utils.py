#============================================================================
#Мусорка мини функций
#============================================================================

import os
import asyncio
import json
#import bleach
import re
import html
import xmltodict
#from collections import OrderedDict
from operator import itemgetter
from bs4 import BeautifulSoup
#from bs4 import NavigableString
from config import config

async def cmdGetParams(cmd):
    self.parsed = cmd.split()
    self.stmp = ""
    for self.elem in self.parsed:
        if self.elem.startswith('!'):
            continue
        if self.stmp != "":
            self.stmp += " "
        self.stmp += self.elem
    return self.stmp

def getVersion():
    with open('version', encoding='utf-8') as version_file:
        version_data = json.loads(version_file.read())
    return version_data['version']


class AuthUtils():
    async def get_auth_group_ids(self):
        print(config.auth["authGroups"])
        self.alliance_ids = []
        for self.group_key, self.group_value in config.auth["authGroups"].items():
            self.alliance_ids.append(self.group_value["id"])
        print(self.alliance_ids)
        return self.alliance_ids

    async def is_auth_exempt(self, roles):
        self.is_exempt = False
        print(config.auth['exempt'])
        print(roles)
        for self.role in roles:
            if self.role.name in config.auth['exempt']:
                self.is_exempt = True
                break
        return self.is_exempt

    async def get_auth_group_values(self, allianceID):
        for self.group_key, self.group_value in config.auth["authGroups"].items():
            if self.group_value["id"] == allianceID:
                self.values = self.group_value
                del self.group_key
                del self.group_value
                break
        return self.values


class MailUtils():
    async def clean_html(raw_html):
        #cleanr = re.compile('<.*?>')
        #cleantext = re.sub(cleanr, '', raw_html)
        clean = bleach.clean(raw_html, tags=[], strip=True)
        return clean

    async def xml_to_dict(xml, type):
        try:
            if xml is None:
                return None
            if type is None:
                return None
            if type == "test":
                #data = xmltodict.parse(xml, dict_constructor=dict)
                data = xmltodict.parse(xml)
                data = data["eveapi"]["result"]["rowset"]["row"]
                data = sorted(data, key=itemgetter('@sentDate'))
                return data
            else:
                data = xmltodict.parse(xml)
            if type == "mails":
                data = data["eveapi"]["result"]["rowset"]["row"]
                data = sorted(data, key=itemgetter('@sentDate'))
            if type == "content":
                data = data["eveapi"]["result"]["rowset"]["row"]["#text"]
            return data
        except Exception as e:
            print(e)
            return None

    async def format_mailbody(txt):
        txt = txt.replace("<br>","\n")
        #print("Replaced <br>:\n{}".format(txt))
        txt = BeautifulSoup(txt, 'html.parser')
        for tag in txt.findAll('a'):
            if re.search("^showinfo:", tag["href"]):
                tag.unwrap()
                continue
            href = tag['href']
            href = href.replace("fitting:","https://o.smium.org/loadout/dna/")
            href = href.replace("::", "\n")
            tag.replaceWith(href)
        #print("Replaced href:\n{}".format(txt))
        #clean = bleach.clean(txt, tags=[], strip=True)
        for tag in txt.findAll(True):
        #    tag.replaceWithChildren()
            tag.unwrap()
        #print("Deleted all other tags:\n{}".format(txt))
        txt = html.unescape(str(txt))
        return txt

    # PHP like string split
    async def str_split(s, n):
        ret = []
        s = str(s)
        try:
            for i in range(0, len(s), n):
                ret.append(s[i:i+n])
            return ret
        except Exception as e:
            print(e)
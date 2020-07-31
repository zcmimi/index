#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
os.system("pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple")

import mistune
import time
import yaml
from encrypt import encrypt
from jinja2 import Environment,FileSystemLoader

aboutme=mistune.markdown(open("aboutme.md",encoding="utf-8").read())

try:yamloader=yaml.CLoader
except:yamloader=yaml.SafeLoader

links={}
for i in os.listdir("links"):
    if not os.path.isdir("links/"+i):continue
    links[i]=[]
    for j in os.listdir("links/"+i):
        if not os.path.exists("links/"+i+"/"+j+"/config.yml"):continue
        x=yaml.load(open("links/"+i+'/'+j+"/config.yml").read(),Loader=yamloader)
        if "//" not in x["avatar"]:x["avatar"]='/'.join(["links",i,j,x["avatar"]])
        links[i].append(x)

env=Environment(loader=FileSystemLoader('.'))
env.trim_blocks=True
env.lstrip_blocks=True

template=env.get_template("index.j2")

open("index.html","w",encoding="utf-8").write(template.render(
    aboutme=aboutme,
    catchme="",
    links=links,
    time=time.strftime("%Y-%m-%d",time.localtime())
))
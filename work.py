#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pip
pip._internal.main([
    "install","-r","requirement.txt",
    "-i","https://pypi.tuna.tsinghua.edu.cn/simple"
])

import mistune
import time
import yaml
from encrypt import encrypt
from jinja2 import Environment,FileSystemLoader

aboutme=mistune.markdown(open("aboutme.md",encoding="utf-8").read())

try:
    links=yaml.load(open("links.yml",encoding="utf-8").read(),Loader=yaml.CLoader)
except:
    links=yaml.load(open("links.yml",encoding="utf-8").read())

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
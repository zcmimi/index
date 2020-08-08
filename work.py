#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os,time
import mistune

try:
    import yaml
    from jinja2 import Environment,FileSystemLoader
except:
    os.system("pip3 install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple")
    import yaml
    from jinja2 import Environment,FileSystemLoader

aboutme=mistune.markdown(open("aboutme.md",encoding="utf-8").read(),escape=False)
catchme=mistune.markdown(open("catchme.md",encoding="utf-8").read(),escape=False)
project=mistune.markdown(open("project.md",encoding="utf-8").read(),escape=False)

try:yamloader=yaml.CLoader
except:yamloader=yaml.SafeLoader

links={}
for i in os.listdir("links"):
    if not os.path.isdir("links/"+i):continue
    links[i]=[]
    for j in os.listdir("links/"+i):
        if not os.path.exists("links/"+i+"/"+j+"/config.yml"):continue
        x=yaml.load(open("links/"+i+'/'+j+"/config.yml").read(),Loader=yamloader)
        if "//" not in x["avatar"]:x["avatar"]='/'+'/'.join(["links",i,j,x["avatar"]])
        links[i].append(x)

open("links.yml","w",encoding="utf-8").write(yaml.dump(links))

env=Environment(loader=FileSystemLoader('.'))
env.trim_blocks=True
env.lstrip_blocks=True

template=env.get_template("index.j2")

open("index.html","w",encoding="utf-8").write(template.render(
    aboutme=aboutme,
    catchme=catchme,
    project=project,
    links=links,
    time=time.strftime("%Y-%m-%d",time.localtime())
))
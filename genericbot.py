#!/usr/bin/python
import frontmatter
import io
import datetime
import glob

title = raw_input('Title: ')
content = raw_input('Content: ')
layout = "post"
date = datetime.datetime.now().strftime("%Y-%m-%d")
time = "07:00:00.000000000 -5:00"
titleDash = title.replace(' ', '-')
dateTime = date +" "+ time
fileName = date+"-"+titleDash + ".md"

file = open(fileName, "w+")
post = frontmatter.load(fileName)
post['layout'] = "post"
post['title'] = title
post['date'] = dateTime 
with open(fileName, "w") as f:
    f.write(frontmatter.dumps(post)+ '\n')
with open(fileName, 'a') as f:
    f.write(content+ '\n')

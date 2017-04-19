#!/usr/bin/python
##Automating Generic out of a Job
import frontmatter
import io
import datetime
import shutil
import git
import Repo
 
#Getting Information for Post
title = raw_input('Title: ')
content = raw_input('Content: ')
layout = "post"
date = datetime.datetime.now().strftime("%Y-%m-%d")
time = "07:00:00.000000000 -5:00"
titleDash = title.replace(' ', '-')
dateTime = date +" "+ time
fileName = date+"-"+titleDash + ".md"

#Creating .md
file = open(fileName, "w+")
post = frontmatter.load(fileName)
post['layout'] = "post"
post['title'] = title
post['date'] = dateTime 
with open(fileName, "w") as f:
    f.write(frontmatter.dumps(post)+ '\n')
with open(fileName, 'a') as f:
    f.write(content+ '\n')

#Moving .md file to git repo
src = fileName
dst = "/home/user/Documents/csg/csg-website/_posts/17S"
shutil.move(src,dst)

#Pushing .md file to git repo

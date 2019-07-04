#!/usr/bin/env python3

import os
from github import Github
import json

with open(os.getenv('HOME') + '/.git-token-gen-json') as f:
    token = f.readline()
    f.close()

token = token.rstrip("\n")
print("token: ", token)

# or using an access token
g = Github(token)
repo = g.get_repo("matjam/hd-wallpapers")
contents = repo.get_contents("wallpapers")

images = []

for content_file in contents:
    image = {}
    image["url"] = content_file.download_url
    images.append(image)

print(json.dumps(images, indent=2))

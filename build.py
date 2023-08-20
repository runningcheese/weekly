import os
import httpx
import re
import urllib.parse
import datetime
import json

with open("config.json", "r", encoding="utf-8") as f:
  CONFIG = json.load(f)

def fetch_ci_time(filePath):
    entries = httpx.get("https://api.github.com/repos/"+ CONFIG["repo"] +"/commits?path=" + filePath + "&page=1&per_page=1")
    ciTime= entries.json()[0]["commit"]["committer"]["date"].split("T")[0]
    return ciTime
    # return datetime.datetime.strptime(ciTime,"%Y-%m-%d")

if __name__ == "__main__":
  readmefile=open('README.md','w')
  readmefile.write("# "+CONFIG["title"] +"\n\n>"+"查看[Deploy](https://github.com/"+CONFIG["repo"]+"/blob/main/Deploy.md)文档自行部署\n\n")
  recentfile=open('RECENT.md','w')

  for root, dirs, filenames in os.walk('./src/pages/posts'):
    filenames = sorted(filenames, key=lambda x:float(re.findall("(\d+)",x)[0]), reverse=True)

  for index, name in enumerate(filenames):
      if name.endswith('.md'):
        filepath = urllib.parse.quote(name)
        oldTitle = name.split('.md')[0]

        url   = CONFIG["homePage"]+'/posts/' + oldTitle
        title = '第 ' + oldTitle.split('-')[0] + ' 期 - ' + oldTitle.split('-')[1]
        readmeMd= '* [{}]({})\n'.format(title, url)
        num = int(oldTitle.split('-')[0])
        if index < 5 :
          if num < 100 :
            modified = fetch_ci_time('/src/pages/posts/' + filepath)
          else :
            modified = fetch_ci_time('/src/pages/posts/' + filepath)
          recentMd= '* [{}]({}) - {}\n'.format(title, url, modified)
          recentfile.write(recentMd)
        readmefile.write(readmeMd)

  recentfile.close()
  readmefile.close()

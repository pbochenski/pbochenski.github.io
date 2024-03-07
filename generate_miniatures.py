import os
import sys
from wand.image import Image
from pathlib import Path
import datetime

def get_arg(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

fileCount = len(next(os.walk("/Users/pawel.bochenski/Documents/kod/moje/pbochenski.github.io/media/thumbs"))[2])
newFileName = newFileName = '{0:03d}.jpg'.format(fileCount)

if get_arg(1) != '':
    fileName = sys.argv[1]
    newFileName = '{0:03d}.jpg'.format(fileCount + 1)
    fileCount = fileCount + 1
    print("generating miniatures for file {0}".format(fileName))
    with Image(filename=fileName) as img:
        with img.clone() as thumb:
            thumb.resize(120, 120)
            thumb.save(filename="media/thumbs/{0}".format(newFileName))
        with img.clone() as small:
            small.transform(resize="300^>")
            small.save(filename="media/small/{0}".format(newFileName))
        with img.clone() as large:
            large.transform(resize="1000^>")
            large.save(filename="media/large/{0}".format(newFileName))
else:
    print("no input param, miniatures creation skipped")

dir_name = "./media/large"
list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)), os.listdir(dir_name) ) )
for file_name in list_of_files:
    file = Path(file_name).stem
    if Path("./_gallery/{0}.md".format(file)).exists():
      print("File {0} exists, skipping".format(file))
    else:
      print("creating metadata file for {0}".format(file))
      with open("./_gallery/{0}.md".format(file), 'w') as f:
        file_content=fr"""---
filename: {file}.jpg
large: media/large/{file}.jpg
small: media/small/{file}.jpg
thumb: media/thumbs/{file}.jpg
date: {datetime.datetime.now().strftime("%Y.%m.%d")}
name: t.b.d
---
"""
        f.write(file_content)
import os, sys
from wand.image import Image

fileName = sys.argv[1]
fileCount = len(next(os.walk("/Users/bochen/Documents/kod/pbochenski.github.io/media/thumbs"))[2])
newFileName = '{0:03d}.jpg'.format(fileCount +1)

with Image(filename=fileName) as img:
    with img.clone() as thumb:
        thumb.resize(120,120)
        thumb.save(filename="media/thumbs/{0}".format(newFileName))
    with img.clone() as small:
        small.transform(resize="300^>")
        small.save(filename="media/small/{0}".format(newFileName))
    with img.clone() as large:
        large.transform(resize="1000^>")
        large.save(filename="media/large/{0}".format(newFileName))

print("update gallery md with file {0}".format(newFileName))
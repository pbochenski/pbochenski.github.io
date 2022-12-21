import os
import sys
from wand.image import Image


def get_arg(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


if get_arg(1) != '':
    if get_arg(2) != '':
        fileName = get_arg(2)
        post = get_arg(1)

        folder = "/Users/bochen/Documents/kod/pbochenski.github.io/assets/images/{0}/".format(post)
        os.makedirs(folder, exist_ok=True)
        fileCount = int(len(next(os.walk(folder))[2]) / 3)
        newFileName = newFileName = '{0:03d}.jpg'.format(fileCount)

        with Image(filename=fileName) as img:
            with img.clone() as thumb:
                thumb.resize(120, 120)
                thumb.save(filename="{0}/thumb_{1}".format(folder, newFileName))
            with img.clone() as small:
                small.transform(resize="300^>")
                small.save(filename="{0}/small_{1}".format(folder, newFileName))
            with img.clone() as large:
                large.transform(resize="1000^>")
                large.save(filename="{0}/large_{1}".format(folder, newFileName))

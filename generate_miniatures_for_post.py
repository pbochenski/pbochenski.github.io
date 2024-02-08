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
    
def createMiniatures(post, fileName):
    folder = "/Users/pawel.bochenski/Documents/kod/pbochenski.github.io/assets/images/{0}/".format(post)
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
    
    print("""<div
            class="albumList"
            data-sub-html=""
            data-download-url="../assets/images/{1}/large_{0}"
            data-src="../assets/images/{1}/large_{0}"
            data-exthumbimage="../assets/images/{1}/thumb_{0}"
            >
            <a href="../assets/images/{1}/large_{0}">
            <img src="../assets/images/{1}/small_{0}" height="300" />
            </a>
            </div>""".format(newFileName, post))

print("<ul id=\"media\" class=\"clearfix justified-gallery\">")

if get_arg(1) != '':
    if get_arg(2) != '':
        path = get_arg(2)
        postName = get_arg(1)

        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in sorted(files):
                    file_path = os.path.join(root, file)
                    if file.endswith("jpg"):
                        createMiniatures(postName,file_path)
        else:
            createMiniatures(path)


print("</ul>")
        

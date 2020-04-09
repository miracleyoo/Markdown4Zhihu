

# Usage: This program aims to transfer your markdown file into a way zhihu.com can recognize correctly.
#        It will mainly deal with your local images and the formulas inside.

import os, re
import argparse
import codecs
import subprocess
import chardet
import functools

from PIL import Image
from pathlib2 import Path
from shutil import copyfile

###############################################################################################################
## Please change the GITHUB_REPO_PREFIX value according to your own GitHub user name and relative directory. ##
###############################################################################################################
# GITHUB_REPO_PREFIX = Path("https://raw.githubusercontent.com/huangrt01/Markdown4Zhihu/master/Data/")
# Your image folder remote link
GITHUB_REPO_PREFIX = "https://raw.githubusercontent.com/huangrt01/Markdown4Zhihu/master/Data/"
COMPRESS_THRESHOLD = 5e5 # The threshold of compression

# The main function for this program
def process_for_zhihu():
    if args.compress:
        reduce_image_size()
    with open(str(args.input), 'rb') as f:
        s = f.read()
        chatest = chardet.detect(s)
    print(chatest)
    with open(str(args.input),"r",encoding=chatest["encoding"]) as f:
        lines = f.read()
        lines = image_ops(lines)
        lines = formula_ops(lines)
        lines = table_ops(lines)
        with open(args.input.parent/(args.input.stem+"_for_zhihu.md"), "w+", encoding=chatest["encoding"]) as fw:
            fw.write(lines)
        git_ops()

# Deal with the formula and change them into Zhihu original format
def formula_ops(_lines):
    _lines = re.sub('((.*?)\$\$)(\s*)?([\s\S]*?)(\$\$)\n', '\n<img src="https://www.zhihu.com/equation?tex=\\4" alt="\\4" class="ee_img tr_noresize" eeimg="1">\n', _lines)
    _lines = re.sub('(\$)(?!\$)(.*?)(\$)', ' <img src="https://www.zhihu.com/equation?tex=\\2" alt="\\2" class="ee_img tr_noresize" eeimg="1"> ', _lines)
    return _lines

# The support function for image_ops. It will take in a matched object and make sure they are competible
def rename_image_ref(m, original=True):
    global image_folder_path
    if not Path(image_folder_path.parent/m.group(2)).is_file():
        return m.group(0)
    if os.path.getsize(image_folder_path.parent/m.group(1+int(original)))>COMPRESS_THRESHOLD:
        if original:
            image_ref_name = Path(m.group(2)).stem+".jpg"
        else:
            image_ref_name = Path(m.group(1)).stem+".jpg"
    else:
        if original:
            image_ref_name = Path(m.group(2)).name
        else:
            image_ref_name = Path(m.group(1)).name
    if original:
        return "!["+m.group(1)+"]("+GITHUB_REPO_PREFIX+str(image_folder_path.name)+"/"+image_ref_name+")"
    else:
        return '<img src="'+GITHUB_REPO_PREFIX+str(image_folder_path.name)+"/" +image_ref_name +'"'

# Search for the image links which appear in the markdown file. It can handle two types: ![]() and <img src="LINK" alt="CAPTION" style="zoom:40%;" />.
# The second type is mainly for those images which have been zoomed.
def image_ops(_lines):
    # if args.compress:
    #     _lines = re.sub(r"\!\[(.*?)\]\((.*?)\)",lambda m: "!["+m.group(1)+"]("+GITHUB_REPO_PREFIX+str(image_folder_path.name)+"/"+Path(m.group(2)).stem+".jpg)", _lines)
    #     _lines = re.sub(r'<img src="(.*?)"',lambda m:'<img src="'+GITHUB_REPO_PREFIX+str(image_folder_path.name)+"/"+Path(m.group(1)).stem+'.jpg"', _lines)
    # else:
    _lines = re.sub(r"\!\[(.*?)\]\((.*?)\)",functools.partial(rename_image_ref, original=True), _lines)
    _lines = re.sub(r'<img src="(.*?)"',functools.partial(rename_image_ref, original=False), _lines)
    return _lines

# Deal with table. Just add a extra \n to each original table line
def table_ops(_lines):
    return re.sub("\|\n",r"|\n\n", _lines)

# Reduce image size and compress. It the image is bigger than threshold, then resize, compress, and change it to jpg.
def reduce_image_size():
    global image_folder_path
    image_folder_new_path = args.input.parent/(args.input.stem+"_for_zhihu")
    if not os.path.exists(str(image_folder_new_path)): 
        os.mkdir(str(image_folder_new_path))
    for image_path in [i for i in list(image_folder_path.iterdir()) if not i.name.startswith(".") and i.is_file()]:
        print(image_path)
        if os.path.getsize(image_path)>COMPRESS_THRESHOLD:
            img = Image.open(str(image_path))
            if(img.size[0]>img.size[1] and img.size[0]>1920):
                img=img.resize((1920,int(1920*img.size[1]/img.size[0])),Image.ANTIALIAS)
            elif(img.size[1]>img.size[0] and img.size[1]>1080):
                img=img.resize((int(1080*img.size[0]/img.size[1]),1080),Image.ANTIALIAS)
            img.convert('RGB').save(str(image_folder_new_path/(image_path.stem+".jpg")), optimize=True,quality=85)
        else:
            copyfile(image_path, str(image_folder_new_path/image_path.name))
    image_folder_path = image_folder_new_path

# Push your new change to github remote end
def git_ops():
    subprocess.run(["git","add","-A"])
    subprocess.run(["git","commit","-m", "update file "+args.input.stem])
    subprocess.run(["git","push", "-u", "origin", "master"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Please input the file path you want to transfer using --input=""')

    # RGB arguments
    parser.add_argument(
        '--compress', action='store_true', help='Compress the image which is too large')

    parser.add_argument(
        '--input',
        type=str,
        help='Path to the file you want to transfer.')

    args = parser.parse_args()
    if args.input is None:
        raise FileNotFoundError("Please input the file's path to start!")
    else:
        args.input = Path(args.input)
        image_folder_path = args.input.parent/(args.input.stem)
        process_for_zhihu()

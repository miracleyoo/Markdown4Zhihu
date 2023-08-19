

# Usage: This program aims to transfer your markdown file into a way zhihu.com can recognize correctly.
#        It will mainly deal with your local images and the formulas inside.

import os, re
import argparse
import codecs
import subprocess
import chardet
import functools
import os.path as op

from PIL import Image
from pathlib2 import Path
from shutil import copyfile

###############################################################################################################
## Please change the GITHUB_REPO_PREFIX value according to your own GitHub user name and relative directory. ##
###############################################################################################################
# GITHUB_REPO_PREFIX = Path("https://raw.githubusercontent.com/`YourUserName`/`YourRepoName`/master/Data/")
# Your image folder remote link
GITHUB_REPO_PREFIX = "https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/"
COMPRESS_THRESHOLD = 5e5 # The threshold of compression

# The main function for this program
def process_for_zhihu():

    if args.encoding is None:
        with open(str(args.input), 'rb') as f:
            s = f.read()
            chatest = chardet.detect(s)
            args.encoding = chatest['encoding']
        print(chatest)
    with open(str(args.input),"r",encoding=args.encoding) as f:
        lines = f.read()
        lines = image_ops(lines)
        # if args.compress and args.stem_folder:
        #     reduce_image_size()
        lines = formula_ops(lines)
        lines = table_ops(lines)
        with open(args.input.parent/(args.input.stem+"_for_zhihu.md"), "w+", encoding=args.encoding) as fw:
            fw.write(lines)
        cleanup_image_folder()
        git_ops()

# Deal with the formula and change them into Zhihu original format
def formula_ops(_lines):
    _lines = re.sub('((.*?)\$\$)(\s*)?([\s\S]*?)(\$\$)\n', '\n<img src="https://www.zhihu.com/equation?tex=\\4" alt="\\4" class="ee_img tr_noresize" eeimg="1">\n', _lines)
    _lines = re.sub('(\$)(?!\$)(.*?)(\$)', ' <img src="https://www.zhihu.com/equation?tex=\\2" alt="\\2" class="ee_img tr_noresize" eeimg="1"> ', _lines)
    return _lines

# The support function for image_ops. It will take in a matched object and make sure they are competible
def rename_image_ref(m, original=True):
    # global image_folder_path
    ori_path = m.group(2) if original else m.group(1)
    try:
        if op.exists(ori_path):
            full_img_path = ori_path
            # copy the image to image_folder_path
            # generate a unique name for the image, if there is a same name image, then add a number to the end of the name recursively until it is unique
            img_stem = Path(full_img_path).stem
            img_suffix = Path(full_img_path).suffix
            img_name = img_stem+img_suffix
            img_name_new = img_name
            if op.exists(op.join(args.image_folder_path, img_name_new)):
                i = 1
                while op.exists(op.join(args.image_folder_path, img_name_new)):
                    img_name_new = img_stem+"_"+str(i)+img_suffix
                    i+=1
            
            copyfile(full_img_path, op.join(args.image_folder_path, img_name_new))
            full_img_path = op.join(args.image_folder_path, img_name_new)

        else:
            full_img_path = op.join(args.file_parent, ori_path)
            img_stem = Path(full_img_path).stem
            if not op.exists(full_img_path):
                return m.group(0)
    except OSError:
        return m.group(0)

    if op.getsize(full_img_path)>COMPRESS_THRESHOLD and args.compress:
        full_img_path = reduce_single_image_size(full_img_path)
    
    image_ref_name = Path(full_img_path).name
    args.used_images.append(image_ref_name)

    print('full_img_path',full_img_path)
    print('image_ref_name',image_ref_name)
    
    if original:
        return "!["+m.group(1)+"]("+GITHUB_REPO_PREFIX+args.input.stem+"/"+image_ref_name+")"
    else:
        return '<img src="'+GITHUB_REPO_PREFIX+args.input.stem+"/" +image_ref_name +'"'

def cleanup_image_folder():
    actual_image_paths = [op.join(args.image_folder_path, i) for i in os.listdir(args.image_folder_path) if op.isfile(op.join(args.image_folder_path, i))]
    for image_path in actual_image_paths:
        if Path(image_path).name not in args.used_images:
            print("File "+str(image_path)+" is not used in the markdown file, so it will be deleted.")
            os.remove(str(image_path))

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


def reduce_single_image_size(image_path):
    # The output file path suffix must be jpg
    output_path = Path(image_path).parent/(Path(image_path).stem+".jpg")
    if op.exists(image_path):
        img = Image.open(image_path)
        if(img.size[0]>img.size[1] and img.size[0]>1920):
            img=img.resize((1920,int(1920*img.size[1]/img.size[0])),Image.ANTIALIAS)
        elif(img.size[1]>img.size[0] and img.size[1]>1080):
            img=img.resize((int(1080*img.size[0]/img.size[1]),1080),Image.ANTIALIAS)
        img.convert('RGB').save(output_path, optimize=True,quality=85)
    return output_path

# Reduce image size and compress. It the image is bigger than threshold, then resize, compress, and change it to jpg.
def reduce_image_size():
    if op.exists(args.image_folder_path):
        image_folder_new_path = args.input.parent/(args.input.stem+"_for_zhihu")
        if not op.exists(str(image_folder_new_path)): 
            os.mkdir(str(image_folder_new_path))
        for image_path in [i for i in list(args.image_folder_path.iterdir()) if not i.name.startswith(".") and i.is_file()]:
            print(image_path)
            if op.getsize(image_path)>COMPRESS_THRESHOLD:
                img = Image.open(str(image_path))
                if(img.size[0]>img.size[1] and img.size[0]>1920):
                    img=img.resize((1920,int(1920*img.size[1]/img.size[0])),Image.ANTIALIAS)
                elif(img.size[1]>img.size[0] and img.size[1]>1080):
                    img=img.resize((int(1080*img.size[0]/img.size[1]),1080),Image.ANTIALIAS)
                img.convert('RGB').save(str(image_folder_new_path/(image_path.stem+".jpg")), optimize=True,quality=85)
            else:
                copyfile(image_path, str(image_folder_new_path/image_path.name))
    args.image_folder_path = image_folder_new_path

# Push your new change to github remote end
def git_ops():
    subprocess.run(["git","add","-A"])
    subprocess.run(["git","commit","-m", "update file "+args.input.stem])
    subprocess.run(["git","push", "-u", "origin", "master"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Please input the file path you want to transfer using --input=""')
    parser.add_argument('--compress', action='store_true', help='Compress the image which is too large')
    parser.add_argument('-i', '--input', type=str, help='Path to the file you want to transfer.')
    parser.add_argument('-e', '--encoding', type=str, help='Encoding of the input file')

    args = parser.parse_args()
    args.used_images = []
    if args.input is None:
        raise FileNotFoundError("Please input the file's path to start!")
    else:
        args.input = Path(args.input)
        args.file_parent = str(args.input.parent)
        args.image_folder_path = op.join(args.file_parent, args.input.stem)
        if not op.exists(args.image_folder_path):
            args.stem_folder=False
            os.makedirs(args.image_folder_path)
        else:
            args.stem_folder=True

        # if op.exists(op.join(args.image_folder_path, args.input.stem)):
        #     args.image_folder_path = op.join(args.image_folder_path, args.input.stem)
        #     args.stem_folder=True
        # else:
        #     args.stem_folder=False
                     
        print(args.image_folder_path)
        process_for_zhihu()



# Usage: This program aims to transfer your markdown file into a way zhihu.com can recognize correctly.
#        It will mainly deal with your local images and the formulas inside.

import os, re
from pathlib2 import Path
import argparse
import codecs
import subprocess
import chardet

###############################################################################################################
## Please change the GITHUB_REPO_PREFIX value according to your own GitHub user name and relative directory. ##
###############################################################################################################
# GITHUB_REPO_PREFIX = Path("https://raw.githubusercontent.com/`YourUserName`/`YourRepoName`/master/Data/")
GITHUB_REPO_PREFIX = "https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/"

def process_for_zhihu():
    with open(str(args.input), 'rb') as f:
        s = f.read()
        chatest = chardet.detect(s)
    with open(str(args.input),"r",encoding=chatest["encoding"]) as f:
        lines = f.read()
        lines = formula_ops(lines)
        lines = image_ops(lines)
        lines = table_ops(lines)
        with open(args.input.parent/(args.input.stem+"_for_zhihu.md"), "w+", encoding=chatest["encoding"]) as fw:
            fw.write(lines)
        git_ops()

def formula_ops(_lines):
    _lines = re.sub('((.*)?\$\$\n)(\s*)?(.+?)(\$\$\n)', '\n<img src="https://www.zhihu.com/equation?tex=\\3" alt="\\3" class="ee_img tr_noresize" eeimg="1">\n', _lines)
    _lines = re.sub('(\$)(?!\$)(.*?)(\$)', ' <img src="https://www.zhihu.com/equation?tex=\\2" alt="\\2" class="ee_img tr_noresize" eeimg="1"> ', _lines)
    return _lines

def image_ops(_lines):
    return re.sub(r"!\[(.*?)\]\((.*?)\)","![\\1]("+GITHUB_REPO_PREFIX+"\\2"+")", _lines)

def table_ops(_lines):
    return re.sub("\|\n",r"|\n\n", _lines)

def git_ops():
    subprocess.run(["git","add","-A"])
    subprocess.run(["git","commit","-m", "update file "+args.input.stem])
    subprocess.run(["git","push", "-u", "origin", "master"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Please input the file path you want to transfer using --input=""')

    # RGB arguments
    parser.add_argument(
        '--rgb', action='store_true', help='Evaluate RGB pretrained network')

    parser.add_argument(
        '--input',
        type=str,
        help='Path to the file you want to transfer.')

    args = parser.parse_args()
    if args.input is None:
        raise FileNotFoundError("Please input the file's path to start!")
    else:
        args.input = Path(args.input)
        process_for_zhihu()
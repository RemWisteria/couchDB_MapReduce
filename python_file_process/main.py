import os
from os import path
import requests
import re



# file_name = "CommandLog-20210413103047.log"
def scan_file(url):
    """
    打印指定目录的所有子文件和子目录的子文件
    :param url: 目录路径
    :return:
    """
    file = os.listdir(url)
    for f in file:
        real_path = path.join(url, f)
        if path.isfile(real_path):
            print(path.abspath(real_path))
        elif path.isdir(real_path):
            scan_file(real_path)
        else:
            print('else')


def file_content_split(url):
    """
    分离文件每一行内容
    :param url: 文件路径
    :return: 数组
    """
    print(path.split(url))
    with open(url) as file:
        container = file.readlines()
    return container


def write_content(destination, content_s):
    """
    向文件写入内容
    :param destination: 写入文件路径
    :param content_s: 写入内容
    :return:
    """
    with open(destination, 'w', encoding='UTF-8') as wstream:
        wstream.write(content_s)

base_path = path.abspath(r"D:\StudyMain\MapReduce_couchDB\XFlogback-220526\FireData")
# scan_file(base_path)
content = file_content_split(r"D:\StudyMain\MapReduce_couchDB\XFlogback-220526\FireData\20220525142152\(2)20173169.gdf")
write_content("content.txt", str(content).replace("'", '"'))

# pattern = r'\bId\b:[A-Za-z0-9]*'
# for i, line in enumerate(content):
#     res = re.findall(pattern, line)
#     if res:
#         print(line.replace('\n', ''))
#         print(i, res, "\n")
#         print(''.join(content))



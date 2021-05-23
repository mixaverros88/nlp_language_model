from os import listdir
from os.path import isfile, join, dirname, abspath
import urllib.request
import configparser

config = configparser.RawConfigParser()
config.read('ConfigFile.properties')

d = dirname(dirname(abspath(__file__)))


def get_reuters_files():
    mypath = d + '\\dataset\\'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    quote = ''
    for fileName in onlyfiles:
        f = open(mypath + fileName, "r")
        quote += f.read()
    return quote


def get_test_file(file_name):
    mypath = d + '\\tests\\files' + file_name + '.txt'
    f = open(mypath, "r")
    return f.read()


def read_norvig_dataset():
    corpus = ''
    for line in urllib.request.urlopen(config.get('URLSECTION', 'url.norvig')):
        corpus += line.decode('utf-8')
    return corpus

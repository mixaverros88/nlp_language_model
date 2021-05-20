from os import listdir
from os.path import isfile, join


def get_reuters_files():
    # TODO: replace path
    mypath = 'C:/Users/mverros/Desktop/archive/python_projects/npl/nlp_language_model/dataset/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    quote = ''
    for fileName in onlyfiles:
        f = open(mypath + fileName, "r")
        quote += f.read()
    return quote


def get_test_file(file_name):
    # TODO: replace path
    mypath = 'C:/Users/mverros/Desktop/archive/python_projects/npl/nlp_language_model/tests/files/' + file_name + '.txt'
    f = open(mypath, "r")
    return f.read()

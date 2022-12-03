import os
from pathlib import Path


def get_list_of_strings(input_path, input_filename):
    #Load file information
    inputPath = Path(input_path + input_filename)
    f = open(inputPath, "r")
    list_of_strings = f.readlines()
    f.close()
    return list_of_strings

def get_strings(dayno):
    cwd = Path(os.path.dirname(os.path.abspath(__file__))).parent
    return get_list_of_strings(cwd.__str__() + "/Inputs/", f'day{dayno}.txt')

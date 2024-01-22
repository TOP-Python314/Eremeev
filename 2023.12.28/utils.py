from pathlib import Path
from sys import path
from shutil import copy2

def load_file(file_path):
    copy2(file_path,Path(path[0]))
    return Path(path[0])


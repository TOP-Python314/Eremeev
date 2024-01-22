from pathlib import Path 
from sys import path

def ask_for_file():
    input_file = input()
    file_path = Path(input_file)
    while file_path.is_file() == False:
        print('! по указанному пути отсутствует необходимый файл !')
        input_file = input()
        file_path = Path(input_file)
    if file_path.is_file():
        from utils import load_file
        res = load_file(file_path)
        
        return Path(res)
        
# >>> config_module = ask_for_file()
# ! по указанному пути отсутствует необходимый файл !
# E:\Users\doter\Desktop\python_main\dz\Eremeev\2023.12.28\data
# ! по указанному пути отсутствует необходимый файл !
# E:\Users\doter\Desktop\python_main\dz\Eremeev\2023.12.28\data\conf.py
# >>>    
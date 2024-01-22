from pathlib import Path

def list_files(aputh: str)-> None | tuple:
    path = Path(aputh)
    path_list = list(path.iterdir())
    filename = []    
    for i in path_list:
        filename.append(str(i.name))
    filename = tuple(filename)
    return filename
    
    
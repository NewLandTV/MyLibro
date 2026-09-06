from os import path

def join(root: str, target: str) -> str:
    return path.join(root, target)

project_root = path.dirname(path.dirname(path.abspath(__file__)))
data_dir = join(project_root, "data")

def exists(pth: str):
    return path.exists(pth)
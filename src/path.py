from os import path

project_root = path.dirname(path.dirname(path.abspath(__file__)))
src_dir = path.dirname(path.abspath(__file__))
data_dir = path.join(project_root, "data")

def join(root: str, target: str) -> str:
    return path.join(root, target)

def exists(pth: str):
    return path.exists(pth)
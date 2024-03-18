import os
from pathlib import Path

from robot.api.logger import *


def check_is_file(path: str, extension: str = None) -> bool:
    _ret = False
    path_file = Path(path)
    if not path_file.exists():
        error(f"Le fichier {path} n'existe pas", html=True)
    elif not path_file.is_file():
        error(f"Le chemin {path} n'est pas un fichier", html=True)
    elif not path_file.suffix != f".{extension}" and extension is not None:
        error(f"Le fichier {path.split("/")[-1]} n'est pas à l'extension {extension}", html=True)
    else:
        info(f"Le fichier {path} existe {'et est à la bonne extension' if extension is not None else ''}")
        return True
    return _ret


def check_is_folder(path: str) -> bool:
    _ret = False
    path_file = Path(path)
    if not path_file.exists():
        error(f"Le fichier {path} n'existe pas", html=True)
    elif not path_file.is_dir():
        error(f"Le répertoire {path} n'est pas un répertoire", html=True)
    else:
        info(f"Le répertoire {path} existe", html=True)
        return True
    return _ret
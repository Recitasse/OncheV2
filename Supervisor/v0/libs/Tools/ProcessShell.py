import subprocess
import os
import pathlib

from dataclasses import dataclass
from typing import ClassVar

from v0.libs.Tools.FileMethods import check_is_file

from robot.api.logger import *


@dataclass
class ProcessShell:
    _cmd: ClassVar[str]
    _stdout: ClassVar[str]
    _stderr: ClassVar[str]
    _stdin: ClassVar[str]


    def execute_command(self, cmd: str) -> str:
        """Exécute une commande shell et renvoie l'output"""
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            if result.stderr != "":
                error(f"Erreur, impossible d'exécuter la commande : {cmd}\n{result.stderr}")
                return ""
            return result.stdout
        except subprocess.CalledProcessError as e:
            warn(f"La commande a echoué : {e}")
        except Exception as e:
            error(f"Erreur non capturée : {e}")
        return ""

    def execute_script(self, path: str):
        """Exécute un script dans le shell de linux"""
        if not check_is_file(path, extension=".sh"):
            error(f"Impossible d'exécuter {path}", html=True)
            return
        cmd = [f".{path}"]
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            info(f"Le code a été exécuté avec succès", html=True)
        else:
            error(f"Le script {path.split("/")[-1]} n'a pu être exécuté avec succès")
        
    def execute_script_in_background(self, cmd: str, **kwargs):
        """Exécute une commmande dans le shell en arrière plan"""
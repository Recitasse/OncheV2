import subprocess
import os
import pathlib

from dataclasses import dataclass
from typing import ClassVar

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

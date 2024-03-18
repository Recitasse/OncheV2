from robot.api.deco import keyword
from robot.api.logger import *
from v0.variables.variables import ERROR, SUCCESS
from v0.libs.Tools.ProcessShell import ProcessShell


@keyword
def execute_cmd_without_output(cmd: str):
    process = ProcessShell(cmd)
    return process.execute_command()


@keyword
def execute_cmd_with_output(cmd: str, result: str):
    process = ProcessShell(cmd)
    res = process.execute_command()
    if res == result:
        return True
    error(f"Le résultat de la commande {cmd} ne correspond pas à l'attendu : {res}")
    return False
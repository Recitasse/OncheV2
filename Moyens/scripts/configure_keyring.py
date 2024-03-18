import keyring
import getpass


def login_keyring():
    keyring.get_keyring()
    pass_ = input(f'Renseignez votre mot de passe utilisateur : \n')
    keyring.set_password("OncheV2", getpass.getuser(), pass_)

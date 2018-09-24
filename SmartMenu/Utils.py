import os


def clear_screen():
    """Clears the commandline window"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
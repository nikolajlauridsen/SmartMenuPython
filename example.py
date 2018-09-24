from SmartMenu.Menu import Menu
from SmartMenu.Bindings import Bindings

bindings = Bindings()


@bindings.bind('this')
def this():
    print('Ayyyy')
    input()


@bindings.bind('that')
def that():
    print('It')
    input()


@bindings.bind('something')
def something():
    print('Hecking')
    input()


@bindings.bind('another')
def another():
    print('WORKS!')
    input()


menu = Menu('menu.txt', bindings, out_of_bounds_msg='YOU WENT TOO FAR!! GO BACK!')
menu.run_menu()

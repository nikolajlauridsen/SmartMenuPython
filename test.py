from SmartMenu.Menu import Menu
from SmartMenu.Bindings import Bindings

bindings = Bindings()


@bindings.bind('this')
def this():
    print('Ayyyy')


@bindings.bind('that')
def that():
    print('It')


@bindings.bind('something')
def something():
    print('Hecking')


@bindings.bind('another')
def another():
    print('WORKS!')


menu = Menu('menu.txt', bindings, out_of_bounds_msg='YOU WENT TOO FAR!! GO BACK!')
menu.run_menu()

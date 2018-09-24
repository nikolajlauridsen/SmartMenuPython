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


menu = Menu('menu.txt', bindings)
menu.run_menu()

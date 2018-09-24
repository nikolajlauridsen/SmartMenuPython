
class Menu:
    def __init__(self, menu_path, bindings):
        self.title = None
        self.description = None
        self.commands = []
        self.load_menu(menu_path)
        self.bindings = bindings

    def load_menu(self, menu_path):
        with open(menu_path, mode='r') as file:
            lines = file.readlines()

            self.title = lines[0]
            self.description = lines[1]

            for i in range(2, len(lines)):
                split = lines[i].strip('\n').split(';')
                self.commands.append([split[0], split[1]])

    def run_menu(self):
        while True:
            print(self.title + '\n')
            for i, command in enumerate(self.commands):
                print('\t' + str(i+1) + ". " + command[0])

            u_input = input('\n' + self.description)
            if u_input.lower() == '0':
                break
            else:
                # Find bindings
                if u_input.isnumeric():
                    option = int(u_input)-1
                    if option < len(self.commands):
                        f_id = self.commands[int(u_input)-1][1]
                        self.bindings.call_binding(f_id)
                    else:
                        print('YOU WENT TOO FAR!! GO BACK!')
                else:
                    print('Invalid input, input a number')

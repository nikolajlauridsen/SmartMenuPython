from .Utils import clear_screen


class Menu:
    def __init__(self, menu_path, bindings, invalid_msg="Invalid input, input a number",
                 out_of_bounds_msg="Selection not in menu", clear=True):

        self.title = None
        self.description = None
        self.invalid_msg = invalid_msg
        self.out_of_bounds_msg = out_of_bounds_msg
        self.commands = []
        self.bindings = bindings
        self.clear = clear
        self.load_menu(menu_path)

    def load_menu(self, menu_path):
        with open(menu_path, mode='r') as file:
            lines = file.readlines()

            self.title = lines[0].strip('\n')
            self.description = lines[1].strip('\n')

            for i in range(2, len(lines)):
                split = lines[i].strip('\n').split(';')
                self.commands.append([split[0], split[1]])

    def run_menu(self):
        while True:
            # Clean screen after selected program has run (only if clear is true)
            if self.clear:
                clear_screen()

            # Print the menu
            print(self.title + '\n')
            for i, command in enumerate(self.commands):
                print('\t' + str(i+1) + ". " + command[0])

            # Take input
            u_input = input('\n' + self.description)
            # Stop menu if 0 is selected
            if u_input.lower() == '0':
                break
            else:
                # Test input
                if u_input.isnumeric():
                    # Remove one from input since lists are 0 indexed
                    option = int(u_input)-1
                    if option < len(self.commands):
                        # Remove menu from screen once in selected program (only if clear is true)
                        if self.clear:
                            clear_screen()
                        # 'find' the id of the selected menu function
                        f_id = self.commands[int(u_input)-1][1]
                        # And execute it
                        self.bindings.call_binding(f_id)
                    else:
                        print(self.out_of_bounds_msg)
                else:
                    print(self.invalid_msg)

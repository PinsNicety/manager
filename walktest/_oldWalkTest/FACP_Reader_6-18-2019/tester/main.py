import os, sys
from data_module import DataCenter


class App:

    def __init__(self):
        """Constructor for the Application menu system object."""
        self.main_menu()

    def main_menu(self):
        """Displays Main Menu and controls action of menu options."""
        self.clear_screen()
        print("""
        MAIN MENU
        ---------

        Choose Panel Type:
        [1] 2-3030
        [2] 640
        [Q] Quit
        """)

        self.user_input = input("Choose a Panel Type: ")
        if self.user_input == '1':
            dc = DataCenter('2-3030')
            dc.read_device_list()
            dc.print_devs()
            dc.read_test_device_list()
            dc.update_test_status()
            dc.print_test_results()
        elif self.user_input == '2':
            dc = DataCenter('640')
            dc.read_device_list()
            dc.print_devs()
            dc.read_test_device_list()
            dc.update_test_status()
            dc.print_test_results()
        elif self.user_input == "q" or self.user_input == "Q":
            self.app_quit()
        else: self.main_menu()

    def app_quit(self):
        """Exits application"""
        sys.exit(0)

    def clear_screen(self):
        """Clears terminal screen in windows for clean menu look."""
        os.system('cls')


app = App()

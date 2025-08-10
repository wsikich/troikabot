from menus import *
from operations import *


current_menu = home


def main():
    global current_menu
    while True:
        current_menu.print_text()
        current_menu.prompt_input()
        next_menu = current_menu.execute_input()
        current_menu = next_menu
        print("")
    

if __name__ == "__main__":
    main()
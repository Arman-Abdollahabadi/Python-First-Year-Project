"""this is my main project file"""

import classes


def main():
    """Restaurant ordering system: main menu"""

    
    restaurant = classes.Restaurant('My Place')
    play = True
    while play:
        classes.Display.display_menu()
        choice = classes.Display.get_user_choice()
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            print('Exit, have a nice shift')
            play = False
        else:
            pass
            

if __name__ == "__main__":
    main()
    
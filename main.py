"""Restaurant ordering system"""

import classes


def main():
    """Restaurant ordering system: main menu"""

    restaurant = classes.Restaurant('My Place')
    play = True
    while play:
        classes.Display.display_menu()
        choice = classes.Display.get_user_choice()
        if choice == '1':
            number_table = int(input('Add table number: '))
            guests_number = int(input('How many guests: '))
            new_table = classes.Table(number_table, guests_number)
            restaurant.add_table(new_table)
            print(f'{new_table} opened')
        elif choice == '2':
            if len(restaurant.tables) != 0:
                print('Open tables:')
                for tables in restaurant.tables:
                    print(f'{tables}')
            else:
                print('No open table')

        elif choice == '3':
            print('Exit, have a nice shift')
            play = False
        else:
            print('invalid option ! try again')
            
if __name__ == "__main__":
    main()
    
if choice == '1':
            number_table = int(input('Add table number: '))
            guests_number = int(input('How many guests: '))
            new_table = classes.Table(number_table, guests_number)
            restaurant.add_table(new_table)
            print(f'{new_table} opend')
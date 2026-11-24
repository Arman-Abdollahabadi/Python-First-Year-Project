import time

class Restaurant:
    """Hold the info of tables"""

    def __init__(self, name):
        self.name = name
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)
        

class Table:
    """One restaurant table with its number, guests and orders"""

    def __init__(self, table_number, guests):
        self.table_number = table_number
        self.guests = guests
        self.orders = []

    def __str__(self):
        return f'Table {self.table_number} with {self.guests} guests'
    
class Display:
    """All function regarding to display text for user"""

    @staticmethod
    def display_menu():
        time.sleep(5)
        print("\n*** My Place  ***")
        print("1. Open a table\n\
2. Show open table\n\
3. Exit\n")

    def get_user_choice():
        choice = input("Please choose 1, 2 or 3\n")
        return choice


# class Ordering:
#     """Here it keeps the data of ordering"""

#     def __init__(self):
#         self.orders = []

#     def add_order(self, order):
#         """Add orders to specific table"""
#         for table in self.tables:
#             self.table_number = order
#         return order



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
        self.how_many_person = guests
        self.orders = []

class Display:
    """All function regarding to display text for user"""

    @staticmethod
    def display_menu():
        time.sleep(1)
        print("\n*** SHAPINATOR MENU ***")
        print("1. Open a table\n\
2. Show open table\n\
3. Exit\n")

    def get_user_choice():
        choice = input("Please choose 1, 2 or 3\n")
        return choice


r = Restaurant('My Place')
t1 = Table(1, 4)
t2 = Table(2, 2)

r.add_table(t1)
r.add_table(t2)

print(len(r.tables))

# class Ordering:
#     """Here it keeps the data of ordering"""

#     def __init__(self):
#         self.orders = []

#     def add_order(self, order):
#         """Add orders to specific table"""
#         for table in self.tables:
#             self.table_number = order
#         return order



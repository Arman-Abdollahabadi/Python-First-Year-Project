class Restaurant:
    """Hold the info of tables"""

    def __init__(self, name):
        self.name = name
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)
        

class Table:
    """List of open tables, with the table number and
    how many persons seated"""


    def __init__(self, table_number, how_many_person):
        self.table_number = table_number
        self.how_many_person = how_many_person
        self.orders = []

    def add_table(self, table):
        self.tables.append(table)

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



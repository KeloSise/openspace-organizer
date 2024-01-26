from src.table import Table
import random

# represents an open space with multiple tables
# to initialise, a number of tables must be specified; organizes a list of names randomly to these tables, and displays the seating arrangement.
class OpenSpace:
    def __init__(self, number_of_tables):
        self.number_of_tables = number_of_tables
        self.tables = [] 
        for table in range(number_of_tables):
            self.tables.append(Table())

    # randomly assign people to the Seat objects in the different Table objects
    def organize(self, names):
        random.shuffle(names)
        for table in self.tables:
            while names and table.has_free_spot():
                name = names.pop()
                table.assign_seat(name)

    # display the different tables and their occupants in a nice and readable way
    def display(self):
        for i, table in enumerate(self.tables, start=1):
            print(f"\nTable {i}:")
            for j, seat in enumerate(table.seats, start=1):
                occupant = seat.occupant if not seat.free else "Empty"
                print(f"  Seat {j}: {occupant}")

    # store the repartition in an Excel file / re-cap file handling on Datacamp
    def store(self, filename):
        pass

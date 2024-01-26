# represents a seat with an occupant (a person's name) and a status indicating whether the seat is free or occupied.
class Seat:
    def __init__(self, occupant=None, free=True):
        self.free = True
        self.occupant = occupant

    # allows the program to assign someone a seat if it's free    
    def set_occupant(self, name):
        if self.free:
           self.occupant = name
           self.free = False
           return True
        else:
            return False

    # removes someone from a seat and returns the name of the person occupying the seat before
    def remove_occupant(self):
        seat_occupant = self.occupant
        self.occupant = None
        self.free = True
        return seat_occupant
    
# represents a table with 4 fixed available seats. Methods check if there's a free spot, assign a seat to someone, and calculate the remaining capacity.  
class Table:
    def __init__(self):
        self.capacity = 4
        self.seats = [] # List of Seat objects (size = capacity) / time-allowing, re-try having seats as a separate variable and not an instance of __init__
        for c in range(self.capacity):
            self.seats.append(Seat(''))

    # returns a boolean (True if a spot is available)
    def has_free_spot(self): 
        for seat in self.seats:
            if seat.free:
                return True
        return False
    
    # places someone at the table
    def assign_seat(self, name): 
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False

    # returns an integer count of the number of free seats
    def capacity_left(self):
        count = 0
        for seat in self.seats:
            if seat.free:
                    count += 1
        return count
   


# Imports the OpenSpace class from openspace.py; Table class from table.py; and Pandas library as pd.
from src.openspace import OpenSpace
from src.table import Table
import pandas as pd  

# function that takes an Excel file path + a column name, reads the Excel file, and returns a list of names from the specified column.
def list_colleagues_excel(file_path, column_name='Names'):
    
    try:
        df = pd.read_excel(file_path, sheet_name='Sheet1')
        colleagues_list = []
        for value in df[column_name]:
            colleagues_list.append(value)
        return colleagues_list

        # to check
        #df = pd.read_excel(file_path, sheet_name='Sheet1')
        #return df[column_name].tolist()  

    except Exception as e:
        print(f"Error loading colleagues: {e}")
        return []
    pass

# specifying the path to the Excel file. Use double slash \\
excel_file_path = "C:\\Users\\ssiny\\Desktop\\openspace-organizer\\colleagues.xlsx"
colleagues = list_colleagues_excel(excel_file_path) # calling the list_colleagues_excel function

# organising the colleagues, whoooooo !!
# takes the list of colleagues and the number of tables. 
# prints information about available seats, organizes colleagues to tables, and displays the seating arrangement.
def launch_organizer(colleagues, number_of_tables):
    print("\n ")
    print(f"There are {len(colleagues)} colleagues waiting to be assigned a seat!")
    #print(f"There are {number_of_tables} tables available")

    print("\n ")
    available_seats_beginning = sum(table.capacity_left() for table in OpenSpace(number_of_tables).tables)
    print(f"There are {available_seats_beginning} seats available.")

    open_space = OpenSpace(number_of_tables)

    print("\n ")
    print("Dear colleagues, your assigned seat is...")
    open_space.organize(colleagues)
    open_space.display()

    print("\n ")
    for i, table in enumerate(open_space.tables, start=1):
        print(f"Number of seats left at Table {i}: {table.capacity_left()}")

number_of_tables = 6 
launch_organizer(colleagues, number_of_tables)

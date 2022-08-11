# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PNguyen,8/10/22,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

import json
# -- Data -- #
# declare variables and constants
objFile = "C:\\Users\\am211f\\Documents\\Continue Education\\Python Programming\\Module05 - Lists and Dictionaries\\Assignment05\\ToDoList.txt"   # An object that represents a file
strata = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(objFile, "r")
for row in objFile:
  lstRow = row.split(" ")
  dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
  lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print("\n")  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
      for dicRow in lstTable:
        for myKey, myValue in dicRow.items():
          print(myKey, " = ", myValue )
      continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
      strTask = input("Enter a Task: ")
      strPriority = input("Enter a Priority: ")
      dicRow = {"Task":strTask,"Priority":strPriority}
      lstTable.append(dicRow)
      continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
      del lstTable[len(lstTable) - 1]
        # TODO: Add Code Here
      continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
      with open("C:\\Users\\am211f\\Documents\\Continue Education\\Python Programming\\Module05 - Lists and Dictionaries\\Assignment05\\ToDoToDoList.txt", 'w') as fout:
        json.dump(lstTable, fout)
      continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        exit()
        break  # and Exit the program

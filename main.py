# This file Handle user interaction and application flow.

# import Storage
import storage

# DB Object Creation and calling
database = storage.Database()
database.initialize()

# import Expense Manager
import expense_manager

manager = expense_manager.ExpenseManager(database)


# Print Title
title = """
           =====================================
                 Personal Expense Tracker        
           ====================================="""
print(title)

# Cli Interface Function
def menu() :
    # Print Menu Options
    print("Menu Options")
    print("------------------")
    print("1.Add Expense")
    print("2.View All Expense")
    print("3.Delete Expense")
    print("4.Exit")

menu()

while True :
    # Getting User Input
    user_input =int(input("Enter Your Option : "))

    # Controlflow
    match user_input :
        case 1 :
            print("Add Expense")

            amount = float(input("Please Enter Amount : "))
            category = input("Please Enter Category : ")
            description = input("Please Enter Description : ")
            date = input("Please Enter Date (YYYY-MM-DD) : ")

            manager.add_expense(amount,category,description,date)
        case 2 :
            print("View All Expense")
            pass
        case 3 :
            print("Delete Expense")
            pass
        case 4 :
            print("Exit")
            break
        case _ :
            print("Invalid Option")
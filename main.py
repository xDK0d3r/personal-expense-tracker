# This file Handle user interaction and application flow.

# import Storage and Expense Manager and datetime
import storage
import expense_manager
from datetime import datetime

# DB Object Creation and calling
database = storage.Database()
database.initialize()

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
    print("3.Edit Expense")
    print("4.Delete Expense")
    print("5.Exit")
    print("------------------")

menu()

while True :
    # Getting User Input
    try :
        user_input =int(input("Enter Your Option : "))
    except ValueError :
        print("Invalid Input ! Please Enter Valid Integers Only !")
        continue

    # Validation
    if user_input not in [1,2,3,4,5] :
        print("Invalid Option ! Please choose valid Option !")

    # Controlflow
    match user_input :
        case 1 :
            print("---------------------------------")
            print("Add Expense")
            print("---------------------------------")

            while True :    
                try :
                 amount = float(input("Please Enter Amount : "))
                except ValueError :
                 print("Invalid Input ! Please Try Again !")
                 continue

                # validation
                if amount <= 0 :
                 print("Amount must be greater than 0")
                 continue

                break            

            # Category choice
            categories = {
                1 : "Food",
                2 : "Travel",
                3 : "Bills",
                4 : "Shopping",
                5 : "Other"
                }

            while True :
              print("""
              -----------------
              Categories
              -----------------
               1.Food
               2.Travel
               3.Bills
               4.Shopping
               5.Other
              -----------------""")

              try :
                category_option = int(input("Please Select Category : "))
              except ValueError :
                print("Invalid Input ! Please Enter Valid Integers Only !")
                continue

              # Validation
              if category_option not in [1,2,3,4,5] :
                print("Invalid Option ! Please choose valid Option !")
                continue

              # Mapping
              category = categories[category_option]
              break

            # Description
            description_input = input("Please Enter Description (optional) : ")
            description = description_input.strip()

            # Date
            while True:
             try:
              date = input("Please Enter Date (YYYY-MM-DD) : ")
              datetime.strptime(date, "%Y-%m-%d")
             except ValueError:
              print("Invalid Date! Please use YYYY-MM-DD.")
              continue

             break

            manager.add_expense(amount,category,description,date)
        case 2 :
            print("-------------------------------")
            print("View All Expense")

            expenses = manager.view_expenses()

            # unpack for UI
            for id,amount,category,description,date in expenses :
                print("-------------------------------")
                print("id = ",id)
                print("Amount = ",amount)
                print("Category = ",category)
                print("Description = ",description)
                print("Date = ",date)
        case 3 :
            print("-------------------------------")
            print("Edit Expense")
            print("-------------------------------")
            expense_id = int(input("Which expense ID do you want to Edit ? : "))
            print("""
            ----------------- 
            Field
            ----------------- 
            1.Amount
            2.Category
            3.Description
            4.Date
            5.Cancel
            -----------------""")
            field = int(input("Select Field to Modify ? :"))
            match field :
                case 1 :
                    new_value = float(input("Please Enter New Amount : "))
                case 2 :
                    new_value = input("Please Enter New Category : ")
                case 3 :
                    new_value = input("Please Enter New Description : ")
                case 4 :
                    new_value = input("Please Enter New Date : ")
                case 5 :
                    print("Canceled !")
                    break
                case _ :
                    print("Invalid Field Selection")
            manager.edit_expense(expense_id,field,new_value)
        case 4 :
            print("-------------------------------")
            print("Delete Expense")
            print("-------------------------------")

            while True :
               
             try:
                expense_id = int(input("Which expense ID do you want to delete ? : "))
             except ValueError :
                print("Invalid Input ! Please Enter Valid Integers Only ! ")
                continue

             # Validation
             if expense_id <= 0:
                print("ID must be greater than 0 ")
                continue
             break

            result = manager.delete_expense(expense_id)

            if result == 1:
               print("Expense Deleted Successfully")
            else :
               print("ID not Found !")
        case 5 :
            print("Exit !")
            break
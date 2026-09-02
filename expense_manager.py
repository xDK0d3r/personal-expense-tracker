# This file Handles Expense Manger Operations.

# Expense Manager Class
class ExpenseManager :
    def __init__(self,database):
        self.db = database

     # Add Expense Method
    def add_expense(self,amount,category,description,date):
        # call insert method to pass data
        self.db.insert_expense(amount,category,description,date)

    # View All Expenses Method
    def view_expenses(self):
        # call get method to retrive data
        expenses = self.db.get_expenses()
        return expenses

    # Delete Expense Method
    def delete_expense(self,expense_id):
        # call delete Method to delete Data
        self.db.delete_expense(expense_id)
        
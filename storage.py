# This file handles Database Operations.

# import Sqlite
import sqlite3

class Database : 
    def __init__(self):
        self.connection = sqlite3.connect("expenses.db")
        self.cursor = self.connection.cursor()

    # DB intialize
    def initialize(self):
        self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS expenses (
      id INTEGER PRIMARY KEY,
      amount REAL,
      category TEXT,
      description TEXT,
      date TEXT
      )
     """)

        # Commit Changes
        self.connection.commit()


    # Function to Insert a Expense
    def insert_expense(self,amount,category,description,date):
        self.cursor.execute("""INSERT INTO expenses (amount,category,description,date)
        VALUES (?,?,?,?)""",(amount,category,description,date))

        self.connection.commit()

    # Function to Get all Expenses Details
    def get_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        expenses = self.cursor.fetchall()
        return expenses

    # Function to Delete a specific Expense
    def delete_expense(self,expense_id):
        self.cursor.execute("DELETE FROM expenses where id = ?",(expense_id,))

        self.connection.commit()

        return self.cursor.rowcount

    # Function to Modify Data
    def edit_expense(self,expense_id,field,new_value,):
       # edit based on field selection
       if field == 1 :
           self.cursor.execute("UPDATE expenses SET amount = ? WHERE id = ?",
                               (new_value,expense_id))
       elif field == 2 :
           self.cursor.execute("UPDATE expenses SET category = ? WHERE id = ?",
                                          (new_value,expense_id))
       elif field == 3 :
           self.cursor.execute("UPDATE expenses SET description = ? WHERE id = ?",
                                          (new_value,expense_id))
       else :
           self.cursor.execute("UPDATE expenses SET date = ? WHERE id = ?",
                                           (new_value,expense_id))

       self.connection.commit()

       return self.cursor.rowcount
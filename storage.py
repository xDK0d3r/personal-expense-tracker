# This file handles Database Operations.

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
    def insert_expense(self):
        pass

    # Function to Get all Expenses Details
    def get_expenses(self):
        pass

    # Function to Delete a specific Expense
    def delete_expense(self):
        pass


# Temporary file db object creation and calling
db = Database()
db.initialize()


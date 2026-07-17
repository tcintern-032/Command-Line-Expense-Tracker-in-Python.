## Expense Tracker (Python CLI)
A simple and user-friendly **Command-Line Expense Tracker** built with **Python**. This application allows users to manage their daily expenses efficiently by adding, viewing, deleting, searching, and summarizing expenses. All data is stored locally in a **JSON file**, ensuring that expenses remain available even after the program is closed.
## Table of Contents
* Overview
* Features
* Technologies Used
* Project Structure
* Usage
* Data Storage
* Error Handling
* Learning Outcomes
* Future Enhancements
* Author
## Overview
Managing personal expenses is an important habit. This project demonstrates how to build a simple expense management system using Python while practicing:
* File Handling
* JSON Data Storage
* Lists and Dictionaries
* Functions
* Exception Handling
* User Input Validation
* Command-Line Interface (CLI)
## Features
* Add a new expense
* View all saved expenses
* Delete an expense
* Calculate total expenses
* Store data permanently in a JSON file
* Handle invalid user input gracefully
* Search expenses by category
* Display expense summary by category
## Technologies Used
* Python 3.x
* JSON Module
* OS Module
## Project Structure
```text
ExpenseTracker/
│
├── expense_tracker.py      # Main application
├── config.py               # Configuration file
├── expenses.json           # Stores expense records
└── README.md               # Project documentation
```
---
## Usage
When you run the application, you will see the following menu:
```text
==============================
      Expense Tracker
==============================

1. Add Expense
2. View Expenses
3. Delete Expense
4. Calculate Total Expenses
5. Search by Category
6. Summary by Category
7. Exit
```
Choose an option by entering the corresponding number
## Example
Add Expense
```text
Enter expense name: Pizza
Enter amount: 500
Enter category: Food
Expense Added Successfully!
```
 View Expenses
```text
1. Pizza
   Amount   : $500
   Category : Food
2. Bus Fare
   Amount   : $100
   Category : Transport
```
  Total Expenses
```text
Total Expenses = $600
```
### Summary by Category

```text
Food        : $500
Transport   : $100
```
---
## Data Storage
All expense records are stored inside the **expenses.json** file.
Example:
```json
[
    {
        "name": "Pizza",
        "amount": 500,
        "category": "Food"
    },
    {
        "name": "Bus Fare",
        "amount": 100,
        "category": "Transport"
    }
]
```
Because the data is stored in JSON format, all expenses remain saved even after closing the application.
## Error Handling
The application includes basic error handling to improve user experience.
Examples:
* Prevents invalid menu choices
* Prevents non-numeric amounts
* Prevents invalid delete selections
* Prevents crashes if the JSON file is empty or missing
## Learning Outcomes
This project helped practice the following Python concepts:
* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* File Handling
* JSON Read/Write Operations
* Exception Handling
* Modular Programming
* Command-Line Application Development
## Future Enhancements
Some possible improvements include:
* Edit existing expenses
* Add date and time for each expense
* Monthly expense reports
* Charts and graphs
* Export to CSV or Excel
* User authentication
## Author
Muhammad Zeeshan Haider
Fresh Graduate In Information Technology From University Of Education Lahore

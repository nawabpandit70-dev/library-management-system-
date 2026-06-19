# Library Management System

## Project Purpose
This project is a simple Library Management System developed in Python.
It allows the user to add books, add members, borrow books, return books, and save data using CSV files.

## Features
- Add a new book
- Add a new member
- Borrow a book
- Return a book
- Display all books
- Display all members
- Display all loans
- Save data into CSV files
- Load saved data when the program starts
- Handle invalid menu input using exception handling

## Files in the Project
- `book.py` - contains the Book class
- `member.py` - contains the Member class
- `loan.py` - contains the Loan class
- `library.py` - contains the Library class and CSV handling
- `main.py` - runs the menu-driven program
- `books.csv` - stores saved book data
- `members.csv` - stores saved member data
- `loans.csv` - stores saved loan data

## How to Run from GitHub

### Run using GitHub Codespaces
1. Open this repository on GitHub.
2. Click the green **Code** button.
3. Open the **Codespaces** tab.
4. Click **Create codespace on main**.
5. Wait for the Codespace to open.
6. In the terminal, run:
   ```bash
   python main.py
   ```
   
## Example Usage
Use the following sample data:

- Book ID: `N1`
- Title: `It ends with us`
- Author: `Colleen Hoover`
- Member ID: `T1`
- Name: `Taranbir Sandhu`
- Email: `ts2003@email.com`
- Loan ID: `L1`

## How to Test
1. Run the program.
2. Choose option `1` and add a book.
3. Choose option `2` and add a member.
4. Choose option `3` and borrow the book.
5. Choose option `5` and check the book list.
6. Choose option `7` and check the loan list.
7. Choose option `4` and return the book.
8. Choose option `8` and save data.
9. Choose option `9` and exit.
10. Run the program again.
11. Choose options `5`, `6`, and `7` to confirm saved data loads correctly.

## Notes
- The program creates `books.csv`, `members.csv`, and `loans.csv` when data is saved.
- If the CSV files do not exist, the program starts with empty data.
- Invalid menu input is handled using `try/except`.

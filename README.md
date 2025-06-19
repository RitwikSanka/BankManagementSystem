# Bank Management System (Flask + SQLite)

This is a web-based Bank Management System built using Python (Flask) and SQLite. It allows users to perform essential banking operations such as creating accounts, viewing account details, depositing and withdrawing funds, and deleting accounts. The project was originally written in C++ as a console application and was adapted into a full-stack web application.

## Features

- Create new bank accounts with an account number, name, and balance
- View all existing accounts in a table
- Deposit money into an account
- Withdraw money with balance validation
- Delete accounts permanently
- Error handling for invalid inputs
- Responsive and clean user interface using Bootstrap

## Technologies Used

- Python 3
- Flask
- SQLite
- SQLAlchemy
- HTML5, Bootstrap 5

## Installation and Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/bankwebapp.git
cd bankwebapp
```

### 2. (Optional) Create and Activate a Virtual Environment

```
python -m venv venv
```

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

### 3. Install Dependencies

```
pip install flask sqlalchemy
```

### 4. Run the Flask Application

```
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

## Usage

- The homepage provides links to create new accounts or view existing ones.
- From the accounts list, you can deposit, withdraw, or delete any account.
- All data is stored in a local SQLite database file named `bank.db`, which is automatically created on first run.

## Project Structure

```
bankwebapp/
├── app.py
├── bank.db                 # created automatically
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── create.html
│   ├── list.html
│   ├── deposit.html
│   └── withdraw.html
├── static/                 # optional for custom styles or scripts
└── README.md
```

## Notes

- No external database setup is required.
- No user authentication is implemented.
- Intended for educational use or portfolio projects.

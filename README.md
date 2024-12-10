# Finance Tool Web Application

## Overview
The Finance Tool is a web application designed to help users manage their personal finances. The tool allows users to add, edit, and delete transactions, set monthly budgets, and view their transaction history. It provides a dashboard summarizing income, expenses, and remaining budget, offering users an insightful look into their financial status. The project leverages Django for the back-end, and it integrates JavaScript on the front-end for client-side validation. The application is mobile-responsive, ensuring usability across devices.

## Distinctiveness and Complexity

### Distinctiveness
This project is distinct from other CS50W projects in several key aspects:

- **Purpose and Functionality**: Unlike Project 2 (E-commerce) or Project 4 (Social Network), this project is focused on personal financial management, allowing users to track income, expenses, and set budgets. It does not involve user-to-user interactions or a marketplace.
- **Data Aggregation**: The dashboard aggregates and displays financial data, including income and expenses by category, and calculates the budget remaining, which adds significant functionality compared to standard CRUD operations in other projects.
- **Dynamic Filtering**: The transaction history includes dynamic filtering options, such as filtering by type, category, and date range, which goes beyond simple data display.

### Complexity
This project satisfies the complexity requirement through:

- **Multiple Models**: The project utilizes three distinct models: Category, Transaction, and Budget, each with different relationships and constraints.
- **User Authentication**: The project implements user authentication with custom views for login, logout, and registration.
- **CRUD Operations**: Full CRUD (Create, Read, Update, Delete) operations are implemented for transactions, complete with form validation and user-specific data handling.
- **JavaScript Validation**: Custom JavaScript is used for client-side form validation, enhancing user experience by preventing invalid submissions.
- **Data Visualization**: The dashboard aggregates and displays monthly income and expenses, and calculates remaining budget dynamically based on user data.

## Project Structure
The project structure is as follows:
```
finance_tool/
|-- budget/
|   |-- templates/
|   |   |-- budget/
|   |   |   |-- add_transaction.html
|   |   |   |-- dashboard.html
|   |   |   |-- delete_transaction.html
|   |   |   |-- edit_transaction.html
|   |   |   |-- layout.html
|   |   |   |-- login.html
|   |   |   |-- register.html
|   |   |   |-- set_budget.html
|   |   |   |-- transaction_history.html
|   |-- admin.py
|   |-- apps.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- finance_tool/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- db.sqlite3
|-- manage.py
```

## File Descriptions

### models.py
Defines three models:

- **Category**: Represents a category of transactions (e.g., "Groceries").
- **Transaction**: Represents an individual transaction with fields for amount, date, type (income/expense), category, and description.
- **Budget**: Represents a user’s budget for a specific month and year, ensuring each user has a unique budget for each period.

### views.py
Contains the logic for handling HTTP requests and rendering templates:

- **dashboard**: Displays the user's total income, expenses, and remaining budget.
- **add_transaction**: Handles adding new transactions.
- **transaction_history**: Lists all user transactions with filtering options.
- **edit_transaction**: Allows users to edit existing transactions.
- **delete_transaction**: Handles transaction deletion with a confirmation prompt.
- **set_budget**: Allows users to set their monthly budget.
- **login_view, logout_view, register**: Manage user authentication.

### forms.py
Defines forms used for user input:

- **TransactionForm**: Handles input for transactions.
- **BudgetForm**: Handles input for setting budgets.

### templates/budget/

- **layout.html**: Base template for consistent structure across all pages.
- **dashboard.html**: Displays financial summaries (income, expenses, budget remaining).
- **add_transaction.html**: Form for adding new transactions.
- **transaction_history.html**: Lists and filters transactions.
- **edit_transaction.html**: Form for editing transactions.
- **delete_transaction.html**: Confirmation page for deleting transactions.
- **login.html**: User login form.
- **register.html**: User registration form.
- **set_budget.html**: Form for setting monthly budgets.

### admin.py
Registers models in the Django admin interface for data management.

## How to Run the Application

### 1. Clone the Repository:
```bash
git clone https://github.com/USERNAME/finance_tool.git
cd finance_tool
```
### 2. Install Dependencies:
Ensure all required packages are installed by running:
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations:
```bash
python manage.py migrate
```

### 4. Create a Superuser:
```bash
python manage.py createsuperuser
```

### 5. Run the Development Server:
```bash
python manage.py runserver
```

### 6. Access the Application:
Visit http://127.0.0.1:8000 in your web browser.

##  Additional Information
- **Dependencies**: Ensure all Python packages in `requirements.txt` are installed.
- **Mobile-Responsiveness**: The application uses Bootstrap for responsive design.
- **Security Considerations**: User authentication is secured using Django's built-in tools.

## Distinctiveness and Complexity Recap

This project is unique due to its focus on financial management, extensive use of models and forms, user-specific data handling, CRUD operations, and JavaScript for form validation. It integrates complex data aggregation logic for financial summaries and provides users with an intuitive interface for budget tracking and transaction management.
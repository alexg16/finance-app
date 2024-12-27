# Personal Finance Tracker

A web application for managing personal finances, tracking income and expenses, and visualizing spending trends. Built as the capstone project for Harvard's **CS50W: Web Programming with Python and JavaScript**, this app demonstrates advanced use of Django, JavaScript, and responsive web design principles.

---

## Features
- **Dashboard**: View income, expenses, budgets, and dynamic charts for spending trends.
- **Transactions Management**: Add, edit, delete, and filter transactions by type, category, and date range.
- **Budget Tracking**: Set monthly budgets and monitor progress.
- **Dynamic Charts**: Visualize data using Chart.js for:
  - Expenses by category (pie chart).
  - Monthly spending trends (bar chart).
- **Mobile Responsiveness**: Fully responsive design using Bootstrap.

---

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Visualization**: Chart.js
- **Database**: SQLite (default Django DB)

---

## Setup and Installation

### Prerequisites
- Python 3.x installed on your system.
- A virtual environment tool (e.g., `venv`).

### Steps to Run the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/andrewkdev/finance-app.git
   cd repository-name
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Open your browser and visit: http://127.0.0.1:8000/

---

## Project Structure 
Here’s an overview of the main files and directories:
   ```bash
       personal-finance-tracker/
    ├── budget/
    │   ├── migrations/           # Database migrations
    │   ├── static/               # Static assets (CSS, JS, images)
    │   ├── templates/            # HTML templates
    │   ├── admin.py              # Admin panel configuration
    │   ├── apps.py               # Django app configuration
    │   ├── forms.py              # Forms for transaction and budget management
    │   ├── models.py             # Database models
    │   ├── views.py              # Application logic
    │   ├── urls.py               # URL routing
    ├── db.sqlite3                # SQLite database
    ├── manage.py                 # Django management tool
    ├── README.md                 # Project documentation
    ├── requirements.txt          # Python dependencies

   ```

---

## Features in Detail
1. **Dashboard**:
  - Displays income, expenses, remaining budget, and visualizations.
  - Dynamic charts update based on transactions for the current month.
2. **Transaction Management**:
  - Add transactions with fields like amount, category, type (income/expense), and description.
  - Edit or delete existing transactions.
  - Filter transactions by type, category, and date.
3. **Budget Tracking**:
  - Set monthly budgets and monitor remaining amounts.
4. **Data Visualization**:
  - Pie Chart: Breaks down expenses by category.
  - Bar Chart: Shows monthly spending trends.

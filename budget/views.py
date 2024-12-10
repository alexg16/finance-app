from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Sum
from .models import Transaction, Budget, Category
from .forms import TransactionForm, BudgetForm 
from datetime import date
import calendar


@login_required
def dashboard(request):
    user = request.user
    today = date.today()

    # Retrieve current month's budget
    budget = Budget.objects.filter(user=user, month=today.month, year=today.year).first()

    # Calculate total income and expenses for the current month
    transactions = Transaction.objects.filter(user=user, date__month=today.month, date__year=today.year)
    income_total = transactions.filter(type="income").aggregate(total=Sum('amount'))['total'] or 0
    expense_total = transactions.filter(type="expense").aggregate(total=Sum('amount'))['total'] or 0

    # Spending by Category for the current month
    category_data = transactions.filter(type="expense").values('category__name').annotate(total=Sum('amount'))
    category_labels = [entry['category__name'] for entry in category_data]
    category_totals = [float(entry['total']) for entry in category_data]

    # Monthly Spending Trend for the current year
    monthly_data = Transaction.objects.filter(
        user=user, type="expense", date__year=today.year
    ).values('date__month').annotate(total=Sum('amount'))
    monthly_totals = [0] * 12
    for entry in monthly_data:
        monthly_totals[entry['date__month'] - 1] = float(entry['total'])

    context = {
        'income_total': float(income_total) if income_total else 0,
        'expense_total': float(expense_total) if expense_total else 0,
        'budget': float(budget.amount) if budget else 0,
        'budget_remaining': float(budget.amount - expense_total) if budget else 0,
        'category_labels': category_labels,
        'category_totals': category_totals,
        'monthly_totals': monthly_totals,
        'month_labels': [calendar.month_name[m] for m in range(1, 13)],
    }
    return render(request, 'budget/dashboard.html', context)

@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Transaction added successfully.")
            return redirect("dashboard")
        else:
            messages.error(request, "Failed to add transaction. Please check the form for errors.")
    else:
        form = TransactionForm()
    return render(request, "budget/add_transaction.html", {"form": form})

@login_required
def transaction_history(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user).order_by('-date')

    # Filters
    transaction_type = request.GET.get('type')
    category_id = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if transaction_type:
        transactions = transactions.filter(type=transaction_type)
    if category_id:
        transactions = transactions.filter(category_id=category_id)
    if start_date:
        transactions = transactions.filter(date__gte=start_date)
    if end_date:
        transactions = transactions.filter(date__lte=end_date)

    categories = Category.objects.all()

    context = {
        'transactions': transactions,
        'categories': categories,
        'transaction_type': transaction_type,
        'category_id': category_id,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'budget/transaction_history.html', context)

@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_history')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'budget/edit_transaction.html', {'form': form, 'transaction': transaction})

@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, "Transaction deleted successfully.")
        return redirect('transaction_history')

    return render(request, 'budget/delete_transaction.html', {'transaction': transaction})


@login_required
def set_budget(request):
    user = request.user
    today = date.today()

    # Check if a budget already exists for the current month and year
    budget, created = Budget.objects.get_or_create(
        user=user,
        month=today.month,
        year=today.year,
        defaults={'amount': 0}
    )

    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            messages.success(request, "Monthly budget set successfully.")
            return redirect('dashboard')
        else:
            messages.error(request, "Failed to set budget. Please check the form.")
    else:
        form = BudgetForm(instance=budget)

    return render(request, 'budget/set_budget.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(request, "budget/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "budget/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("dashboard"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        
        if password != confirmation:
            messages.error(request, "Passwords must match.")
            return render(request, "budget/register.html")

        try:
            user = User.objects.create_user(email, email, password)
            user.save()
            login(request, user)
            messages.success(request, "Account created successfully. Welcome!")
            return HttpResponseRedirect(reverse("dashboard"))
        except IntegrityError:
            messages.error(request, "Email address already taken.")
            return render(request, "budget/register.html")

    return render(request, "budget/register.html")

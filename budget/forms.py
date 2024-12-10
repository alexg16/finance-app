from django import forms
from .models import Transaction, Category
from .models import Budget
from datetime import date
from calendar import month_name

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'type', 'category', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'month', 'year']
        widgets = {
            'month': forms.Select(choices=[(i, month_name[i]) for i in range(1, 13)]),
            'year': forms.Select(choices=[(i, i) for i in range(date.today().year, date.today().year + 5)]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].label = "Budget Amount"
        self.fields['month'].label = "Month"
        self.fields['year'].label = "Year"
from django import forms
import datetime
from django.contrib.auth.models import User

class AddExpensesForm(forms.Form):
    date = forms.DateField(
        label='Expense Date',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'default':datetime.date.today,
                'class':"block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4"
                }))
    category = forms.ChoiceField(
        choices=[
            ('Grocery','Grocery'),
            ('Dine Out','Dine Out'),
            ('Taxi','Taxi')
            ])
    amount = forms.DecimalField(max_digits=6,decimal_places=2)

    
class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
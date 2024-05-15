from django.shortcuts import render, redirect, get_object_or_404
from .models import TrackerIncomeExpense
from .forms import IncomeExpenseForm, StatementDateForm, UserLoginForm, CreateUserForm
from datetime import datetime
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def table(request):
    selected_month = request.GET.get('month', None)
    # Retrieve all entries and order them by date
    entries = TrackerIncomeExpense.objects.filter(user=request.user).order_by('date')

    if selected_month:
        month_number = datetime.strptime(selected_month, "%B").month
        entries = entries.filter(date__month=month_number)
    
    # Combine income and expense entries and sort them by date
    all_entries = list(entries)
    all_entries.sort(key=lambda x: x.date)

    # Calculate total income and total expense
    total_income = sum(entry.amount for entry in all_entries if entry.entryType == 'income')
    total_expense = sum(entry.amount for entry in all_entries if entry.entryType == 'expense')

    context = {
        'all_entries': all_entries,
        'total_income': total_income,
        'total_expense': total_expense,
    }

    return render(request, 'table.html', context)

def add(request):
    if request.method == 'POST':
        form = IncomeExpenseForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('table')
    else:
        form = IncomeExpenseForm()
    return render(request, 'add.html', {'form': form})

def edit(request, pk):
    print('hello')
    entry = get_object_or_404(TrackerIncomeExpense, pk=pk)
    if request.method == 'POST':
        form = IncomeExpenseForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        form = IncomeExpenseForm(instance=entry)
    return render(request, 'edit.html', {'form': form})

def delete(request, pk):
    entry = get_object_or_404(TrackerIncomeExpense, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('table')
    return render(request, 'delete.html', {'entry': entry})

def edit_table(request):
    all_entries = TrackerIncomeExpense.objects.filter(user=request.user)  # Retrieve all entries for debugging purposes
    print(all_entries)  # Print all entries to console for debugging
    context = {'all_entries': all_entries}
    return render(request, 'table.html', context)

def download_statement(request):
    if request.method == 'POST':
        form = StatementDateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # Generate PDF statement using start_date and end_date
            # For simplicity, I'm using a placeholder PDF generation logic
            statement_data = TrackerIncomeExpense.objects.filter(user=request.user, date__range=[start_date, end_date])
            html = render_to_string('statement.html', {'start_date': start_date, 'end_date': end_date, 'statement_data': statement_data})
            pdf = pdfkit.from_string(html, False)
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="statement.pdf"'
            return response
    else:
        # Redirect to the statement form if the request method is not POST
        return redirect('statement_form')

def statement_form(request):
    form = StatementDateForm()
    return render(request, 'statement_form.html', {'form': form})

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
 
    return render(request, 'registration/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def index(request):
    return render(request, 'index.html')
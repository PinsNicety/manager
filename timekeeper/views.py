from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from datetime import datetime, date
from . import models

# Create your views here.
def home(request):
    """ Handles all the actions on the timekeeper main page. """

    content = {
        'left_header': 'home'
    }


    return render(request, 'timekeeper/home.html', content)

def entries(request):
    """ Shows all entries for current user in the current pay period. """

    content = {
        'left_header': 'entries'
    }

    if request.method == 'POST':
        time_in, time_out, total_time = set_times(request.POST['time_in'],
                                                request.POST['time_out'])


        entry = models.Entry.objects.create(site=request.POST['site'],
                                            time_in=time_in,
                                            time_out=time_out,
                                            comments=request.POST['comments'],
                                            total_time=total_time,
                                            user = request.user
        )
        content['entries'] = models.Entry.objects.filter(user=request.user).order_by('time_out')
        return render(request, 'timekeeper/entries.html', content)
    else:
        content['entries'] = models.Entry.objects.filter(user=request.user).order_by('time_out')
        return render(request, 'timekeeper/entries.html', content)

def expenses(request):
    """ Shows all expenses for current user in the current pay period. """

    content = {
        'left_header': 'expenses',
        'date': str(date.today())
    }

    if request.method == 'POST':

        new_date = set_date(request.POST['date'])
        expense = models.Expense.objects.create(site=request.POST['site'],
                                            miles=request.POST['miles'],
                                            date=new_date,
                                            user = request.user
        )
        content['expenses'] = models.Expense.objects.filter(user=request.user).order_by('date')
        return render(request, 'timekeeper/expenses.html', content)

    else:
        content['expenses'] = models.Expense.objects.filter(user=request.user).order_by('date')
        return render(request, 'timekeeper/expenses.html', content)



def set_times(time_in, time_out):
    """
    Takes in 2 date strings and returns them as datetime objects
    as well as the total time between the datetime objects.
    """

    time_in = datetime.strptime(time_in, "%Y-%m-%dT%H:%M")
    time_out = datetime.strptime(time_out, "%Y-%m-%dT%H:%M")

    diff = time_out - time_in
    total_time = diff.total_seconds() / 3600
    return time_in, time_out, total_time

def set_date(form_date):
    """ Takes in a date from the form and returns a DateTime object. """

    year, month, day = form_date.split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    new_date = date(year, month, day)
    return new_date

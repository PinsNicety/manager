from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from datetime import datetime
from . import models

# Create your views here.
def home(request):
    """ Handles all the actions on the timekeeper main page. """

    content = {
        'left_header': ''
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
        return render(request, 'timekeeper/home.html', content)
    else:
        content['entries'] = models.Entry.objects.filter(user=request.user).order_by('time_out')
        return render(request, 'timekeeper/home.html', content)


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

from django.http import HttpResponseRedirect
from django.shortcuts import render
from data_center.forms import TestModelForm
from data_center.tester.data_module import DataCenter

def index(request):

    if request.method == 'POST':
        test_form = TestModelForm(request.POST, request.FILES)
        if test_form.is_valid():
            new_form = test_form.save()
            dc = DataCenter(request.POST['panel_type'], new_form.device_list.path, new_form.alarm_history.path)
            dc.read_device_list()
            dc.print_devs()
            dc.read_test_device_list()
            dc.update_test_status()
            test_results = dc.print_test_results()

            return HttpResponseRedirect('test_complete')
    else:
        test_form = TestModelForm()

    return render(request, 'pages/index.html', {'test_form': test_form})

def test_complete(request):
    return render(request, 'pages/test_complete.html')

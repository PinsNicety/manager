from django.shortcuts import render
from . import forms, models
from .data_center.data_module import DataCenter
from tempfile import NamedTemporaryFile
from openpyxl import load_workbook
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = forms.TestForm(request.POST, request.FILES)
        if form.is_valid():
            walktest = models.WalkTest.objects.create(device_list=request.FILES['device_list'],
                                                        test_history=request.FILES['test_history'],
                                                        site=request.POST['site'],
                                                        panel=request.POST['panel']
            )
            dc = DataCenter(walktest.panel, walktest.device_list, walktest.test_history)
            dc.read_device_list()
            dc.read_test_device_list()
            dc.update_test_status()
            content = {
                'detectors': dc.devices['detectors'],
                'modules': dc.devices['modules'],
                'id': walktest.id
            }
            return render(request, 'walktest/results.html', content)
    else:
        form = forms.TestForm()
    return render(request, 'walktest/home.html', {'form': form})

def export(request, id):
    walktest = models.WalkTest.objects.get(pk=id)
    path = 'media/walktest/walktest.xlsx'

    dc = DataCenter(walktest.panel, walktest.device_list, walktest.test_history)
    dc.read_device_list()
    dc.print_devs()
    dc.read_test_device_list()
    dc.update_test_status()
    dc.print_test_results()

    wb = load_workbook(path)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=test_report.xlsx'
    wb.save(response)
    return response

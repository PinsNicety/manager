from django.shortcuts import render
from . import forms, models
from .data_center.data_module import DataCenter

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
                'modules': dc.devices['modules']
            }
            return render(request, 'walktest/results.html', content)
    else:
        form = forms.TestForm()
    return render(request, 'walktest/home.html', {'form': form})

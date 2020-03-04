from django.shortcuts import render
from . import forms, models

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
            return render(request, 'walktest/home.html', {'form': form})
    else:
        form = forms.TestForm()
    return render(request, 'walktest/home.html', {'form': form})

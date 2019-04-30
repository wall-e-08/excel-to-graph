from django.shortcuts import render, redirect
from .forms import ExcelFileForm


def home(request):
    if request.method == 'POST':
        form = ExcelFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:all_data')
        else:
            pass
    else:
        form = ExcelFileForm()
    ctx = {
        "form": form,
    }
    return render(request, 'home/index.html', ctx)


def all_data(request):
    return render(request, 'home/all_data.html')



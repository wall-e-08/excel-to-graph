from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import ExcelFileForm
from .models import ExcelFile, GraphData
from .utils import get_data_from_sheet


def home(request):
    if request.method == 'POST':
        form = ExcelFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            return redirect('home:select_data', f.id)
    else:
        form = ExcelFileForm()
    ctx = {
        "form": form,
    }
    return render(request, 'home/index.html', ctx)


def data_sheet(request, ds_id):
    data = {}
    try:
        ef = ExcelFile.objects.get(id=ds_id)
    except ExcelFile.DoesNotExist as er:
        print(er)
        ef = None
    if ef:
        data = get_data_from_sheet(ef.excel_file.path)
    ctx = {
        "excl": ef,
        "xl_data": data,
        "ds_id": ds_id,
    }
    return render(request, 'home/all_datasheet.html', ctx)


def select_data(request, ds_id):
    data = {}
    existed_gd = {}
    try:
        ef = ExcelFile.objects.get(id=ds_id)
    except ExcelFile.DoesNotExist as er:
        print(er)
        ef = None
    if ef:
        data = get_data_from_sheet(ef.excel_file.path)
        existed_gd = GraphData.objects.filter(xl_file=ef).order_by('id')
    ctx = {
        "excl": ef,
        "xl_data": data,
        "existed_gd": existed_gd,
        "ds_id": ds_id,
    }
    return render(request, 'home/select_data_for_graph.html', ctx)


def ajax_save_xy_data(request):
    err_msg = ''
    if request.GET:
        try:
            ds_id = request.GET.get('ds_id')
            data = request.GET.get('data')
            ef = ExcelFile.objects.get(id=ds_id)
            GraphData.objects.create(xl_file=ef, coordinates=data)
            return JsonResponse({
                "success": True,
            })
        except (IndexError, ExcelFile.DoesNotExist) as er:
            print(er)
            err_msg = er
        except IntegrityError as er:
            print(er)
            err_msg = "Data already saved! Same data cannot be saved more than once"
    return JsonResponse({
        "success": False,
        "err_msg": err_msg
    })












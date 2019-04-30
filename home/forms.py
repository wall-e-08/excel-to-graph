from django.forms import forms


class ExcelFileForm(forms.Form):
    excel_file = forms.FileField()


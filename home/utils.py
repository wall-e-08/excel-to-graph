import os
import string
import random
import datetime
import xlrd


def get_doc_path(instance, filename):
    file_extension = os.path.splitext(filename)[1]
    return str(
        "{}-{}-{}".format(
            'datasheet',
            datetime.datetime.today().strftime("%d.%m.%y"),
            ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        ) + file_extension
    )


def get_data_from_sheet(file_dir):
    wb = xlrd.open_workbook(file_dir)

    xl_data = []
    for s in wb.sheets():
        for row in range(0, s.nrows):
            col_names = s.row(0)
            col_value = []
            for col in range(0, s.ncols):
                # print("name: {}, col: {}".format(name, col))
                value = s.cell(row, col).value
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                col_value.append(value)
            if not all(v == '' for v in col_value):
                # print("row {}: {}".format(row, [v for v in col_value]))
                xl_data.append(col_value)
    return xl_data



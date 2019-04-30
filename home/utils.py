import os
import string
import random
import datetime


def get_doc_path(instance, filename):
    file_extension = os.path.splitext(filename)[1]
    return str(
        "{}-{}-{}".format(
            'datasheet',
            datetime.datetime.today().strftime("%d.%m.%y"),
            ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        ) + file_extension
    )


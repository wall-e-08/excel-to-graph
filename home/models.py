from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

from .utils import get_doc_path


class ExcelFile(models.Model):
    excel_file = models.FileField(
        upload_to=get_doc_path,
        validators=[FileExtensionValidator(allowed_extensions=settings.ACCEPTED_EXTENSIONS)]
    )


class GraphData(models.Model):
    xl_file = models.ForeignKey(
        'ExcelFile',
        on_delete=models.CASCADE,
    )
    coordinates = models.TextField()

    class Meta:
        unique_together = ('xl_file', 'coordinates')





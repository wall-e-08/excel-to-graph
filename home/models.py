from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

from .utils import get_doc_path


class ExcelFile(models.Model):
    excel_file = models.FileField(
        upload_to=get_doc_path,
        validators=[FileExtensionValidator(allowed_extensions=settings.ACCEPTED_EXTENSIONS)]
    )



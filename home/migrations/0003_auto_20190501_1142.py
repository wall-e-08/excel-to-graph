# Generated by Django 2.1.3 on 2019-05-01 11:42

import django.core.validators
from django.db import migrations, models
import home.utils


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190430_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='excelfile',
            name='excel_file',
            field=models.FileField(upload_to=home.utils.get_doc_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xlsx'])]),
        ),
    ]

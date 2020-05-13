from django.db import models
from utils.id_generator import id_gen


class UploadedFiles(models.Model):
    id = models.CharField(
        max_length=9, primary_key=True, default=id_gen, editable=False)
    file_name = models.CharField(max_length=400)
    uploaded_at = models.DateField(auto_created=True)


class TestReport(models.Model):
    id = models.CharField(
        max_length=9, primary_key=True, default=id_gen, editable=False)
    report_id = models.IntegerField()
    temperature = models.DecimalField(default=0, decimal_places=30, max_digits=100)
    duration = models.CharField(max_length=1000, default='')
    timestamp = models.CharField(max_length=60, default='')
    created_at = models.DateField(auto_now_add=True)


class Log(models.Model):
    id = models.CharField(
        max_length=9, primary_key=True, default=id_gen, editable=False)
    request = models.CharField(max_length=4000, default='')
    created_at = models.DateField(auto_now_add=True)


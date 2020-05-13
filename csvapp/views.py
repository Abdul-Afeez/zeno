import os
import sys

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from csvapp.models import TestReport, Log
from utils.csv_parser import ZenoCSVParser


def home(request):
    test_reports = TestReport.objects.all()
    logs = Log.objects.all()
    return render(request, 'index.html', {'test_reports': test_reports, 'logs': logs})


def delete(request):
    TestReport.objects.all().delete()
    Log.objects.all().delete()
    return HttpResponseRedirect("/")


def process(request):
    storage_path_dir = os.path.split(os.path.abspath(__file__))[0]
    if request.method == 'POST' and request.FILES and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        file_location = os.path.join(storage_path_dir, 'assets', myfile.name)
        filename = fs.save(file_location, myfile)
        zeno_csv_parser = ZenoCSVParser(filename)
        if not zeno_csv_parser.validate_extension(('csv',)):
            os.remove(filename)
            return render(request, 'index.html', {'error': 'Invalid file format, accepts only csv'})
        for index, row in enumerate(zeno_csv_parser.parse()):
            if index == 0:
                zeno_csv_parser.receive_sense_training()
                continue
            if len(row) < zeno_csv_parser.min_length:
                continue
            try:
                test_report = TestReport(report_id=row[0],
                                         temperature=row[2],
                                         timestamp=row[1],
                                         duration=row[3])
                test_report.save()
            finally:
                pass
        os.remove(filename)
    return HttpResponseRedirect("/")


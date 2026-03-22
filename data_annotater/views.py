from django.shortcuts import render, redirect
from .forms import UploadForm
from .forms import AnnotationForm
from .models import StoreRecord
from django.db.models import Q #Allows for 'OR' conditions in filter()
import csv
import io



# Create your views here.
def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            decoded_file = file.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(decoded_file))
            for row in reader:
                # Checks for Duplicate Store Records then processes if UNIQUE
                if not StoreRecord.objects.filter(sku=row['sku'], merchant=row['merchant'], country=row['productcountry'] ).exists():
                    StoreRecord.objects.create(
                        merchant=row['merchant'],
                        sku=row['sku'],
                        country=row['productcountry'],
                    )
            return redirect('dashboard')
    else:
        form = UploadForm()

    return render(request, 'data_annotater/upload.html', {'form': form})

def dashboard_view(request):
    isFiltered = request.GET.get('isFiltered', 'true')
    #BUTTON - WIPES ALL RECORDS FROM DB FOR TESTING
    if request.method == 'POST':
        StoreRecord.objects.all().delete()
        return redirect('dashboard')
    # Views to show all objects
    if isFiltered == 'false':
        records = StoreRecord.objects.all()
    # and filter by annotation status
    else:
        records = StoreRecord.objects.filter(Q(retailer='') | Q(segment=''))

    return render(request, 'data_annotater/dashboard.html', {'records': records, 'isFiltered': isFiltered})

def annotate_view(request, pk):
    record = StoreRecord.objects.get(pk=pk)
    # Handles form submission and saves annotation to DB
    if request.method == 'POST':
        form = AnnotationForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AnnotationForm(instance=record)

    return render(request, 'data_annotater/annotate.html', {'record': record, 'form': form})
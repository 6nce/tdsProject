from django import forms
from .models import StoreRecord

class UploadForm(forms.Form):
    file = forms.FileField()

class AnnotationForm(forms.ModelForm):
    class Meta:
        model = StoreRecord
        fields = [
            'merchant',
            'sku',
            'country',
            'retailer',
            'segment'
        ]
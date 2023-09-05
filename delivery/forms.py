from django import forms
from .models import Delivery

class DeliveryUploadForm(forms.ModelForm):
    class Meta: 
        model = Delivery
        fields = "__all__"


class Meta:
        verbose_name_plural="feedback"
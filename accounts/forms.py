from .models import Shop
from django import forms


class AddUploadForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['b_type', 'model', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super(AddUploadForm, self).__init__(*args, **kwargs)
        self.fields['b_type'].empty_label = "Select"


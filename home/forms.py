from django import forms

class CreateCollectionForm(forms.Form):
    name = forms.CharField(max_length=300, required=True)
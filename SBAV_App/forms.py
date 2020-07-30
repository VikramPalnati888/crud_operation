from SBAV_App.models import *
from django import forms 

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['Item_Name','Items_In_Stock','Items_Out_Stock','Item_Cost']
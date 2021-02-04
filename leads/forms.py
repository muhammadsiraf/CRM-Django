from django import forms
from .models import Agent, Item, Lead

class LeadForm(forms.Form):
    lead_first_name = forms.CharField(label="first name", max_length=20)
    lead_last_name  = forms.CharField(label="last name", max_length=20)
    lead_age        = forms.IntegerField(label="age", min_value=0)
    lead_agent      = forms.ModelChoiceField(queryset=Agent.objects.all())



class LeadFormModel(forms.ModelForm):

    class Meta:
        model = Lead
        fields = '__all__'


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

class ItemInstanceForm(forms.Form):
    instance_item = forms.ModelChoiceField(label="Item Name", queryset=Item.objects.all())
    instance_lead = forms.ModelChoiceField(label="Lead Name", queryset=Lead.objects.all())
    quantity = forms.IntegerField(label="Quantity", min_value=1)
from django import forms

from .models import DocFile, TableAndUrlColumns

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    
class TableAndUrlColumnsForm(forms.ModelForm):
    class Meta:
        model = TableAndUrlColumns
        fields = ('organization', 'material_assigning', 'account_purpose', 'contract_number', 'contract_amount', 'paid1', 'account_number', 'account_date', 'accounts_amount', 'for_payment', 'payment_balance', 'paid2', 'remainder', 'note', 'docfile')
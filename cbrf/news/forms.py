from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'patronimic_name', 'contract_number', 'contract_date', 'message', 'organization', 'send_to_email']

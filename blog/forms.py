from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'mobile_number', 'message']  # List t
# from account.models import User

# from django import forms


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     email= forms.EmailField()
#     mobile_number = forms.CharField(required=False)
    
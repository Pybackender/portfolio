from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):

    # class ContactForm(forms.Form):
    #     name = forms.CharField(max_length=100)
    #     message = forms.CharField(widget=forms.Textarea)
    #     email= forms.EmailField()
    mobile_number = forms.TextInput(attrs={"size": "40", "required": False})

    class Meta:
        model = Contact
        fields = ['name', 'email', 'mobile_number', 'message']  # List t


    def clean_name(self):
        data = self.cleaned_data.get('name')
        if len(data) < 1:
            raise forms.ValidationError("طول متن نباید کمتر از ۵ حرف باشد")
        return data

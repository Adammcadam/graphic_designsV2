from django import forms

from .models import CustomProduct

class CustomQuoteForm(forms.ModelForm):
    class Meta:
        model = CustomProduct
        fields = ('length', 'width', 'height', 'description', 'image', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'length': 'Length',
            'width': 'width',
            'height': 'height',
            'description': 'Give us a little information about your project',
            'email' : 'Email',
            'phone_number' : 'Phone Number'
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'custom-input'

        for field in self.fields:
            if field != 'image':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder


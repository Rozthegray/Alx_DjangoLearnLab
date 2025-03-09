from django import forms

class ExampleForm(forms.Form):
    # A simple form with a few example fields
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    # Optional: Custom validation methods for fields
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@example.com" in email:
            raise forms.ValidationError("Example.com emails are not allowed.")
        return email


from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'gender', 'profile_pic',
            'university_name', 'university_email', 'department', 'branch',
            'year', 'bio', 'current_password'
        ]
        labels = {
            'current_password' : 'Password'
        }
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'year': forms.Select(attrs={'class': 'form-select'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'current_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.Select, forms.Textarea, forms.PasswordInput)):
                field.widget.attrs['class'] = 'form-control'

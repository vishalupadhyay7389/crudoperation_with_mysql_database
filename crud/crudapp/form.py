from django import forms

from crudapp.models import User

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'uemail':forms.TextInput(attrs={'class':'form-control'}),
            'upassword':forms.TextInput(attrs={'class':'form-control'}),
        }
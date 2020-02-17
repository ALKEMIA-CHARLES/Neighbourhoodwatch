from django import forms
from neighbourhoodwatch.models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
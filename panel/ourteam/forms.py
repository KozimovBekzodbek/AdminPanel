from django import forms
from restoran import  models

class OurTeamForm(forms.ModelForm):
    class Meta:
        model = models.Ourteam
        fields = "__all__"


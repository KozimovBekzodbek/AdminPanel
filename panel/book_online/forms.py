from django import forms
from restoran.models import Book_Online


class BookOnlineForm(forms.ModelForm):
    class Meta:
        model = Book_Online
        fields = "__all__"

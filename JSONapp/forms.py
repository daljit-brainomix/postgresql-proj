from django import forms
from django_json_widget.widgets import JSONEditorWidget

from .models import Dog


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog

        fields = (
            "name",
            "data",
        )

        widgets = {"data": JSONEditorWidget}

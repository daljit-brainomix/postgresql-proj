from django.contrib import admin
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget
from .models import Dog

# Register your models here.


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.JSONField: {"widget": JSONEditorWidget},
    }

# from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField
from django.utils.translation import gettext as _
from django.db import models
from django.urls import reverse

# Create your models here.
class Dog(models.Model):
    name = models.CharField(_("name"), max_length=50)
    data = JSONField()

    def get_absolute_url(self):
        return reverse("dog-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

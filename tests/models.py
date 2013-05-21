from django_localflavor_us.models import USStateField, USPostalCodeField
from django.db import models


class USPlace(models.Model):
    state = USStateField(blank=True)
    state_req = USStateField()
    state_default = USStateField(default="CA", blank=True)
    postal_code = USPostalCodeField(blank=True)
    name = models.CharField(max_length=20)

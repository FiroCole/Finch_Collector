from django.db import models

# Create your models here.
class Finch(models.Model):
    FINCH_SUBFAMILY_CHOICES = [
        ("Fringillinae", "Fringillinae"),
        ("Carduelinae", "Carduelinae"),
        ("Euphoniinae", "Euphoniinae"),
        ("Unknown", "Unknown"),
    ]
    name = models.CharField(max_length=100)
    subfamily = models.CharField(max_length=100, choices=FINCH_SUBFAMILY_CHOICES, default="Unknown")
    description = models.TextField(max_length=250)

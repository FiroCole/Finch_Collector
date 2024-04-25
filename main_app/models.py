from django.db import models

# Create your models here.
class Finch(models.Model):
    FINCH_SUBFAMILY_CHOICES = [
        ("Fringillinae", "Fringillinae"),
        ("Carduelinae", "Carduelinae"),
        ("Euphoniinae", "Euphoniinae"),
        ("Unknown", "Unknown"),
    ]
    FINCH_HABITAT_CHOICES = [
        ("Woodlands", "Woodlands"),
        ("Mountains", "Mountains"),
        ("Deserts", "Deserts"),
        ("Unknown", "Unknown"),
    ]
    name = models.CharField(max_length=100)
    subfamily = models.CharField(max_length=100, choices=FINCH_SUBFAMILY_CHOICES, default="Unknown")
    description = models.TextField(max_length=2500)
    habitat = models.CharField(max_length=100, choices=FINCH_HABITAT_CHOICES, default="Woodlands")
    
    def __str__(self):
        return self.name

from django.db import models
from django.urls import reverse

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
    subfamily = models.CharField(max_length=100)
    description = models.TextField(max_length=2500)
    habitat = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'finch_id': self.id    })

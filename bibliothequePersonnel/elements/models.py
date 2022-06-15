from pickle import TRUE
from django.db import models

class Element(models.Model):
    titre = models.CharField(max_length=150)
    remarque = models.TextField(blank=True, null=True)
    note = models.IntegerField(blank=True, null=True)
    TYPE_ELEMENT = (
        ('D', 'Disney'),
        ('F', 'Film'),
        ('S', 'Série')
    )
    image = models.ImageField(upload_to='img/',blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    type_element = models.CharField(max_length=1,choices=TYPE_ELEMENT)
    favori = models.BooleanField(default=False)
    decouvrir = models.BooleanField(verbose_name='Découvrir', default=False)
    revoir = models.BooleanField(default=False)
    acheter = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.titre
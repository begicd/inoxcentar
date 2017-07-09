from __future__ import unicode_literals

from django.db import models



#Create your models here.
materijal_dropdown=[
   ('prohrom-inox','prohrom-inox'),
   ('crni čelik-kovano gvožđe','crni čelik-kovano gvožđe'),
]


kategorija_dropdown=[
    ('kapije','kapije'),
    ('ograde','ograde'),
    ('gelenderi','gelenderi'),
    ('ogradice za terase','ogradice za terase'),
    ('galanterija','galanterija'),
    ]

def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)

class Proizvod(models.Model):
    kategorija=models.CharField(
        ('kategorija'),max_length=60, choices=kategorija_dropdown,default='kapije'
    )
    materijal=models.CharField(
        ('materijal'),max_length=60, choices=materijal_dropdown,default='prohrom-inox'
    )
    image=models.ImageField(
    upload_to=upload_location,
    null=True,
    blank=True, 
    height_field='height_field',
    width_field='width_field'
    )
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)



    #def __str__(self):
     #  return self.kategorija-self.materijal

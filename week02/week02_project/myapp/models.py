from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(blank=False,null=False)
    Age=models.CharField(max_length=2)
    gender=models.CharField(
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ),
        max_length=6,
        )
    faculty=models.CharField(max_length=100)
    province=models.CharField(max_length=100)
    typeofphone=models.CharField(
        choices=(
            ('OSI','IOS'),
            ('Android', 'Android'),
            ),
        max_length=7,
        )
    def __unicode__(self):
        return u"%s"%(self.name)

class Image(models.Model):
    image=models.ImageField(upload_to='images')
    description=models.CharField(max_length=100,blank=True,null=True)
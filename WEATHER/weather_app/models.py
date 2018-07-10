from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ='cities'


class Place(models.Model):
    place= models.CharField(max_length=25)

    def __str__(self):
        return self.place



class Data(models.Model):
    city=models.CharField(max_length=25)
    temp= models.IntegerField(blank=True,null=True)
    date=models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.city




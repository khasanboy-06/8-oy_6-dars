from django.db import models
from django.contrib.auth.models import User


class Hudud(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Qurilish_tashkiloti(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Qurilish_binosi(models.Model):
    qurilish_tashkiloti = models.ForeignKey(Qurilish_tashkiloti, on_delete=models.CASCADE)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    maydoni = models.IntegerField()
    qavat = models.IntegerField()
    parkovka = models.BooleanField()
    bolalar_maydonchasi = models.BooleanField()
    lift = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
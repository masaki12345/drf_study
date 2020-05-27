from django.db import models

# Create your models here.

class Profession(models.Model):
    profession_name = models.CharField(("職業"), max_length=50)
    income = models.IntegerField(("年収"))
    weekly_holiday = models.CharField(("週休"), max_length=50)

    def __str__(self):
        return self.profession_name


class Person(models.Model):
    first_name = models.CharField(("苗字"), max_length=50)
    last_name =models.CharField(("名前"), max_length=50)
    age = models.IntegerField(("年齢"))
    location = models.CharField(("所在地"), max_length=50)
    Profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


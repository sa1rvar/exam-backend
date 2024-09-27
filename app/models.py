from django.db import models

from django.db import models

class Food(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100)
    info = models.TextField(blank=True)
    manufacture = models.TextField(blank=True)
    cat = models.ForeignKey("Category", models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField


    def __str__(self):
        return self.name





from django.db import models

# Create your models here.
class brain(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class beginner(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class brute(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class greed(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class sub(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class implement(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class sort(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class binary(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class pointer(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class hash(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class pair(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class dpstand(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class dp(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class tree(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class graph(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class dsu(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class segtree(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    link = models.URLField()        
    def __str__(self) :
        return self.name
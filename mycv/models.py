from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Exprience(models.Model):
    company = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    startDate = models.CharField(max_length=200,default='Rabat')
    endDate = models.CharField(max_length=200)
    profil = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='Expience/')
    def __str__(self):
        return self.company
class Skill(models.Model):
    name = models.CharField(max_length=200)
    level=models.IntegerField( default=1, validators=[MaxValueValidator(5),MinValueValidator(1)  ])
    icon = models.CharField(max_length=200)
    def __str__(self):
        return self.name
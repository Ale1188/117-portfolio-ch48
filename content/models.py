from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='static/img')
    repository = models.URLField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.name} - ({self.year})"
    
class Experience(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    start_month = models.IntegerField()
    start_year = models.IntegerField()

    end_month = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)

    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.name}"
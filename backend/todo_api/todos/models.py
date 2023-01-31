from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        "Una cadena que representa el modelo"
        return self.title

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    def __str__(self):
        "Una cadena que representa el modelo"
        return self.title

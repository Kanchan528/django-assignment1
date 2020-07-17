from django.db import models

# Create your models here.

class AuthorInfo(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(AuthorInfo, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    image = models.ImageField(null=True)


    def __str__(self):
        return self.title




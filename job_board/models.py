from django.db import models

# Create your models here.
class job_posting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.title


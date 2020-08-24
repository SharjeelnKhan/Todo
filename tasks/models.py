from django.db import models

# Create your models here.


class Task(models.Model):
    task = models.CharField(max_length=200, default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task

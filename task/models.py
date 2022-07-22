from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    execution_period = models.DateTimeField()
    is_executed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

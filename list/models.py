from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, auto_now=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def mark_as_done(self):
        self.is_completed = True
        self.save()
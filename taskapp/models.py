from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def create_task(self):
        self.save()

    def save_task(self):
        self.save()

    def delete_task(self):
        self.delete()

    def update_task(self):
        self.save()

        
    def __str__(self):
        return self.title
    
    @classmethod
    def get_task(cls,searchTerm):
        title = cls.objects.filter(title__icontains=searchTerm)
        return title

    
    
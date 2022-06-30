from django.db import models
from users.models import Account
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    
    def get_json(self):
        return{
            'id': self.id,
            'task':self.task,
        }

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    balance = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def update_balance(self, amount):
        self.balance += amount
        self.save()
#User > Profile
#Profile > User
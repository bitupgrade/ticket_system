from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Fields in ticket forum
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # FIX: Users tickets do not get deleted when 
    
    TICKET_PRIORITY = [
        ('4 - Low', '4 - Low'),
        ('3 - Averege', '3 - Averege'),
        ('2 - High', '2 - High'),
        ('1 - Critical', '1 - Critical'),
    ]

    priority = models.CharField(max_length=12, choices=TICKET_PRIORITY, default='4 - Low')

    TICKET_STATUS = [
        ('Work in progress', 'Work in progress'),
        ('Pending customer', 'Pending customer'),
        ('Pending vendor', 'Pending vendor'),
        ('Closed', 'Closed'),
    ]

    status = models.CharField(max_length=50, choices=TICKET_STATUS, default='In Progress')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) # Returns user to post-detail after creating a post

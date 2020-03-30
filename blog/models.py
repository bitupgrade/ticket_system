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
        ('Priority 4', 'Priority 4'),
        ('Priority 3', 'Priority 3'),
        ('Priority 2', 'Priority 2'),
        ('Priority 1', 'Priority 1'),
    ]

    priority = models.CharField(max_length=10, choices=TICKET_PRIORITY, default='Priority 4')

    TICKET_STATUS = [
        ('In Progress', 'In Progress'),
        ('Waiting internal', 'Waiting internal'),
        ('Waiting on vendor', 'Waiting on vendor'),
        ('Closed', 'Closed'),
    ]

    status = models.CharField(max_length=50, choices=TICKET_STATUS, default='In Progress')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) # Returns user to post-detail after creating a post

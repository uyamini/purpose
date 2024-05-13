from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_score = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    posts = models.ManyToManyField('Post', related_name='volunteers')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_app_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_app_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Post(models.Model):
    STATUS_CHOICES = [
        ('need_help', 'Need Help'),
        ('in_progress', 'In Progress'),
        ('helped', 'Helped'),
    ]
    
    location_state = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_address = models.CharField(max_length=255)
    details = models.TextField()
    date_time_spotted = models.DateTimeField()
    posting_date_time = models.DateTimeField(auto_now_add=True)
    list_of_needs = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='need_help')
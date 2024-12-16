from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username1 = models.CharField(max_length=100)
    Ocuupation = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    Address = models.TextField()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
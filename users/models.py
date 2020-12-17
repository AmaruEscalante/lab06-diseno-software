from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Profile Model for Student and Teacher

    Codigo, Username, Nombres, Password, Tipo(Estudiante, Profesor)
    El modelo User contiene Username, FirstName, LastName, Password
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, blank=False) #

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

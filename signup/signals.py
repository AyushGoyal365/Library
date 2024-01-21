from .models import Profile , Book
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, profile_created = Profile.objects.get_or_create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Book)


def create_book(sender, instance, created, **kwargs):
    if created :
        pass

@receiver(post_save, sender=Book)
def save_book(sender, instance, **kwargs):
    if sender == Book:
        return
    
    instance.save()
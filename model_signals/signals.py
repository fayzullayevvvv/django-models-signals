from datetime import datetime

from django.db.models.signals import post_save, pre_delete, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.delete()
    except Profile.DoesNotExist:
        pass
    

@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Profile succesfully created at {datetime.now()}")
    else:
        print(f"Profile succesfully updated at {datetime.now()}")


@receiver(post_delete, sender=Profile)
def delete_user_profile(sender, instance, **kwargs):
    print(f"Profile deleted at {datetime.now()}")

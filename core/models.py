from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='user/avatar', blank=True)

    def get_username(self):
        return self.user.username

    def get_email(self):
        return self.user.email

    def __str__(self):
        return self.get_username()

    def save(self, *args, **kwargs):
        if not self.email or self.email != self.user.email:
            self.email = self.get_email()
        super().save(*args, **kwargs)


class Device(models.Model):
    title = models.CharField(max_length=255)
    configuration = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    used_by = models.ForeignKey(UserProfile, blank=True, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    item_number = models.IntegerField()
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, id=instance.id)
        instance.profile.save()






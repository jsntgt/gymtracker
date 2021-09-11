from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')
    background = models.ImageField(default='default_background.png', upload_to='background_images')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        img = Image.open(self.background.path)
        if img.height > 100 or img.width > 300:
            output_size = (300, 100)
            img.thumbnail(output_size)
            img.save(self.background.path)


from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import uuid
from ckeditor.fields import RichTextField
from PIL import Image
# Create your models here.

# class CustomUserManager(BaseUserManager):


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


User = get_user_model()


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name='user_profile')
    following = models.ManyToManyField(User, related_name='following', blank=True)
    follower = models.ManyToManyField(User, related_name='p_followers', blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(
        null=True, blank=True, default='users/default.png', upload_to='users/profile')
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True,
                              blank=True, choices=(
                                  ('MAN', 'Man'),
                                  ('FEMALE', 'Female'),
                                  ('OTHER', 'Other'),
                              ))
    business_area = models.CharField(null=True, blank=True, max_length=50)
    about = RichTextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

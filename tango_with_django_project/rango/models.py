from django.db import models

#task
from django.core.validators import RegexValidator
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

#task
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    avatar = models.ImageField(upload_to='profile_images', blank=False)
    # first_name=models.CharField(max_length=30, blank=False,default="abc")
    # last_name=models.CharField(max_length=30, blank=False,default="abc")
    country_code = models.CharField(max_length=5, blank=False)
    # email = models.EmailField( unique=True,blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=False)
    date = models.DateField(blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')

    def __str__(self):
        return self.user.username

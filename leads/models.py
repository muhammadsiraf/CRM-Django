from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.
import uuid


class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    age        = models.IntegerField(default=0)
    agent      = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        # from django.core.urlresolvers import reverse
        return reverse('detail_lead', kwargs={'pk': self.pk})
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Item(models.Model):
    TYPE_CHOICES = (
        ('Toys', 'Toys'),
        ('Guns', 'Guns'),
        ('Foods', 'Foods'),
        ('Electronics', 'Electronics'),
    )
    COLOR_CHOICE = (
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Black', 'Black'),
        ('White', 'White'),
    )
    ORIGIN_CHOICE = (
        ('Europe', 'Europe'),
        ('United States', 'United States'),
        ('China', 'China'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Others', 'Others'),
    )
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    color = models.CharField(choices=COLOR_CHOICE, max_length=20)
    date_of_make = models.DateField(auto_now=False, auto_now_add=False)
    origin = models.CharField(choices=ORIGIN_CHOICE, max_length=20)

    def __str__(self):
        return self.item_name

class Instance_Item(models.Model):
    uuid_id = models.UUIDField(default=uuid.uuid4())
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

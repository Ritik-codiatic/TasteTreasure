# local imp
from .custommanager import UserManager
# django imp
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# libs imp
from location_field.models.plain import PlainLocationField

#Create your models here.

class CustomUser(AbstractUser):
    types = (("Customer","Customer"),("Restaurent_Owner","Restaurent_Owner"))
    user_type = models.CharField(max_length=20,choices=types)
    mobile_number = models.CharField(null=True,max_length=10,unique=True,error_messages={
            'unique': _(
                "A user is already registered with this Mobile number"),
        },)
    address = models.TextField(max_length=100)
    gender_choices = (("Male","Male"),("Female","Female"))
    gender_types = models.CharField(max_length=20,choices=gender_choices)
    profile_pic = models.ImageField(upload_to='pics')
    city_name = models.ForeignKey('City',on_delete=models.CASCADE,null=True)
    username = None
    email = models.EmailField(_('email address'), unique=True,error_messages={
            'unique': _(
                "A user is already registered with this email address"),
        },)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self) -> str:
       return self.email


class City(models.Model):
    name = models.CharField(max_length=20)
    state = models.ForeignKey('State',on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Restaurants(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField()
    opening_time = models.TimeField(auto_now=False)
    closing_time = models.TimeField(auto_now=False)
    contact_number = models.IntegerField()
    cuisines = models.CharField(max_length=20)
    location = PlainLocationField(based_fields=['city'], zoom=7,null = True)

    def __str__(self) -> str:
        return self.name

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurants,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/restaurants_images')
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class RestaurantMenu(models.Model):
    restaurant = models.OneToOneField(Restaurants,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class MenuItems(models.Model):
    restaurant = models.ManyToManyField(RestaurantMenu)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics/menuitems')
    description = models.TextField(max_length=100)
    choice = (('veg','veg'),('non veg','non veg'))
    food_preference = models.CharField(max_length=20,choices=choice)
    
    def __str__(self) -> str:
        return self.name

class Notificatons(models.Model):
    user = models.ManyToManyField(CustomUser)
    headline = models.CharField(max_length=20)
    text = models.TextField(max_length=100)
       
    def __str__(self) -> str:
        return self.headline
    
class RestaurantFollowers(models.Model):
    followers = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    following = models.ForeignKey(Restaurants,on_delete=models.CASCADE)




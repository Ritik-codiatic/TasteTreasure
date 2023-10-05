from django.contrib import admin
from .models import CustomUser,Restaurants,State,City
# Register your models here

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _ 


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
        ...
        # add fields those needs to be visible while adding the data in form.
        
        add_fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'mobile_number', 'user_type', 'address', 'gender_types', 'profile_pic', 'city_name')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
                )
        list_display = ('email', 'first_name', 'last_name', 'is_staff')
        search_fields = ('email', 'first_name', 'last_name')
        ordering = ('email',)
admin.site.register(Restaurants)
admin.site.register(City)
admin.site.register(State)
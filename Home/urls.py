from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from .views import SignupFormView,LoginFormView,LogOutView,CustomerView,OwnerView
urlpatterns = [
    path('',TemplateView.as_view(template_name='home/home.html')),
    path('signup/',SignupFormView.as_view()),
    path('login/',LoginFormView.as_view()),
    path('logout/',LogOutView.as_view()),
    path('customer/',CustomerView.as_view()),
    path('owner/',OwnerView.as_view())
]
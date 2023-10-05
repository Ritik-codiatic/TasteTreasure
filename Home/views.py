from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm
from django.views.generic import View
from .models import *
from django.contrib import auth,messages
# Create your views here.

# def Home(request):
#     u = UserForm()

#     return render(request,'user/home.html',{'u':u})

class SignupFormView(View):
    form_class = UserForm
    template_name = 'home/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        
        if form.is_valid():
            #form.instance.username = form.cleaned_data['email']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            # mobile_number = form.cleaned_data['mobile_number']
            # user_type = form.cleaned_data['user_type']
            # address = form.cleaned_data['address']
            # gender_types = form.cleaned_data['gender_type']
            # profile_pic = form.cleaned_data['profile_pic']
            # city_name = form.cleaned_data['city.name']
            # user = CustomUser(username=username, first_name=first_name, last_name=last_name, email=email,
            #                    mobile_number=mobile_number, user_type=user_type, address=address,
            #                      gender_types=gender_types, profile_pic=profile_pic, city_name=city_name)
            form.save()
            return redirect('/')
        return render(request, self.template_name, context = {'form':form})


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'home/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, context = {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = auth.authenticate(
                email = form.cleaned_data["email"],
                password = form.cleaned_data["password"],
            )
            if user is not None:
                auth.login(request, user)
                if user.user_type == "Customer" :
                    return redirect('/customer') 
                else:
                    return redirect('/owner') 
            
        messages.info(request, "!login failed")
        return render(request, self.template_name, context = {'form':form})
            
class LogOutView(View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('/')
    
class CustomerView(View):
    template_name = 'user/userhome.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class OwnerView(View):
    template_name = 'owner/ownerhome.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
 
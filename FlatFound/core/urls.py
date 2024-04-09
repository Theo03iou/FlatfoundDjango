from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm, next_page='core/index.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm),  name='login'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/login.html',
         next_page='core/login.html'), name='logout'),
    path('about/', views.about, name='about'),
    path('infocontact/', views.infocontact, name='infocontact'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),          # related to base links
    path('terms/', views.terms, name='terms')
]

# Attempting to make the login screen the default

from django.contrib import admin
from django.urls import path
from . import views  # Import your views module
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.signup_view, name='signup'),  # Set the default view to signup_view
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.login_view, name='login'),
    path('index', views.index_view, name='index'),
    path('contact/', views.contact_view, name='contact')

]
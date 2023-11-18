from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_form_submission/', views.contact_form_submission, name='contact_form_submission'),
]
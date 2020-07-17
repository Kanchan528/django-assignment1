from django.urls import path
from .views import landingPage
app_name='website'

urlpatterns = [
    path('',landingPage, name='index')
]
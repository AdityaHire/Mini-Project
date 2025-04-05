from django.db.models.expressions import result
from django.urls import path
from .views import home_page, about_page, contact_page, recommend_medicine

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('recommend/', recommend_medicine , name='recommend'),
    path('contact/', contact_page, name='contact'),
]
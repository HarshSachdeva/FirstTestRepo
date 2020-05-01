from django.urls import path

from . import views

# Create your views here.
urlpatterns = [
    path('ecart', views.ecart, name='ecart'),
    path('register', views.register, name='register'),
    path('catalog', views.catalog, name='catalog'),
    path('review', views.review, name='review'),
    path('thankyou', views.thankyou, name='thankyou')
]
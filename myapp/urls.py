
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/',views.contact_view,name='contact'),
    path('service/', views.service, name='service'),
    path('product/', views.product, name='product'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('about/', views.about, name='about'),
    path('error/', views.error, name='error'),
]


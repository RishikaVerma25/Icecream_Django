from django.contrib import admin
from django.urls import path
from first_proj import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("",views.index,name='first_proj'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
]

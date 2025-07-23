from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_people, name='list_people'),  # Root URL now shows the list
    path('add/', views.add_person, name='add_person'),
    path('list/', views.list_people, name='list_people')  # Keep this for backward compatibility
]
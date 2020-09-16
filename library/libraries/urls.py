from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('books/<id>', views.books, name='library-b')
]
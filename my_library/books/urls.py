from django.urls import path
from books.views import bookslist , json_bookslist

urlpatterns = [
    path('list/' , bookslist),
    path('json/' ,json_bookslist)
]
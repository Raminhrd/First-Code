from django.shortcuts import render
from django.http.response import HttpResponse , JsonResponse


def bookslist(request):
    booklist:str = [
        '1: Harry potter book, ' ,
        '2: steven howking book, ',
        '3: clean code '
    ]
    return HttpResponse(booklist)

def json_bookslist(request):
    json_booklist:str = {
        '1': 'Harry potter book, ' ,
        '2' : 'steven howking book',
        '3' : 'clean code'
    }
    return JsonResponse(json_booklist)
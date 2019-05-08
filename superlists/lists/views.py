from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    htmlpage = """<html>
    <head>
    <title>To-Do Lists</title>
    </head>
    </html>"""
    return HttpResponse(htmlpage)

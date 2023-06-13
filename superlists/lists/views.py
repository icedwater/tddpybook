from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse("""<html>
        <head>
            <title>To-Do lists</title>
        </head>
        <body>
            <h1>To-Do</h1>
            <input id = "new_item" placeholder = "What next?"></input>
        </body>
    </html>""")

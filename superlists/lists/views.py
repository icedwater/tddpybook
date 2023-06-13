from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "home.html", {
        "item_text": request.POST.get("to_do", ''),
    })

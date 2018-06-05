from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    title = "Welcome"
    if request.user.is_authenticated:
        title = "My Title %s" %(request.user)

    #Add form
    context = {
        "title": title
    }
    return render(request, 'home.html', context)

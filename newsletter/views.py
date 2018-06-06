from django.shortcuts import render
from .forms import SignUpForm, ContactForm

# Create your views here.


def home(request):
    title = "Welcome"
    # if request.user.is_authenticated:
    #     title = "My Title %s" %(request.user)

    #Add form
    # if(request.method=='POST'):
    #     print(request.POST)

    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        # form.save()
        print(request.POST['email'])
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"

        instance.full_name = full_name

        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, 'home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        # for key in form.cleaned_data:
        #     print(key, form.cleaned_data.get(key))

        for key, value in form.cleaned_data.items():
            print(key, value)


        # email = form.cleaned_data.get('email')
        # message = form.cleaned_data.get('message')
        # full_name = form.cleaned_data.get('full_name')

    context = {
        "title": "Contact US",
        "form": form,
    }
    return render(request, 'forms.html', context)

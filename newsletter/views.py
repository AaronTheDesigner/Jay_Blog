from django.shortcuts import render
from .models import Newsletter
from .forms import NewsletterUserSignUpForm

# Create your views here.
def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Newsletter.object.filter(email=instance.email).exists():
            print("Sorry. This email already exists")
        else:
            instance.save()

    context = {
        "form": form,
    }

    template = "newsletters/sign_up.html"
    return render(request, template, context)

def newsletter_unsubscribe(request):
    form = NewsletterSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Newsletter.objects.filter(email=instance.email).exists():
            Newsletter.objects.filter(email=instance.email).delete()
        else:
            print("We did not find your email address")

    context = {
        "form": form,
    }

    template = "newsletters/sign_up.html"
    return render(request, template, context)

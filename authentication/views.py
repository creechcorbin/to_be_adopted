from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.views.generic.base import TemplateView
from tbauser.models import AdoptUser
from pets.models import Pet
from tbauser.forms import AdoptUserCreationForm
from authentication.forms import LoginForm, SignupForm

def index(request):
    pets = Pet.objects.all()
    return render (request, 'index.html', {'pets': pets})


class SignupView(TemplateView):
    
    def get(self, request):
        form = SignupForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = AdoptUser.objects.create_user(
                username=data.get('username'), 
                password=data.get('password'), 
                display_name=data.get('display_name'), 
                account_type=data.get('account_type')
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, 'generic_form.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, 
                username=data.get("username"), 
                password=data.get("password")
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
                
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

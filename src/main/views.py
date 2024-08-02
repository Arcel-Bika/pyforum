from datetime import timezone

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from main.models import CustomUser, Category, Forum
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, DetailView, ListView

User = CustomUser


class SignUpView(View):
    def get(self, request):
        return render(request, 'registration/signup.html')

    def post(self, request):
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        city = request.POST['city']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'registration/signup.html',
                          {'error': 'Les mots de passe ne correspondent pas.'})

        if User.objects.filter(email=email).exists():
            return render(request, 'registration/signup.html',
                          {'error': 'Cet email est déjà utilisé.'})

        user = User.objects.create_user(email=email, first_name=first_name,
                                        last_name=last_name, username=user_name,
                                        city=city, password=password1)
        login(request, user)
        return redirect('home')


class CustomLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = CustomUser
            login(request, user)
            return redirect('home')
        return render(request, 'registration/login.html', {'form': form})


class HomeView(TemplateView):
    template_name = 'home.html'


class DashboardView(ListView):
    model = Forum
    template_name = 'dashboard.html'  # Spécifiez le template à utiliser
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = CustomUser.objects.count()
        return context



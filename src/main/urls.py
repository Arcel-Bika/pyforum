from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, CustomLoginView, DashboardView, logout_user, ProfilView, ForumView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("logout/", logout_user, name="logout"),
    path("profil/", ProfilView.as_view, name="profil"),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('forum/', ForumView.as_view(), name='forum'),
    path('', auth_views.TemplateView.as_view(template_name='home.html'), name='home'),  # Page d'accueil
]

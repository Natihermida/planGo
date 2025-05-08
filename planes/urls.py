from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('panel/', views.panel_usuario, name='panel_usuario'),
    path('crear/', views.crear_plan, name='crear_plan'),
    path('plan/<int:id>/', views.ver_plan, name='ver_plan'),
]
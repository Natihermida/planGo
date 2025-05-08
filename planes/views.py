from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Plan
from .forms import PlanForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def landing(request):
    planes = Plan.objects.all().order_by('-fecha')
    return render(request, 'landing.html', {'planes': planes})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('panel_usuario')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def panel_usuario(request):
    planes_creados = request.user.planes_creados.all()
    planes_disponibles = Plan.objects.exclude(participantes=request.user)
    return render(request, 'panel.html', {
        'planes_creados': planes_creados,
        'planes_disponibles': planes_disponibles,
    })

@login_required
def crear_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.creador = request.user
            plan.save()
            form.save_m2m()
            return redirect('panel_usuario')
    else:
        form = PlanForm()
    return render(request, 'crear_plan.html', {'form': form})

@login_required
def ver_plan(request, id):
    plan = get_object_or_404(Plan, id=id)
    return render(request, 'ver_plan.html', {'plan': plan})

def logout_view(request):
    logout(request)
    return redirect('landing')  # o usa '/' directamente

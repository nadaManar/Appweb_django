from django.shortcuts import get_object_or_404,render,redirect
from .models import Formation
from .models import UE
from .forms import UEForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
@login_required
def principale(request):
    if not request.user.is_authenticated:
       return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    return render(request,'principale.html')
@login_required
def about(request):
    return render(request,'about.html')
@login_required
def formation_detail(request,n):
    formation = get_object_or_404(Formation,id=n)
    ues = formation.ues.all()
    return render(request, 'formation_detail.html', {'formation': formation,'ues': ues})
@login_required
def ue_detail(request, m):
    ue = get_object_or_404(UE, id=m)
    formations = ue.formations.all()  
    return render(request, 'ue_detail.html', {'ue': ue, 'formations': formations})
@login_required
def formation_all(request):
    formations = Formation.objects.all()
    return render(request, 'formation_all.html', {'formations': formations})
@login_required
def ue_all(request):
    ues = UE.objects.all()  
    return render(request, 'ue_all.html', {'ues': ues})


@login_required
def ajouter_ue(request):
    if not request.user == Formation.responsable:
        return redirect('ue_all')
    if request.method == 'POST':
        form = UEForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ue_all')  
    else:
        form = UEForm()
    return render(request, 'ue_ajouter.html', {'form': form})

@login_required
def modifier_ue(request, m):
    ue = get_object_or_404(UE, id=m)
    if not ue.responsables.filter(id=request.user.id).exists():
        return redirect('ue_all')
    if request.method == 'POST':
        form = UEForm(request.POST, instance=ue)
        if form.is_valid():
            form.save()
            return redirect('ue_detail', m=ue.id)  
    else:
        form = UEForm(instance=ue)
    return render(request, 'ue.modifier.html', {'form': form, 'ue': ue})
from django.shortcuts import get_object_or_404, redirect, render
@login_required
def supprimer_ue(request, ue_id):
    ue = get_object_or_404(UE, id=ue_id)
    if not request.user == Formation.responsable:
        return redirect('ue_all')
        return redirect('ue_all')
    if request.method == 'POST':
        ue.delete()
        return redirect('ue_all')  
    
    return render(request, 'supprimer_ue.html', {'ue': ue})
@login_required
def formation_responsable(request, n):
    formation = get_object_or_404(Formation, id=n)
    if formation.responsable != request.user:
        return redirect('formation_all')
    ues = formation.ues.all()  
    total_ues = ues.count()
    responsables_ue = set() 
    for ue in ues:
      responsables_ue.update(ues.responsables.all())
    total_cm = ues.aggregate(Sum('CM'))['CM__sum'] or 0
    total_td = ues.aggregate(Sum('TD'))['TD__sum'] or 0
    total_tp = ues.aggregate(Sum('TP'))['TP__sum'] or 0
    total_heures_td = total_cm * 1.5 + total_td + total_tp
    total_ects = ues.aggregate(Sum('credits'))['credits__sum'] or 0
    context = {
        'formation': formation,
        'ues': ues,
        'total_ues': total_ues,
        'responsables_ue': responsables_ue,
        'total_cm': total_cm,
        'total_td': total_td,
        'total_tp': total_tp,
        'total_heures_td': total_heures_td,
        'total_ects': total_ects,
    }

    return render(request, 'formation_responsable.html', context)

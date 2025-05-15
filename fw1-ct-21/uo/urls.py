from django.urls import path
from .views import about 
from . import views 

urlpatterns = [
    path('', views.principale, name='principale'),
    path('about/', about , name='about'),
    path('formation/<int:n>/', views.formation_detail, name='formation_detail'),
    path('ue/<int:m>/', views.ue_detail, name='ue_detail'),
    path('all/',views.formation_all,name='formation_all'),
    path('ues/',views.ue_all,name='ue_all'),
    path('ue/ajouter/', views.ajouter_ue, name='ajouter_ue'),
    path('ue/modifier/<int:m>/', views.modifier_ue, name='modifier_ue'),
    path('ue/supprimer/<int:ue_id>/', views.supprimer_ue, name='supprimer_ue'),
    path('formation/<int:n>/details/', views.formation_responsable, name='formation_responsable'),
]

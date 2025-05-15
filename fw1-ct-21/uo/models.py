from django.db import models
from django.contrib.auth.models import User 

class Formation(models.Model):
    intitule = models.CharField(max_length=100)
    description = models.TextField()
    responsable = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, unique=True,related_name='formations_responsables')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.intitule
    



class UE(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    CM = models.IntegerField()
    TD = models.IntegerField()
    TP = models.IntegerField()
    credits = models.IntegerField()
    formations = models.ManyToManyField(Formation, related_name='ues')
    responsables = models.ManyToManyField(User, related_name='ues_responsables')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.titre



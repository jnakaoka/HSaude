from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Medicos(models.Model):
    name = models.CharField(max_length=100)
    especialidade = models.TextField()
    city = models.CharField(max_length=100)
    creatd_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE )

    def __str__(self):
        return 'id: {} {} {} {} {} '.format(self.id, self.name, self.especialidade, self.city, self.creatd_date, self.active,self.user)
    
class Meta:
    db_table = 'medico'
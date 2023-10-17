from django.db import models

# Create your models here.
class proyect(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    proyect = models.ForeignKey(proyect, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.proyect.name
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    T_documento = models.CharField(max_length=50)
    N_documento = models.CharField(max_length=50, unique=True) # Número de documento único

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
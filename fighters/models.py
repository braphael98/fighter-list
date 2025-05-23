from django.db import models

class Fighter(models.Model):

    difficulty_level_choises = [
        ("FACIL", 'Facil'),
        ("MEDIO", 'Medio'),
        ("AVANÇADO",'Avançado'),
    ]
    
    name = models.CharField(max_length= 100, null = False, blank= False)
    description = models.TextField(null = False, blank= False)
    difficulty_level = models.CharField(max_length=100, choices=difficulty_level_choises,default='')
    
    combo = models.TextField()
    
    def __str__(self):
        return self.name


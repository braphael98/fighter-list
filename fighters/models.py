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
    photo = models.ImageField(upload_to='fighters/', null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


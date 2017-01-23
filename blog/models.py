from django.db import models
from django.utils import timezone


class Post(models.Model): #Define nuestro Modelo
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)#define un texto con maximo de 200 caracteres
	text =   models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null=True)


	def  publish(self): #define nuestra Funcion o Metodo con minusculas
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title





#class- indica que estmos definiendo un object()
# post  - es el nombre de nuestro objeto, siempre comienza con mayuscula
#models.Model - significa que Post es un modelo de Django, asi django sabe que debe
			#	guararlo en la base de datos.



from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
	desc = models.TextField(null=True,verbose_name="Описание")
	img = models.CharField(max_length=100, null=True, verbose_name="Фото")
	name = models.CharField(max_length=50, unique=True, verbose_name="Категория")

	def __str__(self):
		return self.name

class Pizza(models.Model):
	name = models.CharField(max_length=50, unique=True, verbose_name="Название")
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
	desc = models.TextField(verbose_name="Описание")
	img = models.CharField(max_length=100, null=True, verbose_name="Фото")
	price = models.CharField(max_length=50, verbose_name="Цена")

	def __str__(self):
		return self.name

class Salad(models.Model):
	name = models.CharField(max_length=50, unique=True, verbose_name="Название")
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
	desc = models.TextField(verbose_name="Описание")
	img = models.CharField(max_length=100, null=True, verbose_name="Фото")
	price = models.CharField(max_length=50, verbose_name="Цена")

	def __str__(self):
		return self.name

class Steak(models.Model):
	name = models.CharField(max_length=50, unique=True, verbose_name="Название")
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
	desc = models.TextField(verbose_name="Описание")
	img = models.CharField(max_length=100, null=True, verbose_name="Фото")
	price = models.CharField(max_length=50, verbose_name="Цена")

	def __str__(self):
		return self.name

class Comment(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	body = models.TextField(verbose_name="Comments", default="Write your Comment")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Date", null=True, blank=True)

	def __str__(self):
 		return self.body






from django.db import models
from django.conf import settings
import datetime
from django.utils.text import slugify
# Create your models here.
User = settings.AUTH_USER_MODEL

class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(unique=True, null=True, blank=True)
	class Meta:
		verbose_name = 'Categorie'
	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)




class Newspaper(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=500, unique=True, blank=False, null=False)
	text = models.TextField(blank=False, null=False)
	image = models.ImageField(null=True, blank=True, default='default.png')
	date = models.DateTimeField(default=datetime.datetime.now())

	def __str__(self):
		return self.title



class Verificateuser(models.Model):
	user_v = models.OneToOneField(User, unique=True, null=True, on_delete=models.CASCADE)
	verificated = models.BooleanField(default=False)
	date = models.DateTimeField(default=datetime.datetime.now())
	image = models.ImageField(default='user.png')
	def __str__(self):
		return f'{self.user_v.username}, {self.verificated}'


















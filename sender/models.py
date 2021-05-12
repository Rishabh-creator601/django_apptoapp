from django.db import models

# Create your models here.
class Profile(models.Model):
	id = models.AutoField
	name = models.CharField(max_length=20)
	age = models.IntegerField()
	proffession = models.CharField(max_length=30)
	choices = (('male','male'),('female','female'),('others','others'))
	gender =models.CharField(max_length=10,choices=choices,default='male')

	
	
	def __str__(self):
		return self.name

from django.db import models

# Create your models here.
class Country(models.Model):
	name          = models.CharField(unique=True, max_length=50)
	description   = models.TextField(max_length=250)
	population    = models.IntegerField()
	gdp           = models.FloatField()

	def __str__(self):
		return '{} {}'.format(self.name, self.description)


class State(models.Model):
	country       = models.ForeignKey(Country, on_delete=models.CASCADE)
	name          = models.CharField(unique=True, max_length=50)
	description   = models.TextField(max_length=250)
	population    = models.IntegerField()
	gdp           = models.FloatField()

	def __str__(self):
		return '{} {}'.format(self.name, self.description)


class City(models.Model):
	country       = models.ForeignKey(Country, on_delete=models.CASCADE)
	state         = models.ForeignKey(State, on_delete=models.CASCADE)
	name          = models.CharField(unique=True, max_length=50)
	description   = models.TextField(max_length=250)
	population    = models.IntegerField()
	gdp           = models.FloatField()
	pin_code      = models.CharField(verbose_name="Pin Code", unique=True, max_length=6)

	def __str__(self):
		return '{} {}'.format(self.name, self.description)

class Town(models.Model):
	country       = models.ForeignKey(Country, on_delete=models.CASCADE)
	state         = models.ForeignKey(State, on_delete=models.CASCADE)
	name          = models.CharField(unique=True, max_length=50)
	description   = models.TextField(max_length=250)
	population    = models.IntegerField()
	gdp           = models.FloatField()
	pin_code      = models.CharField(verbose_name="Pin Code", unique=True, max_length=6)

	def __str__(self):
		return '{} {}'.format(self.name, self.description)

class Person(models.Model):
	town          = models.ForeignKey(Town, on_delete=models.CASCADE)
	name          = models.CharField(unique=True, max_length=50)

	def __str__(self):
		return self.name

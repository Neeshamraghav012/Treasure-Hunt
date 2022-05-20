from django.db import models

# Create your models here.

class Questions(models.Model):

	qtoken = models.CharField(max_length = 1000)
	qsno = models.IntegerField()
	# question batch number.
	qbno = models.IntegerField(default = 0)
	nextlink = models.CharField(max_length = 1000)

	def __str__(self):

		return f"{self.qtoken}"


class Team(models.Model):

	temail = models.EmailField(max_length = 1000)
	tcode = models.CharField(max_length = 100)
	tname = models.CharField(max_length = 300)
	# team batch number.
	tbno = models.IntegerField(default = 0)
	tdone = models.IntegerField(default = 0)

	def __str__(self):

		return f"{self.tname}"

class Entries(models.Model):

	#eid = models.IntegerField()
	team = models.ForeignKey(Team, on_delete = models.CASCADE)
	qtoken = models.CharField(max_length = 1000)
	time = models.DateTimeField(auto_now_add = True)
	isvalid = models.BooleanField(default = False)

	def __str__(self):

		return f"{self.team.tname} -- {self.isvalid}"
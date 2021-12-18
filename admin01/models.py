from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class topheading(models.Model):
	theading=models.CharField(max_length=500)
class score(models.Model):
	totalscore=models.CharField(max_length=100)
	vicket=models.CharField(max_length=100)
	balls=models.CharField(max_length=100)
	over=models.CharField(max_length=100)
class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

class Team(models.Model):
	team_name=models.CharField(max_length=200)
	team_captain=models.CharField(max_length=200)
	team_score=models.CharField(max_length=200)
	team_wicket=models.CharField(max_length=20)

class Heading(models.Model):
	heading_data=models.CharField(max_length=1000)

class Overs(models.Model):
	b1=models.CharField(max_length=10,blank=True)
	b2=models.CharField(max_length=10)
	b3=models.CharField(max_length=10)
	b4=models.CharField(max_length=10)
	b5=models.CharField(max_length=10)
	b6=models.CharField(max_length=10)
class Over_count(models.Model):
	over=models.CharField(max_length=10)


class Maindata(models.Model):
	team_name=models.CharField(max_length=200)
	team_captain=models.CharField(max_length=200)
	team_score=models.CharField(max_length=200)
	team_wicket=models.CharField(max_length=20)

class welcomepage(models.Model):
	h1=models.CharField(max_length=100)
	h2=models.CharField(max_length=100)

class show_over(models.Model):
	sover=models.CharField(max_length=100)


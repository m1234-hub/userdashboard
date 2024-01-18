import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    starting_balance = models.FloatField(default=0)
    growth = models.FloatField(default=0)


class ActualReturns(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='associated user')
    value = models.FloatField(default=0)
    day = models.IntegerField(default=1)
    
class Journaal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    pair = models.CharField(max_length=70)
    session = models.CharField(max_length=100)
    pips = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    entry_time = models.CharField(max_length=70)
    comment = models.CharField(max_length=100)
    chart_before = models.URLField(max_length=100)
    chart_after = models.URLField(max_length=70)
    profit = models.CharField(max_length=70)
    
class TradingPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    goals = models.TextField(blank=True)
    milestone_timeline = models.TextField(blank=True)
    strengths = models.TextField(blank=True)
    weaknesses = models.TextField(blank=True)
    opportunities = models.TextField(blank=True)
    threats = models.TextField(blank=True)
    

    # Other fields as per your document


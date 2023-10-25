from django.db import models

# Create your models here.
class GraphData(models.Model):
    end_year=models.CharField(max_length=500, blank=True, null=True)
    intensity= models.CharField(max_length=500, blank=True, null=True)
    sector= models.CharField(max_length=500, blank=True, null=True) 
    topic= models.CharField(max_length=500, blank=True, null=True)
    insight= models.CharField(max_length=500, blank=True, null=True) 
    url= models.CharField(max_length=500, blank=True, null=True) 
    region= models.CharField(max_length=500, blank=True, null=True) 
    start_year= models.CharField(max_length=500, blank=True, null=True) 
    impact= models.CharField(max_length=500, blank=True, null=True) 
    added= models.CharField(max_length=500, blank=True, null=True) 
    published= models.CharField(max_length=500, blank=True, null=True) 
    country= models.CharField(max_length=500, blank=True, null=True) 
    relevance= models.CharField(max_length=500, blank=True, null=True) 
    pestle= models.CharField(max_length=500, blank=True, null=True) 
    source= models.CharField(max_length=500, blank=True, null=True) 
    title= models.CharField(max_length=500, blank=True, null=True) 
    likelihood= models.CharField(max_length=500, blank=True, null=True)
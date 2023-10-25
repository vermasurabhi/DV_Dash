from rest_framework import serializers
from .models import GraphData

class graphDataSerializer(serializers.ModelSerializer):
    end_year=serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    intensity= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    sector= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    topic= serializers.CharField(max_length=500, allow_blank=True, allow_null=True )
    insight= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    url= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    region= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    start_year= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    impact= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    added= serializers.CharField(max_length=500, allow_blank=True, allow_null=True) 
    published= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    country= serializers.CharField(max_length=500, allow_blank=True, allow_null=True  ) 
    relevance= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    pestle= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    source= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    title= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 
    likelihood= serializers.CharField(max_length=500, allow_blank=True, allow_null=True ) 

    class Meta:
        model=GraphData
        fields=('__all__')
        extra_kwargs = {"end_year": {"required": False, "allow_null": True}}
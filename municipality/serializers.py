from rest_framework import serializers
from .models import All,All_Temp

class AllSerializer(serializers.ModelSerializer):
	class Meta:
		model = All
		fields = '__all__'
		
class All_TempSerializer(serializers.ModelSerializer):
	class Meta:
		model = All_Temp
		fields = '__all__'
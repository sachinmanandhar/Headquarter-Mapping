import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from .models import WardForm, WardFormTemp

"""
class FormSerializer(serializers.ModelSerializer):
	class Meta:
		model = Form
		fields = '__all__'
"""
	
class TryFormSerializer(serializers.ModelSerializer):
	class Meta:
		model = WardForm
		fields = '__all__'
		
class FormSerializerTemp(serializers.ModelSerializer):
	class Meta:
		model = WardFormTemp
		fields = '__all__'
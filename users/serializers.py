from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', 'address' )
		
class tokenser(serializers.ModelSerializer):
	class Meta:
		model=models.CustomUser
		fields="__all__"
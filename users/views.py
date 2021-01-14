from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers

class UserListView(generics.ListAPIView):
	queryset = models.CustomUser.objects.all()
	serializer_class = serializers.UserSerializer
	

		
		
class getUser(APIView):
	def get(self,request):
		user=Token.objects.get(key=request.query_params.get('token')).user
		serializer=serializers.tokenser(user)
		return Response(serializer.data)
	

		
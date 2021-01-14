from django.shortcuts import render
from rest_framework import viewsets, permissions          # add this
from .serializers import AllSerializer,All_TempSerializer     # add this
from .models import All,All_Temp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.http import HttpResponse
import datetime

class MunPostTemp(APIView):
	def post(self,request):
		data_Serializer = All_TempSerializer(data=request.data)
		if data_Serializer.is_valid():
			data_Serializer.save()
			return Response({'PalikaName':data_Serializer.data.get('PalikaName'),
							 'DateTime':datetime.datetime.now()},status=status.HTTP_201_CREATED)
		return Response({'key': 'value'})
		
class MunGetAll(APIView):
	def get(self,request):
		MunData=All.objects.all()
		serializer=AllSerializer(MunData,many=True)
		return Response(serializer.data)
		
class MunGetDist(APIView):
	def get(self,request):
		MunData=All.objects.filter(districtID=request.query_params.get('districtID'))
		serializer=AllSerializer(MunData,many=True)
		return Response(serializer.data)

class MunGet(APIView):
	def get(self,request):
		MunData=All.objects.filter(munID=request.query_params.get('munid'))
		serializer=AllSerializer(MunData,many=True)
		return Response(serializer.data)
		
def upd():
	val=All_Temp.objects.values('munID')
	for i in val.values():
		for key,value in i.items():
			if(key=='munID'):
				vmunID=value
			if(key=='fid'):
				vfid=value
			if(key=='districtID'):
				vdistrictID=value
			if(key=='ProvinceName'):
				vProvinceName=value
			if(key=='DistrictName'):
				vDistrictName=value
			if(key=='PalikaName'):
				vPalikaName=value
			if(key=='PalikaType'):
				vPalikaType=value
			if(key=='TotalWards'):
				vTotalWards=value
			if(key=='HQMunicipalCenter'):
				vHQMunicipalCenter=value
			if(key=='NumberingTotalPalikas'):
				vNumberingTotalPalikas=value
			if(key=='NoPalikaPerDistrict'):
				vNoPalikaPerDistrict=value
			if(key=='ContactPersonITOfficer'):
				vContactPersonITOfficer=value
			if(key=='ContactPersonPhNumb'):
				vContactPersonPhNumb=value
			if(key=='ContactNumMunicipality'):
				vContactNumMunicipality=value
			if(key=='Website'):
				vWebsite=value
			if(key=='Email'):
				vEmail=value
			if(key=='TotalArea'):
				vTotalArea=value
			if(key=='TotPopulation'):
				vTotPopulation=value
			if(key=='TotMale'):
				vTotMale=value
			if(key=='TotFemale'):
				vTotFemale=value
			if(key=='TotHousehold'):
				vTotHousehold=value
			if(key=='Xcord'):
				vXcord=value
			if(key=='Ycord'):
				vYcord=value
			if(key=='verification'):
				vverification=value
			
		if vverification=='verified':
			data=All.objects.filter(munID=vmunID).update(
													munID=vmunID,
													fid=vfid,
													districtID=vdistrictID,
													ProvinceName=vProvinceName,
													DistrictName=vDistrictName,
													PalikaName=vPalikaName,
													PalikaType=vPalikaType,
													TotalWards=vTotalWards,
													HQMunicipalCenter=vHQMunicipalCenter,
												
													NumberingTotalPalikas=vNumberingTotalPalikas,
													NoPalikaPerDistrict=vNoPalikaPerDistrict,
													ContactPersonITOfficer=vContactPersonITOfficer,
													ContactPersonPhNumb=vContactPersonPhNumb,
													ContactNumMunicipality=vContactNumMunicipality,
													Website=vWebsite,
													Email=vEmail,
													TotalArea=vTotalArea,
													TotPopulation=vTotPopulation,
													TotMale=vTotMale,
													TotFemale=vTotFemale,
													TotHousehold=vTotHousehold,
													Xcord=vXcord,
													Ycord=vYcord,
													verification=vverification)
				
		
	All_Temp.objects.filter(verification='verified').delete()
	print("Done, refresh the database")
	
def update(request):
	upd()
	return HttpResponse('Please Reload the Database')
"""
if __name__ == "__upd__":
    upd()
"""	
"""	
def upd():
	with connection.cursor() as cursor:
		cursor.execute("UPDATE All SET ProvinceName=b.ProvinceName,verification = b.verification FROM All_Temp b WHERE munID = b.munIDD")
"""
	
from django.shortcuts import render
from rest_framework import viewsets, permissions          # add this
from .serializers import TryFormSerializer, FormSerializerTemp      # add this
from .models import WardForm, WardFormTemp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.http import HttpResponse

# Create your views here.
"""
class FormView(viewsets.ModelViewSet):       # add this
	serializer_class = FormSerializer          # add this
	queryset = Form.objects.all() 
	permissions_classes=(permissions.IsAuthenticatedOrReadOnly,)
"""
	
class TryFormView(viewsets.ModelViewSet):       # add this
	serializer_class = TryFormSerializer          # add this
	queryset = WardForm.objects.all()	
	permissions_classes=(permissions.IsAuthenticatedOrReadOnly,)

	
"""def InputForm(request):
	request.CONTENT_TYPE('application/json')
	request.REMOTE_ADDR('http://localhost:3000/')
	Fprov=request.POST.get('selectedPro')
	Fdist=request.POST.get('selectedDistrict')
	FpalikaT=request.POST.get('selectedPalikaType')
	FpalikaN=request.POST.get('enteredPalikaName')
	FWardN=request.POST.get('enteredWardNo')
	FWardOf=request.POST.get('enteredWardOfficeAddress')
	FWardC=request.POST.get('enteredWardContactNo')
	FX=float(request.POST.get('enteredXCords'))
	FY=float(request.POST.get('enteredYCords'))
	FChaipersonN=request.POST.get('enteredChairPersonName')
	FChairpersonC=request.POST.get('enteredChaiPersonContact')
	FSecN=request.POST.get('enteredSecretaryName')
	FSecC=request.POST.get('enteredSecretaryContact')
	FArea=request.POST.get('enteredArea')
	FHouseholds=request.POST.get('enteredHouseholds')
	FPop=request.POST.get('enteredTotalPop')
	FFepop=request.POST.get('enteredMalePop')
	Fmapop=request.POST.get('enteredFemalePop')
	FWeb=request.POST.get('enteredWebsite')
	FEmail=request.POST.get('enteredEmail')
	new=Form(Province=Fprov,
			 District=Fdist,
			 PalikaType=FpalikaT,
			 PalikaName=FpalikaN,
			 Ward_No=FWardN,
			 Ward_Office_Address=FWardOf,
			 Ward_Contact_No=FWardC,
			 X_Cords=FX,
			 Y_Cords=FY,
			 Chairperson_Name=FChaipersonN,
			 Chaiperson_Contact_No=FChairpersonC,
			 Secretary_Name=FSecN,
			 Secretary_Contact_No=FSecC,
			 Area=FArea,
			 Total_Households=FHouseholds,
			 Total_Population=FPop,
			 Total_Male_Population=Fmapop,
			 Total_Female_Population=FFepop,
			 Website=FWeb,
			 Email=FEmail,
			 location=Point(FX,FY, srid = 4326))
	form.save()
"""
class WardFormAll(APIView):
	def get(self,request):
		formData=WardForm.objects.all()
		#formData=WardForm.objects.filter(Object_id=request.query_params.get('Object_id'))
		serializer=TryFormSerializer(formData,many=True)
		return Response(serializer.data)
		
class WardFormMun(APIView):
	def get(self,request):
		#formData=TryForm.objects.all()
		formData=WardForm.objects.filter(munid=request.query_params.get('munid'))
		serializer=TryFormSerializer(formData,many=True)
		return Response(serializer.data)
		
class formAPI(APIView):
	def get(self,request):
		#formData=TryForm.objects.all()
		formData=WardForm.objects.filter(Object_id=request.query_params.get('Object_id'))
		serializer=TryFormSerializer(formData,many=True)
		return Response(serializer.data)
	"""	
	def post(self,request):
		data_Serializer = TryFormSerializer(data=request.data)
		if data_Serializer.is_valid():
			data_Serializer.save()
			return Response({'PalikaName':data_Serializer.data.get('enteredPalikaName'),
							 'DateTime':datetime.datetime.now()},status=status.HTTP_201_CREATED)
		return Response({'key': 'value'})
	#permissions_classes=(permissions.IsAuthenticatedOrReadOnly,)
	
	"""
class postFormAPI(APIView):
	def post(self,request):
		data_Serializer = FormSerializerTemp(data=request.data)
		if data_Serializer.is_valid():
			data_Serializer.save()
			return Response({'PalikaName':data_Serializer.data.get('palika_name'),
							 'DateTime':datetime.datetime.now()},status=status.HTTP_201_CREATED)
		return Response({'key': 'value'})	
	
def upd():
	val=WardFormTemp.objects.values('Object_id')
	for i in val.values():
		for key,value in i.items():
			if(key=='Object_id'):
				vObject_id=value
			if(key=='munid'):
				vmunid=value
			if(key=='province'):
				vprovince=value
			if(key=='ward_no'):
				vward_no=value
			if(key=='DISTRICT'):
				vDISTRICT=value
			if(key=='palika_name'):
				vPalikaName=value
			if(key=='palika_type'):
				vPalikaType=value
			if(key=='Area'):
				vArea=value
			if(key=='Ward_Office_Address'):
				vWard_Office_Address=value
			if(key=='Ward_Contact_No'):
				vWard_Contact_No=value
			if(key=='Chairperson_Name'):
				vChairperson_Name=value
			if(key=='Chaiperson_Contact_No'):
				vChaiperson_Contact_No=value
				
			if(key=='Secretary_Name'):
				vSecretary_Name=value
			if(key=='Secretary_Contact_No'):
				vSecretary_Contact_No=value
				
			if(key=='Total_Households'):
				vTotal_Households=value
			if(key=='Total_Population'):
				vTotPopulation=value
			if(key=='Total_Male_Population'):
				vTotMale=value
			if(key=='Total_Female_Population'):
				vTotFemale=value	
			if(key=='Website'):
				vWebsite=value
			if(key=='Email'):
				vEmail=value
			
			if(key=='X_Cords'):
				vXcord=value
			if(key=='X_Cords'):
				vYcord=value
			if(key=='Verification'):
				vverification=value
			
	
		if vverification=='verified':
			data=WardForm.objects.filter(Object_id=vObject_id).update(
											Object_id=vObject_id,
											munid=vmunid,
											province=vprovince,
											ward_no=vward_no,
											DISTRICT=vDISTRICT,
											palika_name=vPalikaName,
											palika_type=vPalikaType,
											Area=vArea,
											Ward_Office_Address=vWard_Office_Address,
											Ward_Contact_No=vWard_Contact_No,
											Chairperson_Name=vChairperson_Name,
											Chaiperson_Contact_No=vChaiperson_Contact_No,
											Secretary_Name=vSecretary_Name,
											Secretary_Contact_No=vSecretary_Contact_No,
											Total_Households=vTotal_Households,
											Total_Population=vTotPopulation,
											Total_Male_Population=vTotMale,
											Total_Female_Population=vTotFemale,
											Website=vWebsite,
											Email=vEmail,
											X_Cords=vXcord,
											Y_Cords=vYcord,
											Verification=vverification
												)
				
		
	WardFormTemp.objects.filter(Verification='verified').delete()
	print("Done, refresh the database")
	
def updateW(request):
	upd()
	return HttpResponse('Please Reload the Database')


	

	
	

from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
"""
class Form(models.Model):
	Province=models.CharField(max_length=100,null=True, blank=True)
	District=models.CharField(max_length=100,null=True, blank=True)
	PalikaType=models.CharField(max_length=100,null=True, blank=True)
	PalikaName=models.CharField(max_length=100,null=True, blank=True)
	Ward_No=models.CharField(max_length=100,null=True, blank=True)
	Ward_Office_Address=models.CharField(max_length=100,null=True, blank=True)
	Ward_Contact_No=PhoneNumberField()
	X_Cords=models.FloatField(null=True, blank=True)	
	Y_Cords=models.FloatField(null=True, blank=True)
	Chairperson_Name=models.CharField(max_length=100,null=True, blank=True)
	Chaiperson_Contact_No=PhoneNumberField()
	Secretary_Name=models.CharField(max_length=100,null=True, blank=True)
	Secretary_Contact_No=PhoneNumberField()
	Area=models.FloatField(max_length=100,null=True, blank=True)
	Total_Households=models.IntegerField(null=True, blank=True)
	Total_Population=models.IntegerField(null=True, blank=True)
	Total_Male_Population=models.IntegerField(null=True, blank=True)
	Total_Female_Population=models.IntegerField(null=True, blank=True)
	Website= models.URLField(max_length=200)
	Email=models.EmailField(max_length=254)
	location= models.PointField(srid=4326)
def __str__(self):
    return 'PalikaName: %s' % self.name
"""

class WardForm(models.Model):
	Object_id=models.CharField(max_length=100,null=False, blank=False, primary_key=True)
	munid=models.CharField(max_length=100,null=True, blank=True)
	province=models.CharField(max_length=100,null=True, blank=True)
	ward_no=models.CharField(max_length=100,null=True, blank=True)
	DISTRICT=models.CharField(max_length=100,null=True, blank=True)
	palika_name=models.CharField(max_length=100,null=True, blank=True)
	palika_type=models.CharField(max_length=100,null=True, blank=True)
	Area=models.CharField(max_length=100,null=True, blank=True)
	Ward_Office_Address=models.CharField(max_length=100,null=True, blank=True)
	Ward_Contact_No=models.CharField(max_length=100,null=True, blank=True)
	Chairperson_Name=models.CharField(max_length=100,null=True, blank=True)
	Chaiperson_Contact_No=models.CharField(max_length=100,null=True, blank=True)
	Secretary_Name=models.CharField(max_length=100,null=True, blank=True)
	Secretary_Contact_No=models.CharField(max_length=100,null=True, blank=True)
	Total_Households=models.CharField(max_length=100,null=True, blank=True)
	Total_Population=models.CharField(max_length=100,null=True, blank=True)
	Total_Male_Population=models.CharField(max_length=100,null=True, blank=True)
	Total_Female_Population=models.CharField(max_length=100,null=True, blank=True)
	Website=models.CharField(max_length=100,null=True, blank=True)
	Email=models.CharField(max_length=100,null=True, blank=True)
	X_Cords=models.CharField(max_length=100,null=True, blank=True)
	Y_Cords=models.CharField(max_length=100,null=True, blank=True)
	Verification=models.CharField(max_length=100,null=True, blank=True)	
	
	
class WardFormTemp(models.Model):
	Object_id=models.CharField(max_length=100,null=False, blank=False, primary_key=True)
	munid=models.CharField(max_length=100,null=True, blank=True)
	province=models.CharField(max_length=100,null=True, blank=True)
	ward_no=models.CharField(max_length=100,null=True, blank=True)
	DISTRICT=models.CharField(max_length=100,null=True, blank=True)
	palika_name=models.CharField(max_length=100,null=True, blank=True)
	palika_type=models.CharField(max_length=100,null=True, blank=True)
	Area=models.CharField(max_length=100,null=True, blank=True)
	Ward_Office_Address=models.CharField(max_length=100,null=True, blank=True)
	Ward_Contact_No=models.CharField(max_length=100,null=True, blank=True)
	Chairperson_Name=models.CharField(max_length=100,null=True, blank=True)
	Chaiperson_Contact_No=models.CharField(max_length=100,null=True, blank=True)
	Secretary_Name=models.CharField(max_length=100,null=True, blank=True)
	Secretary_Contact_No=models.CharField(max_length=100,null=True, blank=True)
	Total_Households=models.CharField(max_length=100,null=True, blank=True)
	Total_Population=models.CharField(max_length=100,null=True, blank=True)
	Total_Male_Population=models.CharField(max_length=100,null=True, blank=True)
	Total_Female_Population=models.CharField(max_length=100,null=True, blank=True)
	Website=models.CharField(max_length=100,null=True, blank=True)
	Email=models.CharField(max_length=100,null=True, blank=True)
	X_Cords=models.CharField(max_length=100,null=True, blank=True)
	Y_Cords=models.CharField(max_length=100,null=True, blank=True)
	Verification=models.CharField(max_length=100,null=True, blank=True)	
	
	
	
	
	
	
	
	
	
	
	
	

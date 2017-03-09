from django.db import models

# Create your models here.
class Organization(models.Model):
	"""Organization is identified by orgid"""
	lastupdateddate = models.CharField(max_length=100)
	orgabbrname = models.CharField(max_length=10)
	orgid = models.IntegerField(primary_key=True)
	orgimageurl = models.CharField(max_length=150)
	orgjurisdictiontype = models.CharField(max_length=50)
	orgname = models.CharField(max_length=200)
	orgparentid = models.IntegerField()
	orgtype = models.CharField(max_length=200)
	orgurladdress = models.CharField(max_length=200)
	orgurltext = models.CharField(max_length=200)

	def __str__(self):
		return self.orgname


class Facilities(models.Model):
	"""Facilities primary key is facility id"""
	facilityadaaccess = models.CharField(max_length=1000)
	facilitydescription = models.CharField(max_length=1000)
	facilitydirections = models.CharField(max_length=100)
	facilityemail = models.CharField(max_length=150)
	facilityid = models.CharField(max_length=1000)
	facilitylatitude = models.CharField(max_length=200)
	facilitylongitude = models.CharField(max_length=200)
	facilitymapurl = models.CharField(max_length=200)
	facilityname = models.CharField(max_length=200)
	facilityphone = models.CharField(max_length=200)
	facilityreservationurl = models.CharField(max_length=200)
	facilitytypedescription = models.CharField(max_length=200)
	facilityusefeedescription = models.CharField(max_length=200)
	keywords = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	legacyfacilityid = models.CharField(max_length=200)
	orgfacilityid = models.CharField(max_length=200)
	staylimit = models.CharField(max_length=200)

	def __str__(self):
		return self.facilityname



class FacilityAddress(models.Model):
	"""FacilityAddress primary key is address id"""
	addresscountrycode = models.CharField(max_length=200)
	addressstatecode = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	facilityaddressid = models.IntegerField(primary_key=True)
	facilityaddresstype = models.CharField(max_length=200)
	facilityid = models.CharField(max_length=200)
	facilitystreetaddress1 = models.CharField(max_length=200)
	facilitystreetaddress2 = models.CharField(max_length=200)
	facilitystreetaddress3 = models.CharField(max_length=200)
	postalcode = models.CharField(max_length=200)


	def __str__(self):
		return self.city

class RecAreas(models.Model):
	"""RecAreas primary key is address id"""
	keywords = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	orgrecareaid = models.CharField(max_length=200)
	recareadescription = models.IntegerField(primary_key=True)
	recareadirections = models.CharField(max_length=200)
	recareaemail = models.CharField(max_length=200)
	recareafeedescription = models.CharField(max_length=200)
	recareaid = models.CharField(max_length=200)
	recarealatitude = models.CharField(max_length=200)
	recarealongitude = models.CharField(max_length=200)
	recareamapurl = models.CharField(max_length=200)
	recareaname = models.CharField(max_length=200)
	recareaphone = models.CharField(max_length=200)
	recareareservationurl = models.CharField(max_length=200)
	staylimit = models.CharField(max_length=200)


	def __str__(self):
		return self.recareaname




class RecreationalActivity(models.Model):
	"""RecreationalActivity primary key is activity id"""
	activityid = models.IntegerField(primary_key=True)
	activitylevel = models.CharField(max_length=200)
	activityname = models.CharField(max_length=200)
	activityparentid = models.CharField(max_length=200)

	def __str__(self):
		return self.activityname

class EntityLink(models.Model):
	"""EntityLink primary key is address id"""
	description = models.CharField(max_length=200)
	entityid = models.CharField(max_length=200)
	entitytype = models.CharField(max_length=200)
	linktype = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)



	def __str__(self):
		return self.title


class RecAreaAddress(models.Model):
	"""RecAreaAddress primary key is recareaaddressid"""
	addresscountrycode = models.CharField(max_length=200)
	addressstatecode = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	postalcode = models.CharField(max_length=200)
	recareaaddressid = models.CharField(max_length=200)
	recareaaddresstype = models.CharField(max_length=200)
	recareaid = models.CharField(max_length=200)
	recareastreetaddress1 = models.CharField(max_length=200)
	recareastreetaddress2 = models.CharField(max_length=200)
	recareastreetaddress3 = models.CharField(max_length=200)



	def __str__(self):
		return self.city

class Tour(models.Model):
	"""Tour primary key is tourid"""
	createddate = models.CharField(max_length=200)
	facilityid = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	touraccessible = models.CharField(max_length=200)
	tourdescription = models.CharField(max_length=200)
	tourduration = models.CharField(max_length=200)
	tourid = models.CharField(max_length=200)
	tourname = models.CharField(max_length=200)
	tourtype = models.CharField(max_length=200)




	def __str__(self):
		return self.tourname

class Attribute(models.Model):
	"""Attribute """
	attributeid = models.CharField(max_length=200)
	attributename = models.CharField(max_length=200)
	attributevalue = models.CharField(max_length=200)
	entityid = models.CharField(max_length=200)
	entitytype = models.CharField(max_length=200)




	def __str__(self):
		return self.attributename

class Tour(models.Model):
	"""Tour primary key is tourid"""
	createddate = models.CharField(max_length=200)
	facilityid = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	touraccessible = models.CharField(max_length=200)
	tourdescription = models.CharField(max_length=200)
	tourduration = models.CharField(max_length=200)
	tourid = models.CharField(max_length=200)
	tourname = models.CharField(max_length=200)
	tourtype = models.CharField(max_length=200)




	def __str__(self):
		return self.tourname

class PermitEntrance(models.Model):
	"""Permit Entrance primary key is permitentranceid"""
	createddate = models.CharField(max_length=200)
	district = models.CharField(max_length=200)
	facilityid = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	latitude = models.CharField(max_length=200)
	longitude = models.CharField(max_length=200)
	permitentranceaccessible = models.CharField(max_length=200)
	permitentrancedescription = models.CharField(max_length=200)
	permitentranceid = models.CharField(max_length=200)
	permitentrancename = models.CharField(max_length=200)
	permitentrancetype = models.CharField(max_length=200)
	town = models.CharField(max_length=200)




	def __str__(self):
		return self.permitentrancename

class Campsite(models.Model):
	"""campsite primary key is campstieid"""
	campsiteaccessible = models.CharField(max_length=200)
	campsiteid = models.CharField(max_length=200)
	campsitename = models.CharField(max_length=200)
	campsitetype = models.CharField(max_length=200)
	createddate = models.CharField(max_length=200)
	facilityid = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	loop = models.CharField(max_length=200)
	typeofuse = models.CharField(max_length=200)





	def __str__(self):
		return self.campsiteid
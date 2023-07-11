import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = input("Enter the phonenumber with country code and without any space")
def getParsedData(number):
    return ph.parse(number)
def getTimezone(number):
    return timezone.time_zones_for_number(number)
def getCarrierName(number):
    return carrier.name_for_number(number, "en")
def getDescription(number):
    return geocoder.description_for_number(number, "en")
number=getParsedData(number)
PhoneTimezone=getTimezone(number)
PhoneCarrier=getCarrierName(number)
PhoneDescription=getDescription(number)
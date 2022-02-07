import phonenumbers
from phonenumbers import timezone, geocoder, carrier

myNumbers = input("Enter your Mobile number with country code (+91 FOR IND) : ")

myPhone = phonenumbers.parse(myNumbers)
myTimeZone = timezone.time_zones_for_number(myPhone)
myCarrier = carrier.name_for_number(myPhone, "en")
registration = geocoder.description_for_number(myPhone, "en")

print(myPhone)
print(myTimeZone)
print(myCarrier)
print(registration)

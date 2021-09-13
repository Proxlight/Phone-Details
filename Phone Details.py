import phonenumbers
from phonenumbers import geocoder

phone_number = phonenumbers.parse("") 
print(geocoder.description_for_number(phone_number,'en'))

import phonenumbers
from phonenumbers import carrier

service_provider = phonenumbers.parse("")

print(carrier.name_for_number(service_provider,'en'))
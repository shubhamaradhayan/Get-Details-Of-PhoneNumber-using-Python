# pip install phonenumbers
# pip install folium
# pip install opencage

import folium
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number= input("Enter Your Phone Number with Country code (+__) :")

phone = phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
carrier= carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")

key = '2a14c404034b4561b8e1bfe6c485b312'

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)
query = str(reg)
res = geocoder.geocode(query)

lat = res[0]['geometry']['lat']
lng = res[0]['geometry']['lng']

Mymap = folium.Map(location=[lat, lng], zone_start = 9)

folium.Marker([lat, lng], popup=reg).add_to(Mymap)

Mymap.save("location_number.html")


print(phone)
print(time)
print(carrier)
print(reg)
# print(res)
print(lng,lat)

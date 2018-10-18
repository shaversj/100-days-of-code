import gmplot
import geocoder
import config


latitude = []
longitude = []

addresses = "6212 Africa Road Galena OH 43021, 507 West William Street Delaware OH 43015, 10250 Gorsuch Road Galena OH 43021, 7930 Thornbush Drive Westerville OH 43082, 28 Lewis Street Delaware OH 43015, 604 Buehler Drive Delaware OH 43015, 4463 Village Club Drive Powell OH 43065, 5401 Liberty Road Powell OH 43065, 309-313 Lake Street Delaware OH 43015, 13000 Hatch Road Westerville OH 43082, 5000 Dix Road Ostrander OH 43061, 7330 Deer Valley Crossing Powell OH 43065, 2243 Dixon Street Delaware OH 43015"

g = geocoder.google(addresses, key=AIzaSyC5GWMQEeJKaTyhVE-sqzq4dJqrzrqe3VQ)

for result in g:
    latitude.append(result.latlng[0])
    longitude.append(result.latlng[1])

gmap = gmplot.GoogleMapPlotter(
    latitude[0], longitude[0], 13)

gmap.apikey = config.api_key
#gmap.scatter(latitude, longitude, edge_width=10)

gmap.marker(latitude, longitude, title=titles)

gmap.draw('maps.html')

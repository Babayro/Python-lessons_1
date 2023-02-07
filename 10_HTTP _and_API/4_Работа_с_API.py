import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept':'application/json'}, params={
		'format':'geojson',
		'starttime':'2019-01-01',
		'endtime':'2019-05-01',
		'latitude':'51.51',
		'longitude':'-0.12',
		'maxradiuskm':'2000'

	})

print(response.text)
print(type(response.json()))
print(type(response.text))

data = response.json()
print(data['features'][1]['properties']['place'])






url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

start_time = input('Enter the start time')
end_time = input('Enter the end time')
latitude = input('Enter the latitude')
longitude = input('Enter the longitude')
max_radius_km = input('Enter the max radius in km')
min_magnitude = input('Enter the min magnitude')

response = requests.get(url, headers={'Accept':'application/json'}, params={
		'format':'geojson',
		'starttime':start_time,
		'endtime':end_time,
		'latitude':latitude,
		'longitude':longitude,
		'maxradiuskm':max_radius_km,
		'minmagnitude':min_magnitude

	})

data = response.json()

earthquake_list = data['features']
count = 0
for earthquake in earthquake_list:
	count += 1
	print(f"{count}. Place: {earthquake['properties']['place']}. Magnitude: {earthquake['properties']['mag']}.")

import json
import re

with open('parks-geojson.geojson', "r") as x:
    parks_geodata = json.load(x)

parkname_regex = re.compile(r'<td>([a-zA-Z_. ]+)<\/td>')

geodata = []

def dd_dms(floatie):
    n = len(str(int(floatie)))
    x = int(floatie)
    y = int(float(str(floatie)[n:])*60)
    yprime = float(str(floatie)[n:])*60 
    z = int(float(str(yprime)[2:])*60)
    final_string = str(x) + u"\N{DEGREE SIGN}" + str(y) + "'" + str(z) + '"'
    return final_string

for feature in parks_geodata['features']:
    names = parkname_regex.findall(feature['properties']['Description'])
    E = dd_dms(feature['geometry']['coordinates'][0]) + 'E'
    N = dd_dms(feature['geometry']['coordinates'][1]) + 'N'
    DMS = N + ', ' + E
    try:
        geodata.append('Park Name: ' + names[0] + ', Coordinates: {} \n'.format(DMS))
    except:
        continue

with open('geodata.txt', 'w') as y:
    y.writelines(geodata)


import googlemaps
from datetime import datetime
from core import getAppLogger
from core import Vars

logger = getAppLogger('GeoCoder')

from openpyxl import load_workbook
wb = load_workbook(filename = 'Addresses.xlsx', read_only=True)
ws = wb['Addresses']

result = []
for row in ws.rows:
    r = list()
    for cell in row:
        r.append(cell.value)
    result.append(r)

gmaps = googlemaps.Client(key='<<YOUR_API_KEY>>')

for r in result:
    a = '' if r[1] == None else unicode(r[1]).strip()
    c = '' if r[2] == None else unicode(r[2]).strip()
    s = '' if r[3] == None else unicode(r[3]).strip()
    z = '' if r[4] == None else unicode(r[4]).strip()
    addr = a + ',' + c + ',' + s + ',' + z
    lat=0.0
    lon=0.0
    geocode_result = gmaps.geocode(addr)

    lat = 0.0 if not geocode_result else geocode_result[0]["geometry"]["location"]["lat"]
    lon = 0.0 if not geocode_result else geocode_result[0]["geometry"]["location"]["lng"]
    logger.info(r[0] + Vars.SEP + addr + Vars.SEP + str(lat) + Vars.SEP + str(lon))








## Geocoding an address

#geocode_result = gmaps.geocode('C/O ABINGTON MEMORIAL HOSPITAL,ABINGTON,PA')
#lat = geocode_result[0]["geometry"]["location"]["lat"]
#lon = geocode_result[0]["geometry"]["location"]["lng"]
#print lat
#print lon
print 'end'

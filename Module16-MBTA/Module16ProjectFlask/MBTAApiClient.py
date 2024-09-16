import urllib.request, json
import mysqldb

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = dict()
            busDict['id'] = bus['id']
            busDict['longitude'] = bus['attributes']['longitude']
            busDict['latitude'] = bus['attributes']['latitude']
            busDict['label'] = bus['attributes']['label']
            busDict['current_status'] = bus['attributes']['current_status']
            busDict['occupancy_status'] = bus['attributes']['occupancy_status']
            busDict['speed'] = bus['attributes']['speed']
            busDict['updated_at'] = bus['attributes']['updated_at']
            busDict['direction'] = bus['attributes']['direction_id']
            mbtaDictList.append(busDict)
    mysqldb.insertMBTARecord(mbtaDictList)

    return mbtaDictList
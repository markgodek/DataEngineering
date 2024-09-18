import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    sql = ("insert into mbta_buses (id, longitude, latitude, direction, current_status, "
           "label, occupancy_status, speed, updated_at, current_stop_sequence) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    for mbtaDict in mbtaList:
        val = (mbtaDict['id'], mbtaDict['longitude'], mbtaDict['latitude'], mbtaDict['direction'],
               mbtaDict['current_status'], mbtaDict['label'], mbtaDict['occupancy_status'], mbtaDict['speed'],
               mbtaDict['updated_at'],mbtaDict['current_stop_sequence'])
        mycursor.execute(sql, val)

    mydb.commit()

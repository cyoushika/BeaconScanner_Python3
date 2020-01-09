import time
from beacontools import BeaconScanner, IBeaconFilter
from datetime import datetime, timedelta
import csv

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
    uuid = additional_info["uuid"]
    major = additional_info["major"]
    minor = additional_info["minor"]
    timestamp = str(datetime.now())
    with open('BeaconRecord.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow([uuid,major,minor,rssi,timestamp])


# scan for all iBeacon advertisements from beacons with the specified uuid
scanner = BeaconScanner(callback,
    device_filter=IBeaconFilter(uuid="00000000-b53c-1001-b000-001c4d5c1dd0")
)
scanner.start()

while True:
    i = 0

scanner.stop()

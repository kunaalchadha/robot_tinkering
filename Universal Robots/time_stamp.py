import time
from datetime import datetime
dateTimeObj = datetime.now()

while 1:
    time_stamp = (dateTimeObj.hour, dateTimeObj.minute,dateTimeObj.second)
    time.sleep(0.5)
    print (time_stamp)
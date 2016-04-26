# import datetime library
from datetime import datetime
now = datetime.now()
print now # 2016-04-25 18:27:59.145463
print now.year # 2016
print now.month # 4
print now.day # 25
print '%s/%s/%s' % (now.month, now.day, now.year) # 4/25/2016
print '%s:%s:%s' % (now.hour, now.minute, now.second) # 18:27:59
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second) # 4/25/2016 18:27:59

from datetime import datetime

now = datetime.now()
print now

print now.year
print now.month
print now.day

#with format
print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)
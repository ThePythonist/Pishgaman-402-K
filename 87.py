import datetime

x = str(datetime.datetime.now())
time = x.split()[1]
print(time[0:5])

# import datetime
#
# now = str(datetime.datetime.now())
# print(now.split())
# print(now.split()[0])

# ---------------------------------------

# import time
#
# s = 1
# m = 60 * s
# time.sleep(2 * m)
#
# now2 = str(datetime.datetime.now())
# print(now2.split())

# ---------------------------------------

import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().month
minute = datetime.datetime.now().minute
day = datetime.datetime.now().day
hour = datetime.datetime.now().hour
print(f"{hour}:{minute}")

# ---------------- STRFTIME EXAMPLES ----------------

# import datetime
#
# now = datetime.datetime.now()
# print(now.strftime("%B"))

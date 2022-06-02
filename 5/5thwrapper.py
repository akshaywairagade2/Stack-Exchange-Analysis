import time
start_time = time.time()
import os
os.system('cat Users.xml PostHistory.xml | python 5thmapper.py | python 5threducer.py')
print("%s seconds" % (time.time() - start_time))

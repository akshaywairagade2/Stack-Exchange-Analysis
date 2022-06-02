import time
start_time = time.time()
import os
os.system('cat Posts.xml | python 3rdAmapper.py | python 3rdAreducer.py')
print("%s seconds" % (time.time() - start_time))

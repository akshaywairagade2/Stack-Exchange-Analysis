import time
start_time = time.time()
import os
os.system('cat Comments.xml | python 4thmapper.py | python 4threducer.py')
print("%s seconds" % (time.time() - start_time))

import time
start_time = time.time()
import os
os.system('cat Posts.xml | python 3rdBmapper.py | python 3rdBreducer.py')
print("%s seconds" % (time.time() - start_time))

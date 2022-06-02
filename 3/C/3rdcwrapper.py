import time
start_time = time.time()
import os
os.system('cat Posts.xml | python 3rdcmapper.py | python 3rdcreducer.py')
print("%s seconds" % (time.time() - start_time))

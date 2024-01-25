import os
import sys

class x:
    def x(x):
        x=[]
        x.append(lambda: list(map(lambda x: x.x(x))))

os.popen(f"{sys.argv[1]} & echo {x.x(x)}").read()

####DEEPER 
#####import os
######type(os.popen("python3 \r\n import time").read())
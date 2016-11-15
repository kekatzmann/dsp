"""
kevin_katzmann
q5_datetime.py
2016.11.14
"""

# Hint:  use Google to find python function

from datetime import *

####a)
date_start = '01-02-2013'  
date_stop = '07-28-2015'

date_format = '%m-%d-%Y'

date_start_fmt = datetime.strptime(date_start, date_format)
date_stop_fmt = datetime.strptime(date_stop, date_format)

print ("Answer to (a) is: {} days".format((date_stop_fmt - date_start_fmt).days))



####b)  
date_start = '12312013'  
date_stop = '05282015'

date_format = '%m%d%Y'

date_start_fmt = datetime.strptime(date_start, date_format)
date_stop_fmt = datetime.strptime(date_stop, date_format)

print ("Answer to (b) is: {} days".format((date_stop_fmt - date_start_fmt).days))



####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_format = '%d-%b-%Y'

date_start_fmt = datetime.strptime(date_start, date_format)
date_stop_fmt = datetime.strptime(date_stop, date_format)

print ("Answer to (c) is: {} days".format((date_stop_fmt - date_start_fmt).days))




###################################
import time
import datetime

print(time.time())
print(time.ctime())
print(time.ctime())

current_time = time.ctime()
print(current_time)
#UNIX Epoch

dt = datetime.datetime.fromtimestamp(80000000)
print(dt)

###################################

from datetime import datetime #strftime, strptime

current_date = datetime.now()

formated_date= current_date.strftime('%m.%Y.%d %M:%S:%H')
print(formated_date)

###################################

from datetime import datetime


current_date = "2024-02-18 13:53"

parsed_time = datetime.strptime(current_date, '%Y-%m-%d %H:%M')

print(parsed_time)

format_parded_time = parsed_time.strftime('%Y.%d.%m')
print(format_parded_time)

###################################

from dateutil import parser
from datetime import datetime

date_string = "2024-02-13"

parse_date = parser.parse(date_string)

print(parse_date)

formated_parsed_date = parse_date.strftime('%m.%Y.%d')

print(formated_parsed_date)

###################################

from dateutil.relativedelta import relativedelta
from dateutil import parser
from datetime import datetime

date_now = datetime.now()

age_18 = date_now - relativedelta(years=18)

date_of_birth = input('Date of birth: ')
parsed_date_of_birth = parser.parse(date_of_birth)
formated_parsed_date_of_birth = parsed_date_of_birth.strftime("%d.%m.%Y")

if parsed_date_of_birth <= date_now - relativedelta(years=18):
    print('Yes, she can!')
else:
    prtint('No, she can not!')

print('This is the parsed date of birth', formated_parsed_date_of_birth)


###################################

from dateutil import tz
from datetime import datetime

usa = "America/Los_Angeles"
usa_tz = tz.gettz(usa)
print(usa_tz)

utcnow_variable = datetime.utcnow()   
print(utcnow_variable)   




















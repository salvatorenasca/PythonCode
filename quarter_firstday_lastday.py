from datetime import datetime, timedelta
import bisect
import datetime as dt

# SCENARIO
now = datetime.now() - timedelta(days=4)
currentMonth = datetime.now().month
#now = datetime.now()

# METHODS
def get_quarter_begin():
    today = dt.date.today() - timedelta(days=4)

    qbegins = [dt.date(today.year, month, 1) for month in (1,4,7,10)]

    idx = bisect.bisect(qbegins, today)
    return str(qbegins[idx-1])

# TESTING
print(get_quarter_begin())

#Another method to calculate 

current_date = datetime.now() - timedelta(days=4)
print(current_date)
current_quarter = round((current_date.month - 1) // 3 + 1)
print('current quarter: ', current_quarter)
first_date = datetime(current_date.year, 3 * current_quarter - 2, 1)
last_date = datetime(current_date.year + (3 * current_quarter)//12,(3 * current_quarter)%12+1 , 1) + timedelta(days=-1)
 
print("First Day of Quarter:", first_date)
print("Last Day of Quarter:", last_date)

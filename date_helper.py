from datetime import datetime
from datetime import timedelta
# split dates
month, day, year = [int(s) for s in "7/2/2014".split("/")]
print(month, day, year)
# testing dates
f_date = datetime(year, month, day)
l_date = datetime(2014, 7, 11)
# difference between dates
diff_date = l_date - f_date
print(diff_date)
# adding days to a date
later_date = f_date + timedelta(days=diff_date.days)
# reformat to get a date field
later_date_formatted = str(later_date.month) + "/" + str(later_date.day) + "/" + str(later_date.year)
print(later_date_formatted)

#code logic:
# extract DOB
# extract admission date
# calculate the diff
# set DOB to 1/1/1800
# add the diff to new DOB
# replace DOB and admission dates by new dates

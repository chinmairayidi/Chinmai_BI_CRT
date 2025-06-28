'''
sort a list of datas provided in DD-MM-YYYY format chronologically

input:
an integer n (1 < n < 100)
a list of n strings in DD-MM-YYYY format

output:
sorted list of dates(earlier to latest)

example:
input:
['12-05-2-23', '14-05-2023', '13-05-2023']
output:
['12-05-2-23', '13-05-2023', '14-05-2023']
'''

def sort_dates(dates):
    def date_key(date):
        day, month, year = map(int, date.split('-'))
        return (year, month, day)
    return sorted(dates, key=date_key)
sort = sort_dates(['12-09-2023', '14-05-2023', '13-05-2023','30-06-2002'])
print(sort)
getattr = getattr
print(getattr)
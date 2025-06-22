from datetime import datetime, timedelta
s = input()
given_date = datetime(int(s[0:4]), int(s[5:7]), int(s[8:]))
days_to_add = int(input())
future_date = given_date+timedelta(days = days_to_add)
print(future_date.strftime('%Y-%m-%d'))
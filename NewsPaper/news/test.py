from datetime import datetime, timedelta
x = datetime.now()
y = x - timedelta(days=7)
print(x-y)
print(type(x-y))

today = datetime.now()
last_week = today - timedelta(days=7)
print(last_week)
print(type(last_week))
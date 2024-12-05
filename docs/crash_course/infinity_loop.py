# To infinity, and beyond
from datetime import datetime

start_time = datetime.now()
counter = 1

while True:
    print (counter)
    # print("To infinity, and beyond. /Buz")
    counter += 1
    if counter > 1_000_000:
        end_time = datetime.now()
        break
# An actual timespan! In Python! 🐍
time_span = end_time - start_time

print(time_span)
from datetime import datetime

danas = datetime.now()

print (danas)
print (danas.year)
print (danas.month)
print (danas.day)
print (danas.hour)
print (danas.minute)
print (danas.second)


print(datetime.now().strftime("Dan u nedelji: %A %w\n \
                                Dan: %d\n \
                                Mesec: %B\%m\n"))

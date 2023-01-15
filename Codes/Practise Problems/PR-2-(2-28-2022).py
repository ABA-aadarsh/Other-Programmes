#Convert seconds into equivalent seconds, minutes and hours
#Example: Given if given 60, returns 0 hours 1 minutes 0 seconds
seconds=int(input("Enter in seconds: "))
minutes=int((seconds-seconds%60)/60)
seconds%=60
hours=int((minutes-minutes%60)/60)
minutes%=60
print(f":{hours} hours {minutes} minutes {seconds} seconds")
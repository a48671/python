seconds = int(input('Input time (seconds)'))

seconds_in_hour = 3600
seconds_in_minutes = 60

hours = seconds // seconds_in_hour
if hours < 10:
    hours = '0' + str(hours)

minutes = seconds % seconds_in_hour // seconds_in_minutes

seconds = seconds % seconds_in_hour % seconds_in_minutes

print(f'{hours}:{minutes}:{seconds}')
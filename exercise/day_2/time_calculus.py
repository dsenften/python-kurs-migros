hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

if seconds == 59:
    seconds = 0
    if minutes == 59:
        minutes = 0
        if hours == 23:
            hours = 0
        else:
            hours += 1
    else:
        minutes += 1
else:
    seconds += 1

print(f"Time (old format: {'%02d' % hours}:{'%02d' % minutes}:{'%02d' % seconds}")

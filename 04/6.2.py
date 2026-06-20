total_seconds = int(input("введіть число:"))

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

days, remainder = divmod(total_seconds, SECONDS_IN_DAY)
hours, remainder = divmod(remainder, SECONDS_IN_HOUR)
minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")
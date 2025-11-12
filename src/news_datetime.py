from datetime import datetime

# The Moscow Times — Wednesday, October 2, 2002
moscow_times_date = "Wednesday, October 2, 2002"
moscow_times_format = "%A, %B %d, %Y"
dt1 = datetime.strptime(moscow_times_date, moscow_times_format)
print(f"The Moscow Times: {dt1}")

# The Guardian — Friday, 11.10.13
guardian_date = "Friday, 11.10.13"
guardian_format = "%A, %d.%m.%y"
dt2 = datetime.strptime(guardian_date, guardian_format)
print(f"The Guardian: {dt2}")

# Daily News — Thursday, 18 August 1977
daily_news_date = "Thursday, 18 August 1977"
daily_news_format = "%A, %d %B %Y"
dt3 = datetime.strptime(daily_news_date, daily_news_format)
print(f"Daily News: {dt3}")
import datetime as dt
from random import choice
import smtplib

FROM_EMAIL = ""
PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
TO_EMAILS = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("./data/quotes.txt") as file:
        quotes = file.readlines()
        random_quote = choice(quotes)
    
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAILS,
            msg=f"Subject:Be positive!\n\n{random_quote}"
        )

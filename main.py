from datetime import datetime
from random import randint
import pandas
import smtplib

FROM_EMAIL = ""
PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"

today = (datetime.now().month, datetime.now().day)
file_exist = True

try:
    original_data = pandas.read_csv("./data/birthday.csv")
except FileNotFoundError:
    file_exist = False

    default = {
        'name': pandas.Series('Miguel Lopez'),
        'email': pandas.Series(FROM_EMAIL),
        'month': pandas.Series(today[0]),
        'day': pandas.Series(today[1])
    }

    msg_default = "Please, check the csv file at 'Birthday-wisher project'."

    data = pandas.DataFrame(default)
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
else:
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in original_data.iterrows()}

if today in birthdays_dict:
    template_path = f"./letter_templates/letter_{randint(1, 3)}.txt"
    with open(template_path) as template_file:
        letter = template_file.read()
        letter = letter.replace("[NAME]", birthdays_dict[today]["name"])

    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=birthdays_dict[today]["email"],
            msg=f"Subject:Congratulations!\n\n{letter}" if file_exist else f"Subject:Error!\n\n{msg_default}"
        )

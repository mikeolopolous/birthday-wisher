import smtplib

my_email = ""
my_password = ""
server = "smtp.gmail.com"

# connection = smtplib.SMTP(server)
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="miguel.lopez@woodward.mx",
#     msg="Subject:Hello\n\nBody of the email :D"
# )
# connection.close()

with smtplib.SMTP(server) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="miguel.lopez@woodward.mx",
        msg="Subject:Hello\n\nBody of the email :D"
    )

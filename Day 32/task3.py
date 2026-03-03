#Task 3 is a Monday Motivation Email sender using smtplib combined with datetime

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

my_email = "example_email@email.com"  # add your email
password = "your_app_password"  # add your app password

if weekday == 1: #monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Monday Motivation!\n\n{quote}")

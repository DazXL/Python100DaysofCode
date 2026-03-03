#task1 is about smtplib

import smtplib

my_email = "example_email@email.com"  # add your email
password = "your_app_password"  # add your app password

with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # using gmail smtp
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email, to_addrs="your_destiny_email@email.com",
                        msg="hello")  # add your destiny mail

# import smtplib
import datetime as dt
import random


# Uncomment the sections required for the program to work and modify the my_email and password sections to reflect
# the email and password of account related. Furthermore, change the SMTP relay to the matching SMTP relay.

# my_email='whocares@example.com'
# password='thisissupposedtobeyourpassword'


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as all_quotes:
        quotes = all_quotes.readlines()
        quote = random.choice(quotes)


    print(quote)
    # with smtplib.SMTP('stmp.gmail.com') as connection:
        # connection.starttls()
        # connection.login(user=my_email, password=password)
        # connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f'Subject: Motivation \n\n{quote}')
        # connection.close()
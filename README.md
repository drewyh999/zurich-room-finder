# zurich-room-finder
Web spider that search and send message for you to rent a room from online renting platform like wgzimmer

# Stuck, for cannot bypass the god damn Google recaptcha when you submit the message form

# Restarted the development with some concessions due to the restriction of Google recaptcha

> Now the function of the spider is limited to notify you when there could be new ads on the wgzimmer website

# Getting started:

## Requirements(used at development):

- yagmail / 0.14.256
- Beautiful Soup / 4.9.3
- requests / 2.25.1
- keyring / 23.0.1
- python / 3.8

## 1.Register your sender email account:

> The spider use email to notify you when there are new room ads on the website, to do this, you must have an extra email for the spider to send the notification(Sorry I didn't use any email sending api), and register this sender email account to the yagmail library.

> Before doing this, make sure you have turned on the SMTP service of the sender email

Open a python interpreter and run:

```python
import yagmail
yagmail.register('sender_email_username', 'sender_email_password')

```
Which stores your specified sender email username and password to your keyring, which will not be acquired by others

## 2.Fill in the notification receiving email and host as well as the sender email:

Use any editor and open the config.py, fill in the sender email address and receiver email. The host and port number of sender email could be obtain through your email service provider.(For example, the SMTP host name and port of MS Outlook is smtp.office365.com and port number is 587)

```python
SENDER_EMAIL_ACCOUNT = {
   "account":"sender_email_username",
   "host":"sender_email_host",
   "port":"sender_port_number"
}
RECEIVER_EMAIL = "your_receiver_email"
```

## 3.Run the main.py and get notifications:)
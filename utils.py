from config import VERBOSE_MODE
import yagmail
from config import SENDER_EMAIL_ACCOUNT
from config import RECEIVER_EMAIL

def print_info(*args, **kwargs):
    if not VERBOSE_MODE:
        return
    print(*args, **kwargs)

def notify_through_email(title:str,msg:str):
    yagmail.SMTP(SENDER_EMAIL_ACCOUNT["account"],host=SENDER_EMAIL_ACCOUNT["host"],port=SENDER_EMAIL_ACCOUNT["port"]).send(RECEIVER_EMAIL,title,msg)
    print("Sending email to " + RECEIVER_EMAIL)
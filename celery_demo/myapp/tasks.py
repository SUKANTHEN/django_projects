from celery import shared_task
import time

@shared_task
def send_email_task(email_address:str):
    print(f"Sending email to {email_address}....")
    time.sleep(5)
    print(f"Email sent to {email_address}!")
    return f"Email sent to {email_address}!"
from celery import shared_task
from utils.sms import sms


@shared_task
def send_sms_code_task(phone_number, code):
    sms.send(receiver=phone_number, message=code)
    return code

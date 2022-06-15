from kavenegar import *
from A.local_settings import KAVE_SENDER, KAVE_API_KEY


class Sms:
    """
        Note:
            You must set your API_KEY and SENDER number. Go to kavenegar and create an account,
             then you can use the trial version.
            we use this in tasks.
    """
    API_KEY = KAVE_API_KEY
    SENDER = KAVE_SENDER

    def send(self, receiver, message):
        try:
            api = KavenegarAPI(self.API_KEY)
            params = {
                "sender": self.SENDER,
                "receptor": receiver,
                "message": message
            }
            api.sms_send(params)
            return message
        except APIException as e:
            return e
        except HTTPException as e:
            return e


sms = Sms()

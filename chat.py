from datetime import datetime

class Msg:
    message=""
    time=""
    sent_by_me=""
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

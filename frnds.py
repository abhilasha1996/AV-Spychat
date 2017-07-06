class NewSpy:
    name=""
    salutation=""
    age=0
    rating=0.0
    is_online=False
    chats=[]
    current_status=None
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

f1=NewSpy("Shikha","Ms.",20,5.0)
f2=NewSpy("paras","Ms.",21,4.8)

friends=[f1,f2]
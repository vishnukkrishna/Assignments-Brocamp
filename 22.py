class Account:
    def __init__(self,name,account_no):
        self.name = name
        self.account_no = account_no
        
    def get_name(self):
        return self.name,self.account_no

    def set_name(self,name,account_no):
        self.name = name
        self.account_no = account_no

obj = Account(11,11)
obj.set_name("Vishnu",12345678)
print(obj.get_name())
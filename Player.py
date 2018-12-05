class Player:
    
    def __init__(self, name):
        self.__name = name
        self.__balance = 100
        
    def getName(self):
        return self.__name
    
    def getBalance(self):
        return self.__balance
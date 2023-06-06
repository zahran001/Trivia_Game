#This program contains three related modules.

class Questions:
    def __init__(self,q,a1,a2,a3,a4,ca): #initializer method
        self.__TriviaQuesiton = q
        self.__Answer1 = a1
        self.__Answer2 = a2
        self.__Answer3 = a3
        self.__Answer4 = a4
        self.__NumberForCorrectAnswer = ca

    #accessor methods - get data

    def getTriviaQuestion(self):
        return self.__TriviaQuesiton
    def getAnswer1(self):
        return self.__Answer1
    def getAnswer2(self):
        return self.__Answer2
    def getAnswer3(self):
        return self.__Answer3
    def getAnswer4(self):
        return self.__Answer4
    def getNumberForCorrectAnswer(self):
        return self.__NumberForCorrectAnswer

    #mutator methods - update data

    def setTriviaQuestion(self,q):
        self.__TriviaQuesiton = q
    def setAnswer1(self,a1):
        self.__Answer1 = a1

    def setAnswer2(self,a2):
        self.__Answer2 = a2
    def setAnswer3(self,a3):
        self.__Answer3 = a3

    def setAnswer4(self,a4):
        self.__Answer4 = a4

    def setNumberForCorrectAnswer(self,no_ca):
        self.__NumberForCorrectAnswer = no_ca

    def __str__(self):
        return f"{self.__TriviaQuesiton}\n{'1.'+self.__Answer1}\n{'2.'+self.__Answer2}\n{'3.'+self.__Answer3}\n{'4.'+self.__Answer4}"
    

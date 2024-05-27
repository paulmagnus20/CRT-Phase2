class Student:
    def __init__(self,Name,rollno,ecamarks,stldmarks,aicamarks):
        self.name= Name
        self.rollno= rollno
        self.ecamarks= ecamarks
        self.stldmarks= stldmarks
        self.aicamarks= aicamarks
    def printAllDetails(self):
        print(self.name)
        print(self.rollno)
        print(self.ecamarks)
        print(self.aicamarks)
        print(self.stldmarks)
        
obj = Student("Paul","W1",78,88,99)
obj.printAllDetails()


# print(obj.name)
# print(obj.rollno)
# print(obj.ecamarks)
# print(obj.stldmarks)
# print(obj.aicamarks)
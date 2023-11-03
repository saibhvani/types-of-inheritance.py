#Multi-level/Hierarchal Inheritance
class Address:
    __Address:str=""
    def addAddress (self,address):
        self.__address=address
    def getAddress(self):
            return self.__address
class Employee (Address):
            __firstName:str=""
            __lastName:str=""
            __surName:str=""
            def setName (self,fName:str,lName:str,sName:str=""):
                self.__firstName=fName
                self.__surName=sName
                self.__lastName=lName
            def __nameFormat (self):
                return f'{self.__firstName} {self.__lastName} {self.__surName}'
            def getFullName(self):
                return self.__nameFormat()
class permanentEmployee(Employee):
    __sal:int = 30000
    def salcal(self):
        return 12*self.__sal
class contractEmployee(Employee):
    __hr_pay:int =1000
    def salcal(self, hr:int, hrs=12):
        return f'salcal for {hrs} hrs.(self.__hr_pay*hrs)'

emp=permanentEmployee()
emp.setName(fName="sravya",sName="m",lName="motamarri")
emp.addAddress("hyderabad")
print(emp.getFullName())
print(emp.getAddress())
print(emp.salcal())

emp=permanentEmployee()
emp.setName(fName="sravya",sName="m",lName="motamarri")
emp.addAddress("hyderabad")
print(emp.getFullName())
print(emp.getAddress())
print(emp.salcal())

#Multiple inheritance
class ClassB:
    def printData(self):
        print("suma")
class ClassC:
    def printData(self):
        print("sravani")
class ClassA(ClassB,ClassC):
    pass
a=ClassA()
a.printData()

#Hybrid Inheritance
class ClassA:
    def printData(self):
        print("bhavani")
class ClassB(ClassA):
    def printData(self):
        print("sravya")
class ClassC(ClassA):
    def printData(self):
        print("chinni")
class ClassD(ClassB,ClassC):
    pass
a=ClassD()
a.printData()


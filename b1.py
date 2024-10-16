class SoHoc:
    #thuộc tính
    __number1=0
    __number2=0
    #phương thức
    def inputInfo(self):
        self.__number1=int(input("Nhập số thứ nhất: "))
        self.__number2=int(input("Nhập số thứ hai: "))
    def printInfo(self):
        return self.__number1,self.__number2
    def addition(self):
        tong=int(self.__number1+self.__number2)
        print("Tổng của 2 số là ",tong)
    def subtract(self):
        hieu=int(self.__number1-self.__number2)
        print("Hiệu của 2 số là ",hieu)
    def multi(self):
        tich=int(self.__number1*self.__number2)
        print("Tích của 2 số là ",tich)
    def division(self):
        thuong=int(self.__number1/self.__number2)
        print("Thương của 2 số là ",thuong)

so=SoHoc()

so.inputInfo()
print('Hai số vừa nhập là: ',so.printInfo())
so.addition()
so.subtract()
so.multi()
so.division()

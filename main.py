#khuôn mẫu
class cat:
    #thuộc tính
    name="Alex"
    age= 3
    female= True
    color="Brown"
    #phương thức
    def inputInfor(self):
        self.name=input("Nhập tên: ")
        self.age=input("Nhập tuổi: ")
        self.color=input("Nhập màu sắc của lông: ")
    def outputInfor(self):
        print("Tên: ",self.name)
        print("Tuổi: ",self.age)
        print("Màu sắc của lông: ",self.color)

    def setname(self,_name):
        self.name = _name
    def getname(self):
        return self.name
    def setage(self,_age):
        self.name = _age
    def getage(self):
        return self.age
    def setcolor(self,_color):
        self.color = _color
    def getname(self):
        return self.color

#tạo đối tượng
cat1=cat()
cat2=cat()

cat1.inputInfor()
cat1.outputInfor()
# print("="*10)
# print("Con mèo 2",cat2.name)
# print("Con mèo 2",cat2.age)
# print("Con mèo 2",cat2.color)
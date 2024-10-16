class NhanVien:
    #thuộc tính
    __ma_nhan_vien=""
    ten=""
    tuoi=""
    dia_chi=""
    luong=""
    gio_lam=""
    #phương thức
    def inputInfo(self):
        self.__ma_nhan_vien=int(input("Nhập mã nhân viên: "))
        self.ten=str(input("Nhập tên nhân viên: "))
        self. tuoi=int(input("Nhập tuổi nhân viên: "))
        self.dia_chi=input("Nhập địa chỉ: ")
        self.luong=int(input("Nhập lương nhân viên: "))
        self.gio_lam=float(input("Nhập số giờ làm: "))
    def printInfo(self):
        return self.__ma_nhan_vien,self.ten,self.tuoi,self.dia_chi,self.gio_lam
    def tinhThuong(self):
        if self.gio_lam >=200:
            tong=(self.luong*20/100)+self.luong
            return tong
        if self.gio_lam <200 and self.gio_lam>=100:
            tong=(self.luong*10/100)+self.luong
            return tong
        if self.gio_lam <100:
            tong=0+self.luong
            return tong

nv=NhanVien()
nv.inputInfo()
nv.printInfo()
print("Thông tin nhân viên vừa nhập là: ",nv.printInfo())
nv.tinhThuong()
print("Số tiền lương của nhân viên là: ", nv.tinhThuong())




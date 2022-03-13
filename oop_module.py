# Encapsulation
class Kamera(object):
    
    kategori_kamera = ""
    def __init__(self, input_kategori, input_merk, input_tipe, input_warna):
        self.kategori = input_kategori
        self.merk = input_merk
        self.tipe = input_tipe
        self.warna = input_warna
        Kamera.nama_kamera = input_kategori

    def potret(self):
        print("Ini adalah", self.kategori,'\n')

    def info(self):
        print(f"kategori: {self.kategori} \nmerk\t: {self.merk} \ntipe\t: {self.tipe} \nwarna\t: {self.warna}")
        
        
# Inheritence        
class Benda(object):
    def __init__(self, kategori, merk, tipe, warna, harga, warranty):
        self.kategori = kategori
        self.merk = merk
        self.tipe = tipe
        self.warna = warna

    def ulasan(self, kalimat):
        for x in range(kalimat):
            print("bangus banget loh")      
            
    def info(self):
         print(f"kategori: {self.kategori} \nmerk\t: {self.merk} \ntipe\t: {self.tipe} \nwarna\t: {self.warna}")
            
            
class Printer(Benda):
    def __init__(self, kategori, merk, tipe, warna, harga, warranty):
        super().__init__(kategori, merk, tipe, warna, harga, warranty)
        self.harga = harga
        self.warranty = warranty

    def cetak(self):
        super().ulasan(2)
        print("wow...murah banget...")

    def info_printer(self):
        super().info()
        print(f"harga\t: {self.harga}, \nwarranty: {self.warranty}")

        
# Abstraction
from abc import abstractmethod, ABC
class Tumbuhan(ABC):
    
    @abstractmethod
    def profil(self, input_nama_latin, asal, iklim):
        pass
    def manfaat(self, input_manfaat):
        pass
    def spesies(self, input_spesies):
        pass
    def info(self):
        pass
    
    
# Polymorphism
class Benda(object):
    def __init__(self, kategori, merk, tipe, warna):
        self.kategori = kategori
        self.merk = merk
        self.tipe = tipe
        self.warna = warna

    def ulasan(self, kalimat):
        for x in range(kalimat):
            print("bangus banget loh")

    def info(self):
      print(f"kategori: {self.kategori} \nmerk\t: {self.merk} \ntipe\t: {self.tipe} \nwarna\t: {self.warna}")
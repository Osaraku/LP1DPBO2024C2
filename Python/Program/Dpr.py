# Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 1
# dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
# seperti yang telah dispesifikasikan. Aamiin

class Dpr:
    __noId = ""
    __name = ""
    __bidang = ""
    __partai = ""

    def __init__(self, noId = "", name = "", bidang = "", partai = ""):
        self.__noId = noId
        self.__name = name
        self.__bidang = bidang
        self.__partai = partai

    def get_noId(self):
        return self.__noId

    def set_noId(self, noId):
        self.__noId = noId

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bidang(self):
        return self.__bidang
    
    def set_bidang(self, bidang):
        self.__bidang = bidang

    def get_partai(self):
        return self.__partai
    
    def set_partai(self, partai):
        self.__partai = partai

# Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 1
# dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
# seperti yang telah dispesifikasikan. Aamiin

from Dpr import Dpr

listDPR = []
masukan = 0

print("+--------------------------+")
print("| Welcome to DPR Database! |")
print("+--------------------------+")

while (masukan != 5):
    print("Pilih angka untuk memasukkan perintah : ")
    print("1. Tambah anggota DPR")
    print("2. Ubah anggota DPR")
    print("3. Hapus anggota DPR")
    print("4. Tampilkan list anggota DPR")
    print("5. Keluar dari aplikasi")

    masukan = int(input("Angka yang dipilih : "))
    
    if (masukan == 1):
        n = int(input("Masukan banyaknya anggota yang ditambah : "))

        for i in range (n):
            print("Penambahan ke-" + str(i+1) + " : ")
            noId = str(input("Id : "))
            name = str(input("Nama : "))
            bidang = str(input("Bidang : "))
            partai = str(input("Partai : "))

            listDPR.append(Dpr(noId, name, bidang, partai))
            print("Anggota telah ditambahkan!")

    elif(masukan == 2):
        noId = str(input("Masukan id anggota yang akan diubah : "))
        
        ketemu = 0
        i = 0
        while(ketemu == 0 and i < len(listDPR)):
            if(noId == listDPR[i].get_noId()):
                print("Masukan perubahan data!")
                noId = str(input("Id : "))
                name = str(input("Nama : "))
                bidang = str(input("Bidang : "))
                partai = str(input("Partai : "))
                listDPR[i].set_noId(noId)
                listDPR[i].set_name(name)
                listDPR[i].set_bidang(bidang)
                listDPR[i].set_partai(partai)
                
                print("Data anggota telah berhasil diubah!")
                ketemu == 1
            i += 1

        if ketemu == 0:
            print("Tidak ada anggota DPR dengan Id tersebut!")
    
    elif(masukan == 3):
        noId = str(input("Masukan id anggota yang akan dihapus : "))
        
        ketemu = 0
        i = 0
        while(ketemu == 0 and i < len(listDPR)):
            if(noId == listDPR[i].get_noId()):
                del listDPR[i]
                print("Data anggota telah berhasil hapus!")
                ketemu == 1
            i += 1

        if ketemu == 0:
            print("Tidak ada anggota DPR dengan Id tersebut!")

    elif(masukan == 4):
        print("List Anggota DPR : ")
        colLength_1 = 2
        colLength_2 = 4
        colLength_3 = 6
        colLength_4 = 6

        for dpr in listDPR:
            if(len(dpr.get_noId()) > colLength_1):
                colLength_1 = len(dpr.get_noId())

            if(len(dpr.get_name()) > colLength_2):
                colLength_2 = len(dpr.get_name())

            if(len(dpr.get_bidang()) > colLength_3):
                colLength_3 = len(dpr.get_bidang())

            if(len(dpr.get_partai()) > colLength_4):
                colLength_4 = len(dpr.get_partai())

        print("+", end="")
        for i in range(colLength_1 + 2):
            print("-", end="")
        print("+", end="")
        for i in range(colLength_2 + 2):
            print("-", end="")
        print("+", end="")
        for i in range(colLength_3 + 2):
            print("-", end="")
        print("+", end="")
        for i in range(colLength_4 + 2):
            print("-", end="")
        print("+")

        print("| " + "Id ", end="")
        for i in range(colLength_1 - 2):
            print(" ", end="")
        print("| " + "Nama ", end="")
        for i in range(colLength_2 - 4):
            print(" ", end="")
        print("| " + "Bidang ", end="")
        for i in range(colLength_3 - 6):
            print(" ", end="")
        print("| " + "Partai ", end="")
        for i in range(colLength_4 - 6):
            print(" ", end="")
        print("|")

        print("+", end="")
        for i in range(colLength_1 + 2):
            print("-", end="")
        print("+", end="")
        for i in range(colLength_2 + 2):
            print("-", end="")
        print("+", end="")
        for i in range(colLength_3 + 2):
            print("-", end="")
        print("+", end="")
        for i in range(colLength_4 + 2):
            print("-", end="")
        print("+")

        for dpr in listDPR:
            print("| " + dpr.get_noId(), end=" ")
            if len(dpr.get_noId()) < colLength_1:
                for i in range(colLength_1 - len(dpr.get_noId())):
                    print(" ", end="")
            print("| " + dpr.get_name(), end=" ")
            if len(dpr.get_name()) < colLength_2:
                for i in range(colLength_2 - len(dpr.get_name())):
                    print(" ", end="")
            print("| " + dpr.get_bidang(), end=" ")
            if len(dpr.get_bidang()) < colLength_3:
                for i in range(colLength_3 - len(dpr.get_bidang())):
                    print(" ", end="")
            print("| " + dpr.get_partai(), end=" ")
            if len(dpr.get_partai()) < colLength_4:
                for i in range(colLength_4 - len(dpr.get_partai())):
                    print(" ", end="")
            print("|")
            
            print("+", end="")
            for i in range(colLength_1 + 2):
                print("-", end="")
            print("+", end="")
            for i in range(colLength_2 + 2):
                print("-", end="")
            print("+", end="")
            for i in range(colLength_3 + 2):
                print("-", end="")
            print("+", end="")
            for i in range(colLength_4 + 2):
                print("-", end="")
            print("+")
    
    elif(masukan == 5):
        print("+--------------------+")
        print("| See you next time! |")
        print("+--------------------+")

    else:
        print("Inputan yang anda masukkan salah!")
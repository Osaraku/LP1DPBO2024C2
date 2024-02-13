# Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 1
# dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
# seperti yang telah dispesifikasikan. Aamiin

# Import kelas
from Dpr import Dpr

# Inisisasi
listDPR = []
masukan = 0

# Tampilan awal
print("+--------------------------+")
print("| Welcome to DPR Database! |")
print("+--------------------------+")

# Menampilkan menu selama blum keluar
while (masukan != 5):
    print("\nPilih angka untuk memasukkan perintah : ")
    print("1. Tambah anggota DPR")
    print("2. Ubah anggota DPR")
    print("3. Hapus anggota DPR")
    print("4. Tampilkan list anggota DPR")
    print("5. Keluar dari aplikasi")

    # pilih menu
    masukan = int(input("Angka yang dipilih : "))
    
    if (masukan == 1): #jika pilih tambah data
        n = int(input("\nMasukan banyaknya anggota yang ditambah : ")) # minta banyak data yang akan ditambah

        # menambah data
        for i in range (n):
            print("\nPenambahan ke-" + str(i+1) + " : ")
            noId = str(input("Id : "))
            name = str(input("Nama : "))
            bidang = str(input("Bidang : "))
            partai = str(input("Partai : "))

            listDPR.append(Dpr(noId, name, bidang, partai))
        # notf berhasil
        print("\nAnggota telah ditambahkan!")

    elif(masukan == 2): # jika pilih ubah data
        noId = str(input("\nMasukan id anggota yang akan diubah : ")) # pilih id yang akan diubah
        
        # cari id yang diubah
        ketemu = 0
        i = 0
        while(ketemu == 0 and i < len(listDPR)):
            if(noId == listDPR[i].get_noId()):
                # ubah data
                print("\nMasukan perubahan data!")
                noId = str(input("Id : "))
                name = str(input("Nama : "))
                bidang = str(input("Bidang : "))
                partai = str(input("Partai : "))
                listDPR[i].set_noId(noId)
                listDPR[i].set_name(name)
                listDPR[i].set_bidang(bidang)
                listDPR[i].set_partai(partai)
                
                # notif berhasil
                print("\nData anggota telah berhasil diubah!")
                ketemu == 1
            i += 1

        # notif tidak ketemu datanya
        if (ketemu == 0):
            print("\nTidak ada anggota DPR dengan Id tersebut!")
    
    elif(masukan == 3): # jika pilih ubah data
        noId = str(input("\nMasukan id anggota yang akan dihapus : ")) # pilih id yang akan dihapus
        
        # caari id yang akan dihapus
        ketemu = 0
        i = 0
        while(ketemu == 0 and i < len(listDPR)):
            # hapus data
            if(noId == listDPR[i].get_noId()):
                del listDPR[i]
                print("\nData anggota telah berhasil hapus!")
                ketemu == 1
            i += 1

        if ketemu == 0:
            print("\nTidak ada anggota DPR dengan Id tersebut!")

    elif(masukan == 4): # jika memilih menampilkan data
        print("\nList Anggota DPR : ")
        
        # panjang kolom
        colLength_1 = 2
        colLength_2 = 4
        colLength_3 = 6
        colLength_4 = 6

        # mencari kolom terpanjang
        for dpr in listDPR:
            if(len(dpr.get_noId()) > colLength_1):
                colLength_1 = len(dpr.get_noId())

            if(len(dpr.get_name()) > colLength_2):
                colLength_2 = len(dpr.get_name())

            if(len(dpr.get_bidang()) > colLength_3):
                colLength_3 = len(dpr.get_bidang())

            if(len(dpr.get_partai()) > colLength_4):
                colLength_4 = len(dpr.get_partai())

        # Membuat header tabel
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

        # Menampilkan isi tabel
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
    
    elif(masukan == 5): # Jika memilih keluar dari program
        print("+--------------------+")
        print("| See you next time! |")
        print("+--------------------+")

    else: # jika inputan salah
        print("Inputan yang anda masukkan salah!")
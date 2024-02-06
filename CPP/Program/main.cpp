/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 1
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/

// Deklarasi Library
#include <bits/stdc++.h>
#include "Dpr.cpp"

using namespace std;

int main()
{
    // Deklarasi Variabel
    int i, ketemu, n = 0;
    string tunjuk;
    string id;
    string name;
    string bidang;
    string partai;

    list<Dpr> llist;

    int input = 0;

    // Tampilan awal
    cout << "+--------------------------+" << '\n';
    cout << "| Welcome to DPR Database! |" << '\n';
    cout << "+--------------------------+" << '\n';

    // Program akan terus berulang selama user blm meilih akan keluar
    while (input != 5)
    {
        // Tampilan menu
        cout << "\n";
        cout << "Pilih angka untuk memasukkan perintah : " << '\n';
        cout << "1. Tambah anggota DPR" << '\n';
        cout << "2. Ubah anggota DPR" << '\n';
        cout << "3. Hapus anggota DPR" << '\n';
        cout << "4. Tampilkan list anggota DPR" << '\n';
        cout << "5. Keluar dari aplikasi" << '\n';
        cout << "\nAngka yang dipilih : ";

        // Input untuk memilih perintah
        cin >> input;

        // Cek pilihan
        if (input == 1) // Menambahkan data
        {
            // Input jumlah data yang ditambah
            cout << "\nBerapa banyak anggota yang ditambahkan : ";
            cin >> n;
            cout << "\nTambah data dengan format \"Id Nama Bidang Partai\" sebanyak " << n << " kali : " << '\n';

            // Menambah data sebanyak yang telah ditentukan
            for (i = 0; i < n; i++)
            {
                Dpr temp;

                // Input data
                cin >> id >> name >> bidang >> partai;

                temp.set_id(id);
                temp.set_name(name);
                temp.set_bidang(bidang);
                temp.set_partai(partai);

                llist.push_back(temp);
            }
            cout << "Data telah ditambahkan" << '\n';
        }
        else if (input == 2) // Mengubah data
        {
            // Input untuk pilih data mana yang diubah
            cout << "\nMasukkan Id anggota DPR yang akan diubah : " << '\n';
            cin >> tunjuk;

            ketemu = 0; // Variabel untuk cek ada  atau tidak
            list<Dpr>::iterator it = llist.begin();
            while (it != llist.end() && ketemu == 0) // Pengulangan selama blm sampai akhir dan blm ketemu
            {
                // Cek apakah iterasi saat ini ini merupakan yang dipilih
                string skrg = it->get_id();
                if (skrg.compare(tunjuk) == 0)
                {
                    // Ubah data iterasi saat ini
                    cout << "\nUbah data dengan format \" Id Nama Bidang Partai\"" << '\n';
                    cin >> id >> name >> bidang >> partai;

                    it->set_id(id);
                    it->set_name(name);
                    it->set_bidang(bidang);
                    it->set_partai(partai);

                    ketemu = 1;
                    cout << "Data telah diubah" << '\n';
                }
                it++;
            }
            // Jika datanya tidak ketemu
            if (ketemu == 0)
            {
                cout << "Tidak ada anggota DPR dengan Id tersebut!" << '\n';
            }
        }
        else if (input == 3) // Menghapus data
        {
            // Input untuk pilih data mana yang dihapus
            cout << "\nMasukkan Id anggota DPR yang akan dihapus : " << '\n';
            cin >> tunjuk;

            ketemu = 0; // Variabel untuk cek ada  atau tidak
            list<Dpr>::iterator it = llist.begin();
            while (it != llist.end() && ketemu == 0) // Pengulangan selama blm sampai akhir dan blm ketemu
            {
                // Cek apakah iterasi saat ini ini merupakan yang dipilih
                string skrg = it->get_id();
                if (skrg.compare(tunjuk) == 0)
                {
                    // Hapus data iterasi saat ini
                    llist.erase(it);
                    ketemu = 1;
                    cout << "Data telah dihapus" << '\n';
                }
                it++;
            }
            // Jika datanya tidak ketemu
            if (ketemu == 0)
            {
                cout << "Tidak ada anggota DPR dengan Id tersebut!" << '\n';
            }
        }
        else if (input == 4) // Tampilkan Data
        {
            // Menapilkan sluruh data anggota DPR
            cout << "\nDaftar Anggota DPR : " << '\n';
            i = 0;
            for (list<Dpr>::iterator it = llist.begin(); it != llist.end(); it++) // Pengulangan sebanyak jumlah data anggota DPR
            {
                cout << "Id : " << it->get_id() << "\nNama : " << it->get_name() << "\nBidang : " << it->get_bidang() << "\nPartai : " << it->get_partai() << "\n\n";
                i++;
            }
        }
        else if (input == 5) // Keluar dari aplikasi
        {
            // Menampilkan ucapan selamat tinggal
            cout << '\n';
            cout << "+--------------------+" << '\n';
            cout << "| See you next time! |" << '\n';
            cout << "+--------------------+" << '\n';
        }
        else // Jika Input perintah salah
        {
            cout << "\nInputan yang anda masukkan salah!" << '\n';
        }
    }

    return 0;
};
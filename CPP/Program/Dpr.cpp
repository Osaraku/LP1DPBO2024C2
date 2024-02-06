/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 1
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/

// Deklarasi Library
#include <iostream>
#include <string>

using namespace std;

// Kelas DPR untuk representasi data anggota DPR
class Dpr
{
    // Atribut
private:
    string id;
    string name;
    string bidang;
    string partai;

public:
    // Constructor
    Dpr()
    {
        this->id = "";
        this->name = "";
        this->bidang = "";
        this->partai = "";
    }

    Dpr(string id, string name, string bidang, string partai)
    {
        this->id = id;
        this->name = name;
        this->bidang = bidang;
        this->partai = partai;
    }

    // Method
    string get_id()
    {
        return this->id;
    }

    void set_id(string id)
    {
        this->id = id;
    }

    string get_name()
    {
        return this->name;
    }

    void set_name(string name)
    {
        this->name = name;
    }

    string get_bidang()
    {
        return this->bidang;
    }

    void set_bidang(string bidang)
    {
        this->bidang = bidang;
    }

    string get_partai()
    {
        return this->partai;
    }

    void set_partai(string partai)
    {
        this->partai = partai;
    }

    // Destructor
    ~Dpr()
    {
    }
};

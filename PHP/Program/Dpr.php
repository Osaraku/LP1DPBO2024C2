<?php
/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 1
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/

// Kelas DPR
class Dpr
{
    // Atribut
    private $id = '';
    private $name = '';
    private $bidang = '';
    private $partai = '';
    private $foto = '';

    // Constructor
    public function __construct($id = '', $name = '', $bidang = '', $partai = '', $foto = '')
    {
        $this->id = $id;
        $this->name = $name;
        $this->bidang = $bidang;
        $this->partai = $partai;
        $this->foto = $foto;
    }

    // Method set dan get
    public function setId($id)
    {
        $this->id = $id;
    }
    public function getId()
    {
        return $this->id;
    }
    public function setName($name)
    {
        $this->name = $name;
    }
    public function getName()
    {
        return $this->name;
    }
    public function setBidang($bidang)
    {
        $this->bidang = $bidang;
    }
    public function getBidang()
    {
        return $this->bidang;
    }
    public function setPartai($partai)
    {
        $this->partai = $partai;
    }
    public function getPartai()
    {
        return $this->partai;
    }
    public function setFoto($foto)
    {
        $this->foto = $foto;
    }
    public function getFoto()
    {
        return $this->foto;
    }

    // Destructor
    public function __destruct()
    {
    }
}

?>
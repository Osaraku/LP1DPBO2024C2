<?php
/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 1
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/

// Memanggil class
require('Dpr.php');

// Menambahkan data
$dpr1 = new Dpr("21", "Dicky Harun", "Kesehatan", "Nasdem", "<img src='../Foto/1.jpeg' width='40' height='70'>");
$dpr2 = new Dpr("32", "Ir. Iswara", "Pertahanan", "Golkar", "<img src='../Foto/2.jpeg' width='40' height='70'>");
$dpr3 = new Dpr("43", "Biben Fikriana", "Pertanian", "Gerindra", "<img src='../Foto/3.png' width='40' height='70'>");
$dpr4 = new Dpr("54", "Teni Kartini", "Perikanan", "Golkar", "<img src='../Foto/4.jpeg' width='40' height='70'>");

$listDpr = array($dpr1, $dpr2, $dpr3, $dpr4);


?>

<!-- Membuat file html untuk menampilkan tabel -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latihan Praktikum</title>

    <!-- style pada tabel -->
    <style>
        table,
        th,
        td {
            border: 1px solid black;
            border-collapse: collapse;
            padding: 5px;
        }
    </style>
</head>

<body>
    <!-- Menampilkan tabel -->
    <h3>List Anggota DPR : </h3>
    <table class="table" bored>
        <thead>
            <tr>
                <th>Id</th>
                <th>Nama</th>
                <th>Bidang</th>
                <th>Partai</th>
                <th>Foto</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $index = 1;
            foreach ($listDpr as $dpr) {
                ?>
                <tr>
                    <td>
                        <?php echo $dpr->getId(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getName(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getBidang(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getPartai(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getFoto(); ?>
                    </td>
                </tr>
                <?php
                $index++;
            }
            ?>
        </tbody>
    </table>

    <?php
    // Mengubah salah satu data
    $ubahId = "54";
    $ketemu = 0;

    foreach ($listDpr as $dpr) {
        //  Ubah data sesuai kebutuhan
        if ($dpr->getId() == $ubahId) {
            $dpr->setBidang("Kebudayaan");
            $dpr->setPartai("PDIP");
            $ketemu = 1;

            // Notif berhasil
            echo "<br>";
            echo "Data anggota dengan Id <i> (" . $dpr->getId() . ") </i> telah diubah!";
            echo "<br>";
        }
    }
    // Notif tidak ketemu
    if ($ketemu == 0) {
        echo "<br>";
        echo "Tidak ada anggota DPR dengan Id <i> (" . $ubahId . ") </i>";
        echo "<br>";
    }
    ?>

    <!-- menampilkan tabel -->
    <h3>List Anggota DPR : </h3>
    <table class="table" bored>
        <thead>
            <tr>
                <th>Id</th>
                <th>Nama</th>
                <th>Bidang</th>
                <th>Partai</th>
                <th>Foto</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $index = 1;
            foreach ($listDpr as $dpr) {
                ?>
                <tr>
                    <td>
                        <?php echo $dpr->getId(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getName(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getBidang(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getPartai(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getFoto(); ?>
                    </td>
                </tr>
                <?php
                $index++;
            }
            ?>
        </tbody>
    </table>

    <?php
    // Manghapus salah satu data
    $hapusId = "43";
    $ketemu = 0;
    $i = 0;
    $tempId = null;

    // Mencari data yang akan dihapus
    while ($i < count($listDpr) && $ketemu == 0) {
        if ($listDpr[$i]->getId() == $hapusId) {
            $tempId = $listDpr[$i]->getId();
            unset($listDpr[$i]);
            $ketemu = 1;

            // Notif berhasil
            echo "<br>";
            echo "Data anggota dengan Id <i> (" . $tempId . ") </i> telah dihapus!";
            echo "<br>";
        }
        $i++;
    }
    /// Notif gagal
    if ($ketemu == 0) {
        echo "<br>";
        echo "Tidak ada anggota DPR dengan Id <i> (" . $tempId . ") </i>";
        echo "<br>";
    }
    ?>

    <!-- menampilkan tabel -->
    <h3>List Anggota DPR : </h3>
    <table class="table" bored>
        <thead>
            <tr>
                <th>Id</th>
                <th>Nama</th>
                <th>Bidang</th>
                <th>Partai</th>
                <th>Foto</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $index = 1;
            foreach ($listDpr as $dpr) {
                ?>
                <tr>
                    <td>
                        <?php echo $dpr->getId(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getName(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getBidang(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getPartai(); ?>
                    </td>
                    <td>
                        <?php echo $dpr->getFoto(); ?>
                    </td>
                </tr>
                <?php
                $index++;
            }
            ?>
        </tbody>
    </table>
</body>

</html>
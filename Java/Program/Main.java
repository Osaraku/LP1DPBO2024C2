/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 1
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        int i, j, n, input, ketemu;
        String id, name, bidang, partai;

        ArrayList<Dpr> listDPR = new ArrayList<>();

        Scanner sc = new Scanner(System.in);

        System.out.println("+--------------------------+");
        System.out.println("| Welcome to DPR Database! |");
        System.out.println("+--------------------------+");

        input = 0;
        while (input != 5) {
            System.out.println();
            System.out.println("Pilih angka untuk memasukkan perintah : ");
            System.out.println("1. Tambah anggota DPR");
            System.out.println("2. Ubah anggota DPR");
            System.out.println("3. Hapus anggota DPR");
            System.out.println("4. Tampilkan list anggota DPR");
            System.out.println("5. Keluar dari aplikasi");
            System.out.println("Angka yang dipilih : ");
            input = sc.nextInt();

            if (input == 1) {
                System.out.println("Berapa banyak anggota yang ditambahkan :");
                n = sc.nextInt();

                for (i = 0; i < n; i++) {
                    System.out.println();
                    System.out.println("Penambahan ke-" + Integer.toString(i + 1));
                    System.out.print("Id : ");
                    id = sc.next();
                    System.out.print("Nama : ");
                    name = sc.next();
                    System.out.print("Bidang : ");
                    bidang = sc.next();
                    System.out.print("Partai : ");
                    partai = sc.next();

                    Dpr temp = new Dpr();
                    temp.setId(id);
                    temp.setName(name);
                    temp.setBidang(bidang);
                    temp.setPartai(partai);
                    listDPR.add(temp);
                }
                System.out.println("Data telah ditambahkan");
            }

            else if (input == 2) {
                System.out.println("Masukkan Id anggota DPR yang akan diubah : ");
                id = sc.next();

                ketemu = 0;
                i = 0;
                while (ketemu == 0 && i < listDPR.size()) {
                    if (id.equals(listDPR.get(i).getId())) {
                        System.out.println();
                        System.out.println("Masukan perubahan data!");
                        System.out.print("Id : ");
                        id = sc.next();
                        System.out.print("Nama : ");
                        name = sc.next();
                        System.out.print("Bidang : ");
                        bidang = sc.next();
                        System.out.print("Partai : ");
                        partai = sc.next();

                        listDPR.get(i).setId(id);
                        listDPR.get(i).setName(name);
                        listDPR.get(i).setBidang(bidang);
                        listDPR.get(i).setPartai(partai);

                        System.out.println("Data telah diubah!");
                        System.out.println();
                        ketemu = 1;
                    }
                    i++;
                }
                if (ketemu == 0) {
                    System.out.println("Tidak ada anggota DPR dengan Id tersebut!");
                    System.out.println();
                }
            }

            else if (input == 3) {
                System.out.println("Masukkan Id anggota DPR yang akan dihapus : ");
                id = sc.next();

                ketemu = 0;
                i = 0;
                while (ketemu == 0 && i < listDPR.size()) {
                    if (id.equals(listDPR.get(i).getId())) {
                        listDPR.remove(i);

                        System.out.println("Data telah dihapus!");
                        System.out.println();
                        ketemu = 1;
                    }
                    i++;
                }
                if (ketemu == 0) {
                    System.out.println("Tidak ada anggota DPR dengan Id tersebut!");
                    System.out.println();
                }
            }

            else if (input == 4) {
                System.out.println();
                System.out.println("List Anggota DPR :");
                int colLength_1 = 2;
                int colLength_2 = 4;
                int colLength_3 = 6;
                int colLength_4 = 6;

                for (i = 0; i < listDPR.size(); i++) {
                    if (listDPR.get(i).getId().length() > colLength_1) {
                        colLength_1 = listDPR.get(i).getId().length();
                    }
                    if (listDPR.get(i).getName().length() > colLength_2) {
                        colLength_2 = listDPR.get(i).getName().length();
                    }
                    if (listDPR.get(i).getBidang().length() > colLength_3) {
                        colLength_3 = listDPR.get(i).getBidang().length();
                    }
                    if (listDPR.get(i).getPartai().length() > colLength_4) {
                        colLength_4 = listDPR.get(i).getPartai().length();
                    }
                }

                System.out.print("+");
                for (i = 0; i < colLength_1 + 2; i++) {
                    System.out.print("-");
                }
                System.out.print("+");
                for (i = 0; i < colLength_2 + 2; i++) {
                    System.out.print("-");
                }
                System.out.print("+");
                for (i = 0; i < colLength_3 + 2; i++) {
                    System.out.print("-");
                }
                System.out.print("+");
                for (i = 0; i < colLength_4 + 2; i++) {
                    System.out.print("-");
                }
                System.out.println("+");

                System.out.print("| Id ");
                for (i = 0; i < colLength_1 - 2; i++) {
                    System.out.print(" ");
                }
                System.out.print("| Nama ");
                for (i = 0; i < colLength_2 - 4; i++) {
                    System.out.print(" ");
                }
                System.out.print("| Bidang ");
                for (i = 0; i < colLength_3 - 6; i++) {
                    System.out.print(" ");
                }
                System.out.print("| Partai ");
                for (i = 0; i < colLength_4 - 6; i++) {
                    System.out.print(" ");
                }
                System.out.println("|");

                System.out.print("+");
                for (i = 0; i < colLength_1 + 2; i++) {
                    System.out.print("-");
                }
                System.out.print("+");
                for (i = 0; i < colLength_2 + 2; i++) {
                    System.out.print("-");
                }
                System.out.print("+");
                for (i = 0; i < colLength_3 + 2; i++) {
                    System.out.print("-");
                }
                System.out.print("+");
                for (i = 0; i < colLength_4 + 2; i++) {
                    System.out.print("-");
                }
                System.out.println("+");

                for (i = 0; i < listDPR.size(); i++) {
                    System.out.print("| " + listDPR.get(i).getId() + " ");
                    for (j = 0; j < colLength_1 - listDPR.get(i).getId().length(); j++) {
                        System.out.print(" ");
                    }
                    System.out.print("| " + listDPR.get(i).getName() + " ");
                    for (j = 0; j < colLength_2 - listDPR.get(i).getName().length(); j++) {
                        System.out.print(" ");
                    }
                    System.out.print("| " + listDPR.get(i).getBidang() + " ");
                    for (j = 0; j < colLength_3 - listDPR.get(i).getBidang().length(); j++) {
                        System.out.print(" ");
                    }
                    System.out.print("| " + listDPR.get(i).getPartai() + " ");
                    for (j = 0; j < colLength_4 - listDPR.get(i).getPartai().length(); j++) {
                        System.out.print(" ");
                    }
                    System.out.println("|");

                    System.out.print("+");
                    for (j = 0; j < colLength_1 + 2; j++) {
                        System.out.print("-");
                    }
                    System.out.print("+");
                    for (j = 0; j < colLength_2 + 2; j++) {
                        System.out.print("-");
                    }
                    System.out.print("+");
                    for (j = 0; j < colLength_3 + 2; j++) {
                        System.out.print("-");
                    }
                    System.out.print("+");
                    for (j = 0; j < colLength_4 + 2; j++) {
                        System.out.print("-");
                    }
                    System.out.println("+");
                }
            }

            else if (input == 5) {
                System.out.println("+--------------------+");
                System.out.println("| See you next time! |");
                System.out.println("+--------------------+");
            }

            else {
                System.out.println("Inputan yang anda masukkan salah!");
            }
        }

        sc.close();
    }
}

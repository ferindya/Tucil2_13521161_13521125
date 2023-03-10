# Closest Pair of Points in 3D
Disusun untuk memenuhi Tugas Kecil 2 IF2211 Strategi Algoritma "Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer"

## Daftar Isi
* [Deskripsi Singkat Program](#deskripsi-singkat-program)
* [Struktur Program](#struktur-program)
* [Requirement Program](#requirement-program)
* [Cara Kompilasi Program](#cara-kompilasi-program)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Author](#author)

## Deskripsi Singkat Program
Permasalahan yang diangkat pada tugas kecil ini adalah memvisualisasikan semua titik dalam bidang 3D, sepasang titik yang jaraknya terdekat ditunjukkan dengan warna berbeda dari titik lainnya.
*Closest Pair of Points* merupakan pasangan titik yang terdekat atau pasangan titik yang mempunyai jarak minimal di antara pasangan titik yang lain pada bidang dengan ruang dimensi tertentu. Dengan kata lain, jika terdapat n buah titik pada bidang dengan dimensi tertentu, maka closest pair of points merupakan pasangan titik dengan jarak terdekat satu sama lain dibandingkan dengan pasangan titik lainnya.

### Visualisasi Algoritma *Quickhull*:
https://www.researchgate.net/profile/Brian-Higgins/post/How-to-calculate-closest-pair-of-points-in-3D-data-sets/attachment/59d61e82c49f478072e974e2/AS%3A271742377889792%401441799840030/image/NearestNeighbors.jpg

## Struktur Program
```bash
.
│   README.md
├───test
|   |___n = 1000.png
|   |___n = 128.png
|   |___n = 16 (1).png
|   |___n = 16 (2).png
|   |___n = 64.png
|   |___visualisasi n = 1000.png
|   |___visualisasi n = 128.png
|   |___visualisasi n = 16 (1).png
|   |___visualisasi n = 16 (2).png
|   |___visualisasi n = 64.png
│                                      
├───src
│   │___main.py
│           
└───doc
       Tucil2_13521125_13521161.pdf
```

## Requirement Program
* Python versi 3.8.5 atau lebih baru. Pastikan pula terdapat package PyPi (PIP) pada Python Anda.

## Cara Menjalankan Program
1. Buka Command Prompt (CMD) pada komputer Anda.
2. Pilih ke directory tempat file berada.
3. Setelah masuk ke directory, ketik "python main.py".
4. Program akan meminta masukan jumlah titik yang berada di bidang 3D.
5. Pengguna memasukkan input jumlah titik yang berada di bidang 3D.
6. Program akan menampilkan output pasangan titik dengan jarak terpendek, jarak terpendek, banyak perhitungan Euclidean Distance, waktu eksekusi, dan visualisasi titik dalam bidang 3D.
7. Visualisasi dengan indikator warna merah menandakan pasangan titik dengan jarak terpendek.


## Author
* Asyifa Nurul Shafira (13521125)
* Ferindya Aulia Berlianty (13521161)

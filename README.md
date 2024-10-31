# Program Klasifikasi Segitiga

Program ini digunakan untuk mengklasifikasikan jenis segitiga berdasarkan panjang tiga sisi yang dimasukkan oleh pengguna. Berdasarkan input panjang sisi, program akan menentukan apakah segitiga tersebut adalah segitiga sama sisi, sama kaki, siku-siku, atau sembarang. Jika tidak memenuhi syarat untuk membentuk segitiga, program akan memberikan peringatan.

## Cara Kerja Program

1. **Input Panjang Sisi**  
   Program meminta pengguna untuk memasukkan tiga panjang sisi segitiga (`a`, `b`, dan `c`).

2. **Pengecekan Kondisi Segitiga Valid**
   - Jika salah satu panjang sisi bernilai nol atau negatif, program akan mencetak:
     ```
     Tidak Ada Segitiga Dapat Dibangun
     ```
   - Jika panjang salah satu sisi lebih besar atau sama dengan jumlah dua sisi lainnya, program akan mencetak:
     ```
     Tidak Ada Segitiga Dapat Dibangun
     ```

3. **Klasifikasi Jenis Segitiga**
   Berdasarkan panjang sisi yang diberikan, program akan mengklasifikasikan segitiga sebagai berikut:
   
   - **Segitiga Sama Kaki**: Jika dua sisi memiliki panjang yang sama, dan sisi ketiga berbeda. Output yang dicetak:
     ```
     Segitiga SAMA KAKI
     ```
   - **Segitiga Sama Sisi**: Jika ketiga sisi memiliki panjang yang sama. Output yang dicetak:
     ```
     Segitiga SAMA SISI
     ```
   - **Segitiga Siku-Siku**: Berdasarkan rumus Pythagoras, jika kuadrat dari satu sisi sama dengan jumlah kuadrat dari dua sisi lainnya, maka segitiga adalah siku-siku. Output yang dicetak:
     ```
     Segitiga SIKU-SIKU
     ```
   - **Segitiga Bebas**: Jika segitiga tidak termasuk dalam kategori di atas. Output yang dicetak:
     ```
     Segitiga BEBAS
     ```

## Catatan

Pada kode saat ini, pengecekan untuk segitiga siku-siku belum sepenuhnya akurat karena menggunakan logika sederhana (`a * a or b * b or c * c`). Untuk mengecek segitiga siku-siku dengan benar, Anda perlu menggunakan rumus Pythagoras: salah satu dari tiga kondisi berikut harus benar:
   - `a^2 + b^2 = c^2`
   - `a^2 + c^2 = b^2`
   - `b^2 + c^2 = a^2`

## Cara Menjalankan Program

1. Pastikan Anda memiliki Python terinstal di sistem Anda.
2. Jalankan program dengan perintah berikut:
   ```bash
   python segitiga.py

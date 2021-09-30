# KEC
Repository untuk tugas mata kuliah Kecerdasan Buatan (AI)


![node tree](https://github.com/suwidhi/KEC/blob/main/DFS-BFS.png?raw=true)


Algoritma DFS:
Pertama node akan ditambahkan ke list visited jika belum pernah dikunjungi sebelumnya. Kemudian dari semua leaf node tersebut akan dicek kembali jika sudah ada di visited atau belum. Jika belum maka akan ditambahkan kedalam list visited. Kemudian dicek kembali apakah leaf dari node tersebut ada pada graf, jika ada maka node tersebut akan direkursif dengan fungsi yang sama sampai selesai.

Algoritma BFS:
Sama seperti DFS, pertama jika node belum ada di list visited maka tambahkan kedalam list visited. Kemudian buat list queue untuk menampung antrian dari node berikutnya yang akan direkursif. Kemudian cek apakah node tersebut ada dalam entry yang ada pada dictionary graf yang sudah di tentukan sebelumnya. Jika ada maka cek tiap leaf apakah sudah ada pada list visited, jika belum maka tambahkan. Setelah itu tinggal rekursif fungsi tersebut pada list queue sampai selesai.

Output Program:
DFS: ['1', '4', '2', '3', '9', '10', '5', '6', '7', '8']
BFS: ['1', '4', '2', '3', '5', '7', '8', '9', '10', '6']

DFS:
  1. Root node adalah 1
  2. Kemudian ke node 4
  3. Karena node 4 tidak memiliki leaf maka lanjut ke leaf dari node 1 yang belum dikunjungi yaitu 2
  4. Dari node 2 masuk ke 3 dan berheti saat 9 karena 9 tidak memiliki leaf lagi
  5. Balik ke node parent dari 9 yaitu 3, kemudian visit node berikutnya yaitu 10
  6. Naik lagi sampai kembali ke node 2 kemudian turun ke node yang belum dikunjungi yaitu 5
  7. Turun ke node 6, kemudian ke 7, terakhir ke 8.
  
  
BFS:
  1. Pertama root node yaitu 1
  2. Pada baris ke-2 ada node 4 dan 2
  3. Pada baris ke-3 ada 3, 5, 7, 8
  4. Pada baris ke-4 ada 9, 10, dan 6
  

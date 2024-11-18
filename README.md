# Aplikasi Sistem Informasi Desa

Aplikasi sistem informasi desa berbasis web dibuat menggunakan Python dan Streamlit. Aplikasi ini memungkinkan pengguna untuk menambah, menghapus, memperbarui, dan mengelompokkan data penduduk dari setiap dusun di desa.

## Pengoperasian Data Kependudukan

Terdapat data penduduk Dusun Dunggala, data penduduk Dusun Tontayuo Daa, dan data penduduk Dusun Tontayuo Kiki. Sebelum melakukan pengoperasian data kependudukan, terlebih dahulu dapat dipilih data penduduk dusun yang dituju.

Terdapat beberapa menu pengoperasian yang disediakan pada aplikasi.

### Menu Tambah Data

Menu Tambah Data digunakan untuk menghapus data penduduk. Berikut tahapan untuk menghapus data:
1. Pilih “Tambah Data” dari menu.
2. Isi informasi yang diperlukan untuk setiap kolom.
3. Klik “Tambah Data” untuk menyimpan data baru.

Data yang baru ditambahkan tersimpan pada baris terakhir pada dataset kependudukan dusun yang dituju.

### Menu Hapus Data

Menu Hapus Data digunakan untuk menambahkan data penduduk baru. Berikut tahapan untuk menambahkan data:
1. Pilih “Hapus Data” dari menu.
2. Isi indeks baris yang akan dihapus.
3. Klik “Hapus Data” untuk menghapus data.

### Menu Perbarui Data

Menu Perbarui Data digunakan untuk memperbarui data penduduk. Berikut tahapan untuk memperbarui data:
1. Pilih “Perbarui Data” dari menu.
2. Isi indeks baris yang akan diperbarui.
3. Pilih kolom yang akan diperbarui.
4. Isi informasi nilai baru untuk kolom yang akan diperbarui.
5. Klik “Perbarui Data” untuk memperbarui data.

### Menu Pengelompokan Data

Menu Pengelompokan Data digunakan untuk mengelompokkan data penduduk berdasarkan kolom tertentu. Berikut tahapan untuk mengelompokkan data:
1. Pilih “Pengelompokan Data” dari menu.
2. Pilih pengelompokan yang akan dioperasikan.
3. Isi informasi yang diperlukan untuk mengelompokkan data.

   a. Pengelompokan data berdasarkan nomor kartu keluarga

      Masukkan nomor kartu keluarga yang akan dikelompokkan, kemudian klik “Hasil Pengelompokan” untuk memperoleh data penduduk yang memiliki nomor kartu keluarga yang sama. Selain itu, ditampilkan jumlah penduduk dalam pengelompokan.

   b. Pengelompokan data berdasarkan umur

      Masukkan umur awal dan umur akhir yang akan dikelompokkan, kemudian klik “Hasil Pengelompokan” untuk memperoleh data penduduk dengan pengelompokan berdasarkan umur. Selain itu, ditampilkan jumlah penduduk dalam pengelompokan.

   c. Pengelompokan data berdasarkan pekerjaan

      Masukkan pekerjaan penduduk yang akan dikelompokkan, kemudian klik “Hasil Pengelompokan” untuk memperoleh data penduduk yang memiliki pekerjaan tersebut. Selain itu, ditampilkan jumlah penduduk dalam pengelompokan.

   d. Pengelompokan data berdasarkan jenis kelamin

      Masukkan jenis kelamin penduduk yang akan dikelompokkan, kemudian klik “Hasil Pengelompokan” untuk memperoleh data penduduk yang memiliki jenis kelamin tersebut. Selain itu, ditampilkan jumlah penduduk dalam pengelompokan.

### Menu Pengunduhan Data

Data penduduk tiap dusun dapat diunduh dengan mengeklik “Download” di bawah tabel data kependudukan.

Setelah mengeklik “Download”, maka data akan tersimpan dengan format nama file “updated_file.csv”.

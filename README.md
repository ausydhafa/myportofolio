Nama : Ausy Dhafa Adhitama

NPM : 2406417954

Kelas : PBP D

### Tugas 2

1. Pertama, urls.py pada direktori portofolio/urls.py menerima request dan meneruskannya ke main.urls karena terdapat konfigurasi include("main.urls"). Selanjutnya, main/urls.py mencocokkan URL, misalnya /education/, dengan view show_education. View kemudian mengambil data Education dari model menggunakan Django ORM, misalnya Education.objects.all(). Data tersebut dimasukkan ke dalam context dan dikirim ke template education.html. Di dalam template, data pada context ditampilkan menggunakan template loop\. Django kemudian merender template menjadi HTML dan mengirimkan hasilnya kembali kepada pengguna sehingga dapat ditampilkan pada browser.
2. Karena model memungkinkan data disimpan dan dikelola secara terstruktur di database. Ketika ingin menambah, menghapus, atau mengubah pendidikan, kita tidak perlu mengubah kode HTML satu per satu, membuat aplikasi lebih mudah dipelihara dan dikembangkan.
3. makemigrations digunakan untuk membuat file migration berdasarkan perubahan yang dilakukan pada model. Django akan membuat file migration baru yang berisi instruksi untuk menambahkan field description ke database. Sedangkan, migrate digunakan untuk menerapkan migration tersebut ke database.
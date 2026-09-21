Nama : Ausy Dhafa Adhitama

NPM : 2406417954

Kelas : PBP D

### Tugas 2

1. Pertama, urls.py pada direktori portofolio/urls.py menerima request dan meneruskannya ke main.urls karena terdapat konfigurasi include("main.urls"). Selanjutnya, main/urls.py mencocokkan URL, misalnya /education/, dengan view show_education. View kemudian mengambil data Education dari model menggunakan Django ORM, misalnya Education.objects.all(). Data tersebut dimasukkan ke dalam context dan dikirim ke template education.html. Di dalam template, data pada context ditampilkan menggunakan template loop\. Django kemudian merender template menjadi HTML dan mengirimkan hasilnya kembali kepada pengguna sehingga dapat ditampilkan pada browser.

2. Karena model memungkinkan data disimpan dan dikelola secara terstruktur di database. Ketika ingin menambah, menghapus, atau mengubah pendidikan, kita tidak perlu mengubah kode HTML satu per satu, membuat aplikasi lebih mudah dipelihara dan dikembangkan.

3. makemigrations digunakan untuk membuat file migration berdasarkan perubahan yang dilakukan pada model. Django akan membuat file migration baru yang berisi instruksi untuk menambahkan field description ke database. Sedangkan, migrate digunakan untuk menerapkan migration tersebut ke database.

#### AI Disclosure
Dalam pengerjaan tugas ini, saya menggunakan ChatGPT sebagai alat bantu untuk membantu menjelaskan ulang konsep makemigrations dan migrate guna menjawab refleksi dan membantu melakukan pengecekan dan debugging ketika terdapat kesalahan atau error.

### Tugas 3
1. ModelForm digunakan karena dapat membuat form berdasarkan model Django sehingga proses pembuatan field, validasi data, dan penyimpanan ke database menjadi lebih mudah dibandingkan membuat form HTML secara manual. Sementara itu, {% csrf_token %} digunakan untuk melindungi form dari serangan Cross-Site Request Forgery (CSRF) dengan memastikan bahwa permintaan yang dikirim memiliki token keamanan yang sesuai.

2. JSON lebih disukai dalam pengembangan aplikasi web modern karena memiliki struktur yang sederhana, mudah dibaca, dan mudah diproses oleh berbagai bahasa pemrograman, khususnya JavaScript. JSON juga memiliki format yang ringkas sehingga sesuai untuk pertukaran data antara frontend dan backend melalui API.

3. Ketika view mengambil data pendidikan dari database, data tersebut masih berbentuk objek model Django. Serialization diperlukan untuk mengubah objek tersebut menjadi format JSON yang dapat dikirim melalui HTTP response dan diproses oleh aplikasi lain. Pada project ini, data JSON kemudian di-deserialize kembali menjadi objek Python agar dapat ditampilkan pada halaman Education.

#### AI Disclosure
Dalam pengerjaan tugas ini, saya tidak menggunakan Generative AI sama sekali.
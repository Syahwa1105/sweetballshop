Nama: Qoriana Syahwa Maharani. <br>
NPM: 2406437533. <br>
Kelas: PBP-B.

-**Nama Project : Sweetball Shop**<br>
-**Link PWS : https://qoriana-syahwa-sweetballshop.pbp.cs.ui.ac.id/**


## **Tugas 2 PBP - Implementasi Model-View-Template (MVT) pada Django**  
**1.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Membuat proyek baru  
pertama saya membuat folder proyek sweetballshop lalu mengaktifkan virtual environment. Setelah itu saya install Django dan membuat proyek baru dengan nama yang sama.
- Membuat aplikasi main
setelah proyek jadi, saya membuat app baru bernama main yang nantinya akan digunakan sebagai inti aplikasi.
- Mendaftarkan app ke settings
saya mendaftarkan di sweetballshop/settings.py, lalu saya menambahkan main ke bagian INSTALLED_APPS supaya Django tahu ada aplikasi baru.
- Membuat model Product 
di main/models.py, saya mendefinisikan model Product dengan field name, price, description, thumbnail, category, dan is_featured sesuai instruksi soal.
- Migrasi database 
saya menjalankan perintah makemigrations dan migrate untuk membuat dan menerapkan perubahan struktur tabel ke database.
- Membuat view
di main/views.py saya menambahkan fungsi show_main yang mengembalikan template main.html dengan context berisi identitas (npm, nama, kelas).
- Membuat routing
saya membuat file urls.py di app main dan menambahkan path ke fungsi show_main. Lalu saya hubungkan main/urls.py ke sweetballshop/urls.py.
- Membuat template
saya membuat file main.html di folder main/templates/ untuk menampilkan identitas saya dan nama aplikasi SweetBall Shop.
- Menjalankan server
setelah semua dibuat, saya jalankan python manage.py runserver untuk mengecek apakah halaman bisa diakses di browser.
- Membuat unit test
saya menambahkan file tests.py untuk memastikan URL utama bisa diakses, template yang digunakan benar, dan identitas saya muncul di halaman.
- Push ke GitHub dan deploy ke PWS
Terakhir, proyek ini saya upload ke repository GitHub lalu saya deploy ke PWS supaya bisa diakses secara online.

2. <img width="1024" height="768" alt="Neutral Flowchart" src="https://github.com/user-attachments/assets/d048b68f-7596-4ad3-af62-325b443478d8" />

**3. Jelaskan peran settings.py dalam proyek Django!** 
peran settings.py yaitu  berisi semua konfigurasi utama project Django. Contohnya seperti:
- daftar aplikasi yang aktif (INSTALLED_APPS)
- konfigurasi database
- middleware
- static files  
- mode debug dan allowed hosts.  
Tanpa settings.py ini, Django tidak akan tahu bagaimana cara menjalankan proyek.

**4. Bagaimana cara kerja migrasi database di Django?**
Proses migrasi di Django bekerja dalam dua tahap, yaitu
- makemigrations : Django akan membaca perubahan di model, lalu membuat file migrasi berisi instruksi SQL.  
- migrate : file migrasi tersebut dieksekusi ke database sehingga tabel di database selalu sesuai dengan model Python yang dibuat.

**5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Menurut saya Django dipilih untuk dijadikan pembelajaran Utama, karena:
- sudah menerapkan arsitektur MVT (mirip MVC) yang umum dipakai di banyak framework
- memiliki banyak fitur bawaan (batteries included) jadi mahasiswa bisa langsung fokus ke konsep
- djanggo memiliki dokumentasi yang jelas dan komunitasnya besar
- djanggo sudh digunakan di industri nyata sehingga ilmu yang dipelajari relevan
- django berbasis Python yang relatif mudah dipelajari.

**6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**
menurut saya penjelasan asdos di tutorial 1 sudah sangat membantu untuk menyelesaikan tugas individu 2 ini dan penjelasan yang diberikan juga sangat jelas untuk dipahami dan sangat membantu di tugas individu 2 ini.

## **TUGAS 3 PBP** 
Nama: Qoriana Syahwa Maharani
NPM: 2406437533
Kelas: PBP-B 

**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery itu penting karena aplikasi web sering membutuhkan untuk bertukar data, bukan hanya menampilkan halaman HTML. Misalnya pada aplikasi frontend (React, Flutter, dsb) perlu ambil data dari backend dalam format tertentu (JSON atau XML). Dengan adanya data delivery, sistem bisa saling komunikasi dengan rapi, konsisten, dan mudah dipakai ulang oleh aplikasi lain.

**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Kalau dibandingkan, JSON biasanya lebih praktis dan lebih sering dipakai. JSON lebih ringan, gampang dibaca oleh manusia, dan langsung cocok dipakai di JavaScript atau bahasa pemrograman lainnya. XML sebenarnya lebih tua atau lebih lama dan masih berguna di beberapa sistem besar, tapi lebih verbose (kebanyakan tag). Jadi, itu sebabnya kalau sekarang JSON lebih populer karena lebih sederhana dan efisien.

**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**

is_valid() dipakai untuk mengecek apakah data yang dimasukkan ke form sesuai dengan aturan field di model. Misalnya kolom harga harus integer, link harus URL valid, dan field wajib harus diisi. Kalau is_valid() bernilai True, berarti data aman disimpan ke database. Kalau tidak, form akan menampilkan pesan error. Tanpa is_valid(), data bisa masuk ke database meski salah format dan bikin masalah ke depannya.

**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

csrf_token adalah token keamanan yang mencegah serangan CSRF (Cross Site Request Forgery). Dengan token ini, Django bisa memastikan form yang dikirim benar-benar dari website kita, bukan dari website lain yang mencoba menyusup ke website kita. Kalau kita tidak pakai csrf_token, penyerang bisa bikin form palsu di situs lain yang mengirim request ke aplikasi kita seolah-olah dari user, dan ini bisa dipakai untuk aksi berbahaya (misalnya hapus data, ganti password, dsb).

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. Membuat file forms.py dan menambahkan ProductForm untuk input produk baru.

2. Menambahkan beberapa fungsi view di views.py:
- add_product → menambah produk baru lewat form.
- product_detail → menampilkan detail dari produk tertentu.
- products_json, products_xml, product_json_by_id, product_xml_by_id → untuk data delivery (JSON dan XML).

3. Mengatur routing di urls.py untuk menghubungkan setiap view dengan URL.

4. Membuat template main.html untuk menampilkan identitas dan daftar produk sekaligus, product_form.html untuk menampilkan form tambah produk, product_detail.html untuk menampilkan detail produk. jadi semua template mewarisi base.html supaya tampilan konsisten

5. Menambahkan tombol Add dan Detail di halaman list produk.

6. Menjalankan migrasi database karena sempat ada perubahan di models.py

7. Mengecek URL JSON dan XML lewat browser maupun Postman.

8. Melakukan add-commit-push ke GitHub, lalu deploy ke PWS.

**6. Apakah ada feedback untuk asdos di tutorial 2?**
Menurut saya penjelasan asdos di tutorial 2 sudah cukup jelas dan membantu, terutama dalam memberi contoh langsung di kode. 

**Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman**
![xml](https://github.com/user-attachments/assets/0fea1d17-da20-4e8f-b761-af628c6ea10a)
![json](https://github.com/user-attachments/assets/73ebaf01-363a-4655-b915-375a1a900aff)

![json pk](https://github.com/user-attachments/assets/8adf62b1-4fe6-4729-a6c5-75a2c4e208d5)
![xml pk](https://github.com/user-attachments/assets/d6cc8bb4-ab2e-43a8-8433-43f449e8baa1)




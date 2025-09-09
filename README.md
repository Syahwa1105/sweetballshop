Nama : Qoriana Syahwa Maharani
NPM : 2406437533
Kelas : PBP-B
Tugas 2 PBP - Implementasi Model-View-Template (MVT) pada Django  

Nama Project : Sweetball Shop

Link PWS : https://pbp.cs.ui.ac.id/qoriana.syahwa/sweetballshop


1.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
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

3. Jelaskan peran settings.py dalam proyek Django! 
peran settings.py yaitu  berisi semua konfigurasi utama project Django. Contohnya seperti:
- daftar aplikasi yang aktif (INSTALLED_APPS)
- konfigurasi database
- middleware
- static files  
- mode debug dan allowed hosts.  
Tanpa settings.py ini, Django tidak akan tahu bagaimana cara menjalankan proyek.

4. Bagaimana cara kerja migrasi database di Django? 
Proses migrasi di Django bekerja dalam dua tahap, yaitu
- makemigrations : Django akan membaca perubahan di model, lalu membuat file migrasi berisi instruksi SQL.  
- migrate : file migrasi tersebut dieksekusi ke database sehingga tabel di database selalu sesuai dengan model Python yang dibuat.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya Django dipilih untuk dijadikan pembelajaran Utama, karena:
- sudah menerapkan arsitektur MVT (mirip MVC) yang umum dipakai di banyak framework
- memiliki banyak fitur bawaan (batteries included) jadi mahasiswa bisa langsung fokus ke konsep
- djanggo memiliki dokumentasi yang jelas dan komunitasnya besar
- djanggo sudh digunakan di industri nyata sehingga ilmu yang dipelajari relevan
- django berbasis Python yang relatif mudah dipelajari.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
menurut saya penjelasan asdos di tutorial 1 sudah sangat membantu untuk menyelesaikan tugas individu 2 ini dan penjelasan yang diberikan juga sangat jelas untuk dipahami dan sangat membantu di tugas individu 2 ini.

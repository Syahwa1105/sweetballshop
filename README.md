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

## **TUGAS 3 PBP - Implementasi Form dan Data Delivery pada Django** 
Nama: Qoriana Syahwa Maharani <br>
NPM: 2406437533<br>
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
- add_product untuk menambah produk baru lewat form.
- product_detail untuk menampilkan detail dari produk tertentu.
- products_json, products_xml, product_json_by_id, product_xml_by_id untuk data delivery (JSON dan XML).

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

## **Tugas 4 PBP - Implementasi Autentikasi, Session, dan Cookies pada Django**

**1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**

AuthenticationForm adalah form bawaan Django yang sudah disediakan khusus untuk menangani proses login. Form ini akan secara otomatis mencocokkan input username dan password yang dimasukkan oleh pengguna dengan data yang tersimpan di database.

Kelebihan:
- Tidak perlu membuat form login dari nol, sehingga lebih praktis.
- Sudah terintegrasi dengan sistem autentikasi Django, jadi lebih aman dan minim bug.
- Validasi input seperti format username dan kesesuaian password dilakukan otomatis.

Kekurangan:
- Tampilan form masih sangat sederhana sehingga biasanya perlu di-custom agar lebih sesuai dengan desain aplikasi.
- Form ini hanya mendukung login dasar dengan username dan password. Jika ingin menambahkan metode login lain (misalnya login dengan email atau OTP), maka perlu membuat form kustom tambahan.

**2.Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**

- Autentikasi adalah proses memverifikasi identitas pengguna. Contoh paling umum adalah login dengan username dan password. Kalau data cocok dengan database, maka pengguna dianggap valid.

- Otorisasi adalah proses untuk menentukan apa yang boleh atau tidak boleh dilakukan oleh pengguna setelah mereka terautentikasi. Misalnya, pengguna biasa hanya bisa menambah produk, tetapi admin bisa menghapus produk.

Django mengimplementasikan nya:
- Autentikasi dilakukan menggunakan model User, fungsi authenticate() dan login(), serta form bawaan seperti AuthenticationForm.

- Otorisasi diatur menggunakan sistem permission (is_staff, is_superuser), middleware, dan decorator seperti @login_required atau @permission_required untuk membatasi akses pada view tertentu.

**3.Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**

**Session:**

- Kelebihan: data disimpan di server, sehingga lebih aman untuk menyimpan informasi penting. Kapasitas juga lebih besar dibanding cookies.

- Kekurangan: membutuhkan ruang penyimpanan di server, sehingga semakin banyak pengguna bisa menambah beban server.

**Cookies:**

- Kelebihan: mudah digunakan, bisa menyimpan data kecil langsung di browser, dan data dapat bertahan walaupun browser ditutup.

- Kekurangan: kapasitasnya terbatas (sekitar 4KB) dan rawan dimanipulasi karena disimpan di sisi client.

**4.Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**

Cookies tidak sepenuhnya aman secara default, karena data yang tersimpan di sisi client bisa saja dicuri atau dimanipulasi. Risiko yang sering muncul antara lain pencurian cookie (session hijacking) atau penyalahgunaan cookie lewat serangan XSS.

Django punya mekanisme perlindungan bawaan, antara lain:

- Memberikan atribut HttpOnly pada cookie sehingga tidak bisa diakses dengan JavaScript.

- Cookie bisa dipaksa hanya dikirim lewat HTTPS dengan mengaktifkan SESSION_COOKIE_SECURE = True.

- Django juga menambahkan proteksi CSRF token pada form, sehingga serangan request palsu bisa dicegah.

Dengan fitur-fitur tersebut, risiko dari penggunaan cookies bisa diminimalisir.

**5.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

**Membuat fungsi dan form registrasi**

Pertama, saya menambahkan fungsi register di views.py dengan memanfaatkan UserCreationForm bawaan Django. Fungsi ini memungkinkan pengguna untuk membuat akun baru. Jika berhasil, pengguna akan langsung diarahkan ke halaman login. Saya juga menambahkan template register.html untuk menampilkan form registrasi.

**Membuat fungsi login dan logout**

Kedua, saya menambahkan fungsi login_user yang menggunakan AuthenticationForm. Jika login berhasil, pengguna akan diarahkan ke halaman utama. Saya juga membuat fungsi logout_user yang akan menghapus sesi login dan menghapus cookie last_login.

**Menambahkan proteksi dengan login_required**

Agar halaman utama (show_main) hanya bisa diakses oleh pengguna yang sudah login, saya menambahkan decorator @login_required(login_url='/login'). Hal ini juga saya terapkan di beberapa fungsi lain seperti add_product dan product_detail.

**Menghubungkan model Product dengan User**

Setelah autentikasi dasar selesai, saya baru menambahkan field user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) di dalam model Product. Dengan cara ini, setiap produk yang dibuat akan tercatat siapa pemiliknya.

**Migrasi database**

Saya menjalankan python manage.py makemigrations dan python manage.py migrate untuk memperbarui struktur database sesuai dengan perubahan model.

**Menghubungkan produk dengan user saat ditambahkan**

Pada fungsi add_product, saya memodifikasi kode agar produk baru otomatis mencatat pengguna yang sedang login (request.user) sebagai author.

**Menampilkan informasi user dan cookie last_login**

Di show_main, saya menambahkan context baru berupa request.user.username serta cookie last_login. Informasi ini saya tampilkan di halaman utama, sehingga pengguna bisa melihat siapa yang sedang login dan kapan terakhir kali login.

**Menampilkan author di halaman detail produk**

Pada template product_detail.html, saya menambahkan kode untuk menampilkan author dari produk. Jika tidak ada, maka ditampilkan “Anonymous”.

**Membuat dua akun dengan dummy data**
Saya membuat dua akun pengguna dan masing-masing saya isi dengan tiga produk dummy. Dengan ini saya bisa melihat bahwa data produk memang terikat dengan user yang membuatnya.
- tampilan akun pertama yaitu LanyBallShop dan my articles di dalam nya (3 product berbeda) :
  <img width="1920" height="1080" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/4a2f2ee4-08f5-4e28-87bb-5ceb78d6798f" />

- tampilan akun kedua yaitu cookieballshop dan my articles nya di dalam nya (3 product berbeda): 

  <img width="1920" height="1080" alt="Screenshot (57)" src="https://github.com/user-attachments/assets/e6a674f6-beff-40c4-a526-b8e4815764b7" />

**Commit dan push ke GitHub serta PWS**

Setelah semua berfungsi dengan baik, saya melakukan add, commit, dan push ke GitHub serta PWS.


## **Tugas 5 PBP - Desain Web menggunakan HTML, CSS dan Framework CSS

**1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Browser menentukan gaya yang berlaku dengan aturan specificity. Urutan prioritas dari yang tertinggi ke terendah:
1. Inline style (mis. <div style="...">) — prioritas tertinggi.
2. ID selector (#my-id) — lebih spesifik daripada class.
3. Class, attribute, pseudo-class (.my-class, [type="text"], :hover).
4. Element selector (div, p, h1) dan pseudo-element (::before).
5. User agent stylesheet (default browser) — paling rendah.

Jika dua selector memiliki specificity yang sama, aturan yang muncul paling akhir di stylesheet atau yang dimuat paling akhir itu yang berlaku. Untuk memaksa aturan tertentu, hindari menggunakan!important kecuali benar-benar perlu—karena itu menyulitkan pemeliharaan.

**2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design memungkinkan antarmuka menyesuaikan ukuran dan orientasi layar (desktop, tablet, smartphone). Manfaatnya seperti :
- UX konsisten pada berbagai perangkat.
- Aksesibilitas lebih baik (pengguna mobile jadi mudah berinteraksi).
- SEO & performa: mesin pencari dan metrik pengguna cenderung menghargai situs mobile-friendly.

Contoh nya adalah : 
- Sudah responsive: Google Search, Twitter seperti layout, typography, dan interaksi menyesuaikan layar.
- Kurang responsive: situs lama (terutama beberapa situs instansi publik) yang masih fixed-width seperti harus di-zoom/geser manual di smartphone.

**3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Dalam CSS, setiap elemen dianggap sebagai sebuah kotak yang disebut box model. Box model terdiri dari empat lapisan utama: content, padding, border, margin.
**- Content
Bagian terdalam yang berisi teks, gambar, atau elemen lain.

**- Padding
Ruang di dalam elemen, yaitu jarak antara content dan border. Padding memberi “napas” pada isi elemen.

.card {
  padding: 16px;
}


**- Border
Garis yang mengelilingi padding dan content. Border bisa memiliki warna, ketebalan, atau gaya tertentu (solid, dashed, dotted).

.card {
  border: 2px solid #ccc;
}


**- Margin
Ruang di luar border yang memisahkan elemen dari elemen lain di sekitarnya.

.card {
  margin: 20px;
}

**Kapan digunakan?
- Pakai padding untuk memberi ruang di dalam elemen agar isi lebih mudah dibaca.
- Pakai border untuk membedakan satu elemen dengan elemen lain misalnya card produk.
- Pakai margin untuk mengatur jarak antar elemen dalam layout misalnya jarak antar card.

**4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
CSS menyediakan dua sistem utama untuk mengatur tata letak modern: Flexbox dan Grid.
**a. Flexbox (Flexible Box)
- Dirancang untuk layout satu dimensi (baris atau kolom).
- Memudahkan pengaturan distribusi ruang antar elemen dan alignment.
- Cocok untuk navbar, daftar tombol, form input berjejer, atau layout yang linear.

**b. Grid Layout
- Dirancang untuk layout dua dimensi (baris dan kolom).
- Memberi kontrol penuh pada struktur halaman.
- Cocok untuk galeri produk, dashboard, atau tampilan dengan kolom-kolom tetap.

jadi kesimpulan nya gunakan Flexbox jika hanya ingin mengatur posisi item dalam baris/kolom dan gunakan Grid jika butuh layout besar dengan struktur baris dan kolom yang konsisten.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Dalam mengimplementasikan checklist, saya menyesuaikan alur kerja dengan kebutuhan aplikasi saya (SweetBallShop) Berikut langkah-langkah yang saya lakukan:

1. Menambahkan Tailwind CSS melalui CDN di file base.html agar styling lebih konsisten dan responsif.
2. Membuat navbar yang sederhana dan responsif untuk navigasi halaman utama.
3. Membangun tampilan daftar produk menggunakan komponen card yang reusable, kemudian meng-include file product_card.html di halaman utama.
4. Mengatur form produk (create & edit) menggunakan ModelForm di forms.py, lalu menghubungkannya dengan views.py.
5. Menambahkan fitur delete produk menggunakan metode POST dengan halaman konfirmasi sederhana.
6. Membuat tampilan empty state dengan gambar no-product.png agar halaman tetap informatif meskipun belum ada data.
7. Testing aplikasi di lokal, lalu melakukan commit dan push ke GitHub serta PWS untuk memastikan bisa diakses secara online.


## **Tugas 6 PBP - Javascript dan AJAX**

**1. Apa perbedaan antara synchronous request dan asynchronous request **

Pada *synchronous request*, proses komunikasi antara client dan server berjalan secara berurutan. Browser akan menunggu hingga server mengirimkan respon sebelum bisa melakukan tindakan lain. Akibatnya, jika proses di server memakan waktu lama, tampilan halaman bisa terasa lambat atau bahkan “terhenti sementara”.
Sedangkan pada *asynchronous request*, permintaan ke server dilakukan di latar belakang tanpa harus memuat ulang seluruh halaman. Browser tetap bisa berinteraksi dengan pengguna sambil menunggu respon dari server. AJAX menggunakan konsep ini sehingga data bisa diperbarui sebagian tanpa perlu *refresh* halaman.

**2. Bagaimana AJAX bekerja di Django (alur request–response)?**

Ketika pengguna melakukan aksi seperti menambah atau menghapus data, JavaScript akan mengirimkan *request* ke server menggunakan `fetch()` atau `XMLHttpRequest`. Django kemudian menerima permintaan tersebut melalui *view* yang disiapkan khusus untuk menangani AJAX, biasanya mengembalikan respon dalam format JSON.
Respon JSON ini dikirim kembali ke JavaScript di sisi client, kemudian hasilnya diolah untuk memperbarui tampilan halaman tanpa melakukan *reload*. Dengan cara ini, Django tetap berfungsi sebagai pengatur logika dan data, sementara interaksi pengguna ditangani secara dinamis oleh JavaScript.

**3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?**

Beberapa keuntungan utama penggunaan AJAX antara lain:

* **Efisiensi waktu dan data:** hanya bagian tertentu dari halaman yang diperbarui, bukan keseluruhan halaman.
* **Pengalaman pengguna lebih halus:** interaksi terasa cepat dan responsif tanpa perlu *reload* penuh.
* **Pemisahan tanggung jawab yang jelas:** Django fokus pada logika backend, sedangkan JavaScript menangani tampilan interaktif di frontend.
* **Kemudahan integrasi fitur dinamis:** seperti *modal form*, *toast notification*, atau *live refresh* data, yang sulit dicapai dengan render tradisional.

**4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?**

Untuk menjaga keamanan, beberapa langkah penting perlu diterapkan:

* **Gunakan CSRF Token:** Django menyediakan mekanisme `csrftoken` yang harus dikirim bersama setiap *POST request* untuk mencegah *Cross-Site Request Forgery*.
* **Validasi input di server:** meskipun validasi juga dilakukan di sisi client, Django harus tetap memverifikasi data di sisi server agar tidak mudah diserang manipulasi.
* **Gunakan HTTPS:** semua komunikasi antara client dan server sebaiknya terenkripsi agar data sensitif seperti kata sandi tidak bocor.
* **Batasi respon dari server:** hindari menampilkan pesan error yang terlalu detail pada respon AJAX, agar tidak memberikan petunjuk berlebih kepada pihak yang tidak berwenang.

**5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?**

AJAX secara signifikan meningkatkan *user experience* karena membuat interaksi di halaman terasa lebih cepat dan natural. Pengguna tidak perlu menunggu proses *reload* setiap kali menambah, mengedit, atau menghapus data. Selain itu, fitur seperti *loading state*, *toast notification*, dan *modal form* memberikan umpan balik langsung yang membantu pengguna memahami apa yang sedang terjadi.
Secara keseluruhan, AJAX membuat aplikasi web terasa lebih responsif, modern, dan nyaman digunakan.




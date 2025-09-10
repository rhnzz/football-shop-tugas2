- Tautan menuju aplikasi PWS yang sudah di-deploy: 
https://raihana-auni-footballshoptugas2.pbp.cs.ui.ac.id/
- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1 . membuat direktori untuk proyek, mengaktifkan virtual env untuk mengisolasi package, meng-install beberapa depedencies, lalu membuat proyek django football_shop_tugas2
2 . memodifikasi .env, .env.prod, settings.py, lalu menjalankan server untuk mengecek apakah sudah berhasil dibuat aplikasinya
3 . update ke git dengan membuat repo baru terlebih dahulu, git init, menambahkan file .gitignore, menghubungkan repo lokal dengan repo di git, atur branch, melakukan git add, commit, dan push
4 . membuat proyek baru di PWS, mengatur env yg sesuai, menambahkan allowed host di settings.py,  melakukan git add, commit, dan push, menjalankan 3 instruksi yang diberikan di PWS, cek proyeknya dengan buka dari PWS
5 . membuat aplikasi main dengan kondisi virtual env aktif, lalu menambahkan main ke list installed apps di settings.py
6 . membuat direktori templates di app main, membuat file html, dan coding file html tersebut
7 . mengubah/coding file models.py di app main, lalu membuat dan menetapkan migrasi setiap melakukan perubahan di file models.py
8 . mengubah/coding file views.py, membuat fungsi baru yang menerima request
9 . membuat file urls.py di app main, coding files urls.py dan menambahkan path yang sesuai, coding urls di proyek juga, menambahkan import include, an menambahkan app main di url patterns, run server dan buka webnya buat liat udah sesuai atau belum
10 . membuat file test.py dan coding untuk menja;ankan unit testing, menjalankan "python manage.py test main" buat jalanin test app main
11 . melakukan git add, commit,dan push. dan melakukan push PWS  
- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
https://drive.google.com/file/d/19qkB3UfHa9DW5VPIdgQPukL55tcW68V1/view?usp=drivesdk (gambar sendiri)
penjelasan:
urls.py : yang mengatur atau memetakan path url proyek ke function atau app tertentu
views.py : sebagai jembatan antara models.py dan template html, dapat mengambil data dari models.py dan mengirimkan ke template html
models.py : mengirim data (bisa ada yg dari database) yang dibutuhkan views.py
template html : menerima data dari views.py dan memberi halaman HTML/halaman web
- Jelaskan peran settings.py dalam proyek Django!
peran settings.py adalah sebagai tempat utama untuk melakukan konfigurasi semua pengaturan penting untuk proyek django
- Bagaimana cara kerja migrasi database di Django?
pertama 'makemigration" untuk memeriksa perubahan dan membuat file migrasi yang berisi perubahan yang belum diaplikasikan
kedua "migrate" mengaplikasikan seluruh perubahan yang terdapat di berkas migrasi 
- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
menurut saya karena django menggunakan bahasa python dan pola arsitektur django menggunakan MVT (model-view-template)
- Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
tidak ada :D, sudah sangat baik penjelasan di tutorial 0 maupin 1
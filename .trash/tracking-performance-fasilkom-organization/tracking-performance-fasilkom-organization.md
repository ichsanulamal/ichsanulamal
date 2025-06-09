# Fasilkom Organization Tracer

​	Proyek data engineering  untuk menganalisis sumber daya manusia pada suatu organisasi, dalam kasus ini mahasiswa atau mantan mahasiswa Fasilkom UI. 



## Tujuan dan Manfaat

- Melihat efektivitas dan sebaran bidang pekerjaan mahasiswa Fasilkom di masa kuliah maupun setelah kuliah
- Melihat organisasi mana yang "paling membantu" 
- Untuk organisasi bisa lebih memperhatikan bagian HR nya agar lebih tepat sasaran program upgradingnya, bukan hanya sebatas "program formalitas" saja 
- Pengarsipan CRM/HR organisasi dengan mantan anggota
- Melihat yang paling produktif sepanjang periode adanya Fasilkom
- Just For Fun :v:



Sumber data: linkedin



## Tahapan

1. Extract

   - Collecting data dari linkedin bagian search section atau DB Fasilkom kalo bisa

   - Manfaatkan **linkedinAPI** 
   - Kalo APInya terbatas, scrapping manual pakai **selenium**, **scrappy**, atau lain2. Kalo bisa diotomatisasi tambah bagus

2. Transform

   - Memastikan semua data "clean"

   - Database design dan membuat *constraint* untuk data

3. Load 

   - Load data yang sudah benar ke database bebas
   - Tentukan tujuan dan buat ML model untuk prediksi???
   - Buat dashboard, report, dkk dari yang ingin dianalisis pakai **Tableau** atau **PowerBI** atau **Kaggle**, dll

4. ### **Insight yang bisa didapat:**

   - Pertumbuhan jumlah mahasiswa Fasilkom (Ilkom juga SI) dari tahun ke tahun
   - Ratio bidang pekerjaan tiap angkatan, tiap jurusan. Bisa juga kategorisasi big company, global company, dll untuk lihat berapa persentase dari tiap angkatan yang kerja company2 tersebut.
   - Rata2 magang tiap orang di masa kuliah, tiap angkatan. 
   - Untuk organisasi <A>, anggotanya kerja di bidang mana saja. Seberapa cepat anggota tersebut mendapat magang atau pekerjaan, yang mana organisasi yang paling membantu mahasiswa.
   - Meneliti minat tiap orang dan buat algoritma untuk kategorisasi atau klasterisasi minatnya agar bisa dikumpulkan dan mendapat insight dari yang sudah senior
   - ...tambahkan sendiri



## Keypoints

- Usahakan terotomatisasi secara periodik, buat **scheduler**
- Seiring waktu, data tiap orang pasti berubah, pikirkan gimana caranya agar bisa diupdate otomatis dan *integrity* di database tetap terjaga
- Kalo volumenya makin naik, coba-coba pakai **cloud** atau platform gratisan buat nampung datanya, tapi kayanya ga akan sih


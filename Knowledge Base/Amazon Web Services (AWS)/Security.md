AWS Identity and Access Management (AWS IAM)
AWS Shield
  
AWS Key Management Service (AWS KMS)
AWS Web Application Firewall (AWS WAF)
  
Amazon Inspector
Amazon GuardDuty
  
### Summary
- Pertama, AWS menyajikan _shared responsibility model_ alias model tanggung jawab bersama. AWS bertanggung jawab atas keamanan dari cloud sementara Anda bertanggung jawab untuk keamanan di cloud.
- Kemudian, AWS IAM memungkinkan Anda untuk memiliki users, groups, roles, dan policies.
    - _**Users**_ dapat Anda pakai untuk _login_ atau masuk ke AWS dengan menggunakan nama pengguna dan kata sandi. Ia juga secara default tidak memiliki _permission_ (izin) sama sekali.
    - _**Groups**_ merupakan kumpulan dari beberapa pengguna.
    - _**Roles**_ adalah identitas yang berguna untuk memberikan akses kredensial sementara dan permission untuk jangka waktu tertentu.
    - _**Policies**_ berfungsi untuk memberikan permission ke sebuah identitas secara eksplisit, baik _allow_ (mengizinkan) atau _deny_ (menolak) suatu tindakan tertentu di AWS.
    - IAM juga menghadirkan _**identity federation**_ (federasi identitas). Jika suatu perusahaan telah memiliki penyimpanan identitasnya sendiri, maka user di perusahaan tersebut dapat terkoneksi ke AWS menggunakan _role based access_ (akses berbasis peran). Hal itu memungkinkan user melakukan sekali _login_ untuk sistem perusahaan tersebut dan sekaligus juga lingkungan AWS.
    - Satu hal terakhir yang perlu diingat tentang IAM adalah _**multi-factor authentication**_ (MFA). Pastikan Anda mengaktifkan MFA untuk setiap user, terutama _root user_ yang memiliki semua permission secara default dan tak dapat direstriksi.
- Selanjutnya, kita juga telah membahas AWS Organizations. Saat menggunakan AWS, kemungkinan Anda akan memiliki beberapa akun. Biasanya, akun digunakan untuk mengisolasi beban kerja, lingkungan, tim, atau aplikasi. Nah, AWS Organizations dapat membantu Anda untuk mengelola beberapa akun secara hierarkis.
- Tak luput kita juga telah belajar mengenai _compliance_(kepatuhan). AWS menggunakan auditor pihak ketiga untuk membuktikan compliance-nya terhadap beragam program compliance. Anda dapat menggunakan:
    - AWS Compliance Center untuk menemukan informasi lebih lanjut tentang compliance.
    - AWS Artifact untuk mendapatkan akses ke dokumen compliance.
Persyaratan compliance yang Anda miliki mungkin dapat bervariasi untuk setiap aplikasinya.
- Lalu, kita telah menelaah tentang serangan distributed denial-of-service (DDoS) dan cara menanganinya dengan menggunakan layanan seperti ELB, security group, AWS Shield, dan AWS WAF.
- Kemudian, kita juga telah mempelajari materi enkripsi. Di AWS, Anda sebagai pemilik data bertanggung jawab atas keamanannya. Itu berarti Anda perlu menerapkan enkripsi untuk data yang Anda miliki, baik _in-transit_ (ketika dikirim) maupun _at rest_ (saat disimpan).
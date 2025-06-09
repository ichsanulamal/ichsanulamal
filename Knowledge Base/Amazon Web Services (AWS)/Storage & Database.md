Instance Store dan Amazon Elastic Block Store (Amazon EBS)
Amazon Simple Storage Service (Amazon S3)
jika Anda memiliki objek atau file yang lengkap dan hanya membutuhkan sesekali perubahan, maka pilihlah **Amazon S3**. Namun, jika Anda membutuhkan proses read (baca) data yang kompleks, maka tentu saja Anda perlu memilih **Amazon EBS**.
- **S3 Standard**
- **S3 Standard-Infrequent Access (S3 Standard-IA)**
- **S3 One Zone-Infrequent Access (S3 One Zone-IA)**Berbeda dengan S3 Standard dan S3 Standard-IA yang menyimpan data minimal di tiga Availability Zone, kelas penyimpanan S3 One Zone-IA menyimpan data hanya di satu Availability Zone.Nah, ini menjadikannya kelas penyimpanan yang perlu Anda pertimbangkan jika memiliki kondisi seperti berikut:
- **S3 Intelligent-Tiering**Pada kelas penyimpanan S3 Intelligent-Tiering, Amazon S3 memantau pola akses objek.
- **S3 Glacier**Opsi kelas penyimpanan ini ideal untuk data audit. Katakanlah Anda perlu menyimpan data selama beberapa tahun untuk tujuan audit. Sehingga, tidak memerlukan proses akses yang langsung pada saat itu juga.
- **S3 Glacier Deep Archive**
  
Amazon Elastic File System (Amazon EFS)
  
Amazon Relational Database Service (Amazon RDS)
Amazon Aurora (oltp)
  
Amazon DynamoDB (key, value)
Amazon Redshift (olap)
  
AWS Database Migration Service
  
Amazon DocumentDB
Amazon Neptune (social network)
  
### Blockchain based
Amazon Managed Blockchain
Amazon Quantum Ledger Database (Amazon QLDB)
  
### Caching
Amazon ElastiCache
Amazon DynamoDB Accelerator (DAX)
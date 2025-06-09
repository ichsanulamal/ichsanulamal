  
### Tipe Instance EC2
- **General purpose instances** (Instance tujuan umum)
- **Compute optimized instances** (Instance teroptimasi untuk komputasi)
- **Memory optimized instances** (Instance teroptimasi untuk memori)
- **Accelerated computing instances** (Instance terakselerasi untuk komputasi)
- **Storage optimized instance** 
### Harga
- On-Demand (Sesuai Permintaan)
- Savings Plans (Rencana Tabungan)
- Reserved Instances (Instance Terpesan)
    
    Opsi pembayaran pada Reserved Instances:
    
    1. _All upfront_ (semua di muka), yaitu Anda membayarnya secara penuh saat Anda berkomitmen.
    2. _Partial upfront_ (sebagian di muka), di mana Anda membayar sebagian di awal.
    3. _No upfront_ (tanpa uang muka), di mana Anda tak membayar apa pun di muka.
- Spot Instances (Instance Spot)
- Dedicated Hosts (Host Khusus)
### EC2 Auto Scaling
### Elastic Load Balancing (ELB)
### Amazon Simple Queue Service (Amazon SQS)
### Amazon Simple Notification Service (Amazon SNS)
  
## Serverless
- Jika Anda ingin menjalankan aplikasi dan menginginkan akses penuh ke sistem operasinya seperti Linux atau Windows, Anda bisa menggunakan **Amazon EC2**.
- Jika Anda ingin menjalankan fungsi yang berjalan singkat, aplikasi berbasis kejadian, dan Anda tak ingin mengelola infrastrukturnya sama sekali, gunakanlah layanan **AWS Lambda**.
- Jika Anda ingin menjalankan beban kerja berbasis Docker container di AWS, langkah yang perlu Anda lalui adalah:
    - Anda harus memilih layanan orkestrasinya terlebih dahulu. Anda bisa menggunakan **Amazon ECS** atau **Amazon EKS**.
    - Setelah memilih alat orkestrasinya, kemudian Anda perlu menentukan platformnya. Anda dapat menjalankan container pada **EC2 instance** yang Anda kelola sendiri atau dalam lingkungan _serverless_ seperti **AWS Fargate** yang dikelola oleh AWS.
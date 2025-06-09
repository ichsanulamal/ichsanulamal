### AWS Regions
  
  
1. Region adalah wilayah yang terisolasi secara geografis di mana Anda dapat mengakses layanan yang diperlukan untuk menjalankan segala macam kebutuhan.
2. Region terdiri dari Availability Zone yang memungkinkan Anda untuk menjalankan seluruh bangunan data center yang terpisah secara fisik dengan jarak puluhan mil sambil menjaga aplikasi Anda tetap bersatu secara logis. Availability Zone membantu Anda untuk dapat mencapai _high availability_ (ketersediaan tinggi) dan _disaster recovery_ (pemulihan bencana) tanpa upaya apa pun dari Anda.
3. AWS Edge locations digunakan untuk menjalankan Amazon CloudFront sehingga dapat memperdekat konten kepada pelanggan Anda di mana pun mereka berada.
  
### IaC
AWS Elastic Beanstalk
AWS CloudFormation
  
  
- Membahas bagaimana klaster logis dari data center membentuk **Availability Zone**. Lalu, Availability Zone membentuk **Region** dan tersebar secara global.
- Menelaah cara memilih Region dan Availability Zone yang ingin dioperasikan. Sebagai praktik terbaik, Anda harus selalu menerapkan infrastruktur minimal di 2 Availability Zone.
- Menilik beberapa layanan AWS seperti Elastic Load Balancing, Amazon SQS, dan Amazon SNS.
- Membicarakan tentang **Edge locations** dan bagaimana Anda dapat menyebarkan konten untuk mempercepat pengiriman ke pelanggan.
- Membahas perangkat edge seperti AWS Outposts yang memungkinkan Anda menjalankan infrastruktur AWS langsung di data center Anda sendiri.
- Mendiskusikan bagaimana cara menyediakan sumber daya AWS melalui berbagai opsi: **AWS Management Console, SDK, CLI, AWS Elastic Beanstalk, dan AWS CloudFormation**--di mana Anda mempelajari cara menyiapkan _infrastructure as code_ (infrastruktur sebagai kode).
### Apa itu Data Modelling?
- Organizing elemen dari setiap data dan bagaimana relasi antara setiap data nya
- Untuk mendukung sistem informasi
### Tahapan
- Mengetahui kebutuhan bisnis dan user applications
- Conceptual Data Modelling
- Logical Data Modelling
- Physical Data Modelling
  
### 1. RDBMS
- Database/Schema : Kumpulan dari Table
- Tables/Relation : Kumpulan row dan column
    
    ### ACID Transactions
    
    Atomicity : semua transaksi diproses atau tidak ada yang diproses
    
    Consistency : Perlu ada constraint dan rules saat menuliskan ke database
    
    Isolation : transaction diproses secara independen dan aman, tidak peduli dengan urutannya
    
    Durability : transaksi yang sudah terjadi harus selalu disimpan meskipun sistemnya rusak
    
    ### Jangan menggunakan RDBMS Jika:
    
    - Large amounts of data
    - Perlu berbagai tipe format data
    - Perlu throughput banyak atau fast read
    - Schema yang fleksibel
    - High availability
    - Perlu horizontal scalability : menambah server
    
    Contoh RDBMS : PostgreSQL, Oracle, MySQL, dll
    
  
### 2. NoSQL
- Apache Cassandra (Partition Row Store)
- MongoDB (Document Store)
- DynamoDB (Key-Value Store)
- Apache HBase (Wide Column Store)
- Neo4j (Graph Database)
### Apache Cassandra
- Keyspace (mirip schema), Table, Row
- Partition
  
![[/Untitled 8.png|Untitled 8.png]]
![[/Untitled 1 5.png|Untitled 1 5.png]]
![[/Untitled 2 5.png|Untitled 2 5.png]]
![[/Untitled 3 4.png|Untitled 3 4.png]]
![[/Untitled 4 4.png|Untitled 4 4.png]]
![[/Untitled 5 4.png|Untitled 5 4.png]]
![[/Untitled 6 3.png|Untitled 6 3.png]]
![[/Untitled 7 2.png|Untitled 7 2.png]]
![[/Untitled 8 2.png|Untitled 8 2.png]]
![[Untitled 9.png]]
![[Untitled 10.png]]
![[Untitled 11.png]]
![[Untitled 12.png]]
![[Untitled 13.png]]
## ACID
![[Untitled 14.png]]
![[Untitled 15.png]]
![[Untitled 16.png]]
![[Untitled 17.png]]
![[Untitled 18.png]]
![[Untitled 19.png]]
![[Untitled 20.png]]
![[Untitled 21.png]]
![[Untitled 22.png]]
![[Untitled 23.png]]
![[Untitled 24.png]]
![[Untitled 25.png]]
![[Untitled 26.png]]
![[Untitled 27.png]]
![[Untitled 28.png]]
![[Untitled 29.png]]
![[Untitled 30.png]]
![[Untitled 31.png]]
![[Untitled 32.png]]
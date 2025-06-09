### Kapan butuh NoSQL?
- Perlu High availability
- Memiliki data dengan ukuran besar
- Perlu linear scalability
- Low latency
- Perlu fast reads and write
Pada **distributed database**, agar memiliki **high availability** diperlukan data yang tersebar atau diperlukan banyak copy dari data
**Eventual Consistency**: Consistency model pada **distributed** computing untuk mencapai **high availability (AP)**. Apabila tidak ada update pada suatu item, maka akses ke item tersebut akan mengembalikan update item terakhir kali.
  
### CAP (Consistency, Availability, Partition Tolerance) Theorem
Trilema
Consistency: Setiap read mengembalikan item terbaru yang benar atau error
Availability: Setiap request diterima dan response dikirim (meskipun data yang dikirim tidak update)
Partition tolerance: Sistem tetap berjalan meskipun ada node yang mati atau gangguan lainnya seperti gangguan network etc.
![[/Untitled 34.png|Untitled 34.png]]
[![](https://facingissuesonitcom.files.wordpress.com/2020/02/cap-theorem.jpg?w=1000)](https://facingissuesonitcom.files.wordpress.com/2020/02/cap-theorem.jpg?w=1000)
  
## Apache Cassandra
- Perlu **Denormalization** untuk mencapai fast reads, karena tidak ada **JOINS**
- Optimized untuk fast reads
### Primary Key
- Unique
- Hashing pada nilai PK ini mengakibatkan penempatan ke node tertentu pada sistem
- Data distibuted melalui partition key ini
- Simple atau Composite
### Clustering Columns
- Sort data DESC order
  
![[/Untitled 1 7.png|Untitled 1 7.png]]
![[/Untitled 2 7.png|Untitled 2 7.png]]
![[/Untitled 3 6.png|Untitled 3 6.png]]
![[/Untitled 4 6.png|Untitled 4 6.png]]
![[/Untitled 5 6.png|Untitled 5 6.png]]
![[/Untitled 6 5.png|Untitled 6 5.png]]
![[/Untitled 7 4.png|Untitled 7 4.png]]
![[/Untitled 8 4.png|Untitled 8 4.png]]
![[/Untitled 9 3.png|Untitled 9 3.png]]
![[/Untitled 10 3.png|Untitled 10 3.png]]
![[/Untitled 11 3.png|Untitled 11 3.png]]
![[/Untitled 12 3.png|Untitled 12 3.png]]
![[/Untitled 13 3.png|Untitled 13 3.png]]
![[/Untitled 14 3.png|Untitled 14 3.png]]
![[/Untitled 15 3.png|Untitled 15 3.png]]
![[/Untitled 16 3.png|Untitled 16 3.png]]
![[/Untitled 17 3.png|Untitled 17 3.png]]
![[/Untitled 18 3.png|Untitled 18 3.png]]
![[/Untitled 19 3.png|Untitled 19 3.png]]
![[/Untitled 20 3.png|Untitled 20 3.png]]
![[/Untitled 21 3.png|Untitled 21 3.png]]
![[/Untitled 22 3.png|Untitled 22 3.png]]
![[/Untitled 23 3.png|Untitled 23 3.png]]
![[/Untitled 24 3.png|Untitled 24 3.png]]
![[/Untitled 25 2.png|Untitled 25 2.png]]
![[/Untitled 26 2.png|Untitled 26 2.png]]
Cloud Managed
- RDS, DynamoDB, S3
Self-Managed
- EC2 + Postgresql, EC2 + Cassandra, EC2 + Unix FS
Redshift/Teradata Aster/Oracle Exadata/Azure SQL: SQL, Columnar, Massively Parallel
Pada DBMS SQL, biasanya **setiap query** selalu dieksekusi pada **single CPU** dari 1 node  
Dengan Massively Parallel Processing (MPP), 1 query dapat dieksekusi ke **multiple CPU** atau node
### Redshift
SQL, Columnar, Massively Parallel  
Komponen:  
- Leader Node: Koordinasi Compute Nodes, external communication, optimisasi query
- Compute Nodes: Memiliki beberapa slices, cluster dengan n slices dapat memproses n partisi dari table secara simultan
### Optimizing ETL Design
Improving performance untuk query time
### Distribution Styles
- EVEN distribution
    - Round robin load-balancing (membagi row berurutan ke tiap CPU)
    - Drawback: Sulit untuk join karena bisa jadi dimension table dan fact table diproses pada CPU yang berbeda (Shuffling: pindah data antar node pada cluster)
- All distribution
    - Distributing `fact` dengan EVEN, tetapi `dimensions` di load ke semua CPU
    - Tidak ada shuffling
- AUTO distribution:
    - Tergantung redshift
    - Apabila tabel berukuran kecil menggunakan ALL, apabila sebaliknya menggunakan EVEN
- KEY distribution
    - Row dibagi berdasarkan KEY yang sama. Artinya, setiap CPU hanya berisi row dengan KEY yang sama.
    - Drawback: Skewed distribution
### Sorting Key
Diurutkan berdasarkan key dan kemudian round robin seperti EVEN distribution, sehingga memudahkan join
  
![[/Untitled 45.png|Untitled 45.png]]
![[/Untitled 1 10.png|Untitled 1 10.png]]
![[/Untitled 2 10.png|Untitled 2 10.png]]
![[/Untitled 3 8.png|Untitled 3 8.png]]
![[/Untitled 4 8.png|Untitled 4 8.png]]
![[/Untitled 5 8.png|Untitled 5 8.png]]
![[/Untitled 6 7.png|Untitled 6 7.png]]
![[/Untitled 7 6.png|Untitled 7 6.png]]
![[/Untitled 8 6.png|Untitled 8 6.png]]
![[/Untitled 9 5.png|Untitled 9 5.png]]
![[/Untitled 10 5.png|Untitled 10 5.png]]
![[/Untitled 11 5.png|Untitled 11 5.png]]
![[/Untitled 12 5.png|Untitled 12 5.png]]
![[/Untitled 13 5.png|Untitled 13 5.png]]
![[/Untitled 14 5.png|Untitled 14 5.png]]
![[/Untitled 15 5.png|Untitled 15 5.png]]
![[/Untitled 16 5.png|Untitled 16 5.png]]
![[/Untitled 17 5.png|Untitled 17 5.png]]
![[/Untitled 18 5.png|Untitled 18 5.png]]
![[/Untitled 19 5.png|Untitled 19 5.png]]
![[/Untitled 20 5.png|Untitled 20 5.png]]
![[/Untitled 21 5.png|Untitled 21 5.png]]
![[/Untitled 22 5.png|Untitled 22 5.png]]
![[/Untitled 23 5.png|Untitled 23 5.png]]
![[/Untitled 24 5.png|Untitled 24 5.png]]
![[/Untitled 25 4.png|Untitled 25 4.png]]
![[/Untitled 26 4.png|Untitled 26 4.png]]
![[/Untitled 27 3.png|Untitled 27 3.png]]
![[/Untitled 28 3.png|Untitled 28 3.png]]
![[/Untitled 29 3.png|Untitled 29 3.png]]
![[/Untitled 30 3.png|Untitled 30 3.png]]
![[/Untitled 31 3.png|Untitled 31 3.png]]
![[/Untitled 32 3.png|Untitled 32 3.png]]
![[/Untitled 33 3.png|Untitled 33 3.png]]
![[/Untitled 34 3.png|Untitled 34 3.png]]
![[/Untitled 35 3.png|Untitled 35 3.png]]
![[/Untitled 36 2.png|Untitled 36 2.png]]
![[/Untitled 37 2.png|Untitled 37 2.png]]
![[/Untitled 38 2.png|Untitled 38 2.png]]
![[/Untitled 39 2.png|Untitled 39 2.png]]
![[/Untitled 40 2.png|Untitled 40 2.png]]
![[/Untitled 41 2.png|Untitled 41 2.png]]
![[/Untitled 42 2.png|Untitled 42 2.png]]
![[/Untitled 43 2.png|Untitled 43 2.png]]
![[/Untitled 44 2.png|Untitled 44 2.png]]
![[/Untitled 45 2.png|Untitled 45 2.png]]
![[Untitled 46.png]]
![[Untitled 47.png]]
![[Untitled 48.png]]
![[Untitled 49.png]]
![[Untitled 50.png]]
![[Untitled 51.png]]
![[Untitled 52.png]]
![[Untitled 53.png]]
![[Untitled 54.png]]
![[Untitled 55.png]]
![[Untitled 56.png]]
![[Untitled 57.png]]
![[Untitled 58.png]]
![[Untitled 59.png]]
![[Untitled 60.png]]
![[Untitled 61.png]]
![[Untitled 62.png]]
![[Untitled 63.png]]
![[Untitled 64.png]]
![[Untitled 65.png]]
![[Untitled 66.png]]
![[Untitled 67.png]]
![[Untitled 68.png]]
![[Untitled 69.png]]
![[Untitled 70.png]]
![[Untitled 71.png]]
![[Untitled 72.png]]
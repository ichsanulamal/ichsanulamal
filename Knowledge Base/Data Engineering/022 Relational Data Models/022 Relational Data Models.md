### OLAP VS OLTP
OLAP → analytical
OLTP → transactional
  
### Normalization
Digunakan untuk transactional secara efisien → Mengurangi redundancy dan meningkatkan integrity
- 1NF → semua cell unique dan single values
- 2NF → semua kolom perlu dependen dengan primary key
- 3NF → Tidak ada transitif dependensi
### Denormalization
Digunakan untuk read heavy workloads → Meningkatkan performance untuk read
  
Fact tables: measurements, metrics, or facts dari proses bisnis
Dimension Tables: people, products, place, time untuk untuk menjelaskan fact tables
### Fact and Dimension Tables
- Star Schemas
    - benefit: denormalized, simple query, fast aggregations
    - drawbacks: data integrity, decrease flexibility, simplified
- Snowflake Schemas
    
  
![[/Untitled 33.png|Untitled 33.png]]
![[/Untitled 1 6.png|Untitled 1 6.png]]
![[/Untitled 2 6.png|Untitled 2 6.png]]
![[/Untitled 3 5.png|Untitled 3 5.png]]
![[/Untitled 4 5.png|Untitled 4 5.png]]
![[/Untitled 5 5.png|Untitled 5 5.png]]
![[/Untitled 6 4.png|Untitled 6 4.png]]
![[/Untitled 7 3.png|Untitled 7 3.png]]
![[/Untitled 8 3.png|Untitled 8 3.png]]
![[/Untitled 9 2.png|Untitled 9 2.png]]
![[/Untitled 10 2.png|Untitled 10 2.png]]
![[/Untitled 11 2.png|Untitled 11 2.png]]
![[/Untitled 12 2.png|Untitled 12 2.png]]
![[/Untitled 13 2.png|Untitled 13 2.png]]
![[/Untitled 14 2.png|Untitled 14 2.png]]
![[/Untitled 15 2.png|Untitled 15 2.png]]
![[/Untitled 16 2.png|Untitled 16 2.png]]
![[/Untitled 17 2.png|Untitled 17 2.png]]
![[/Untitled 18 2.png|Untitled 18 2.png]]
![[/Untitled 19 2.png|Untitled 19 2.png]]
![[/Untitled 20 2.png|Untitled 20 2.png]]
![[/Untitled 21 2.png|Untitled 21 2.png]]
![[/Untitled 22 2.png|Untitled 22 2.png]]
![[/Untitled 23 2.png|Untitled 23 2.png]]
![[/Untitled 24 2.png|Untitled 24 2.png]]
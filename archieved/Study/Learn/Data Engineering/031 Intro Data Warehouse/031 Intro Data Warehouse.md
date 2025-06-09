Operational Databases  
Pros: Excellent for operations, no redundancy, high integrity  
Cons: Too slow for analytics, Too hard to understand  
Data Warehouse: subject-oriented, integrated, nonvolatile, time-variant
## DWH pada konteks bisnis:
- Perhatikan setiap requirement
    - Scaling? Apakah single database cukup?
    - Kompleksitas?
    - Tabular data?
    - Apakah perlu performance yang cepat atau bisa fleksibel?
  
  
#### OLTP vs OLAP
|OLTP|OLAP|
|---|---|
|[[Transactional]]|Analytical|
|[[Performance]]|Perlu banyak query/join|
|[[No redundancy]]|Sulit dipahami|
|[[High integrity]]|As long as can generate analysis|
  
  
## Fact or Dimension Table
- Fact Table biasanya bersifat **numeric & additive** seperti transaksi, order, dll
- Dimension table biasanya merupakan table penjelasan dari attribute pada fact table seperti, departemen, lokasi, karyawan, waktu, dll.
  
ETL → Dimensional model
Tujuan Data Modelling : Agar mudah dipahami dan fast query → **Star Schema**
Dari normalized/OLTP menuju OLAP
  
  
## Data Warehouse Architecture:
**Kimball**  
Standarisasi untuk setiap fungsi bisnis atau departmen  
**Data mart**
- Setiap departemen memiliki ETL dan dimensional model nya masing-masing
- Bisa menimbulkan inkonsistensi, beda departemen beda data
**Inmon's corporate information factory (CIF)**
- Semua data ditampung terlebih dahulu pada bentuk normal (pada ETL), kemudian tiap departmen load ke dimensional model masing-masing yang dibutuhkannya
**Hybrid (Kimbal + Inmon)**
  
### DWH Architecture
### Kimball's Bus Architecture
All sources -> DWH -> Enterprise DW bus architecture
### Independent Data Marts
The department has independent ETL
### Inmon's Corporate Information Factory (CIF)
All sources -> DWH (3NF) -> Datamart
### Hybrid Kimball Bus & Inmon CIF
All sources -> DWH (3NF) -> Enterprise DW bus architecture
  
### OLAP Cubes
Roll-Up: City to Country (Makin simpel)  
Drill-Down: Country to City (Makin banyak)  
Slice: Where City="WHAT"  
Dice: Where City="WHAT" and Month in ["WHAT", ...] and Branch in ["WHAT", ...]  
GROUP by CUBE(movie, branch, month): kombinasi aggregasi dari semuanya, misalnya total, total by movie branch month, total by movie branch, total by movie, etc.
  
**MOLAP**: Pre-aggregate OLAP Cubes ke **non-relational database**  
**ROLAP**: _On the fly_ menggunakan SQL biasa
  
![[/Untitled 35.png|Untitled 35.png]]
![[/Untitled 1 8.png|Untitled 1 8.png]]
![[/Untitled 2 8.png|Untitled 2 8.png]]
![[/Untitled 3 7.png|Untitled 3 7.png]]
![[/Untitled 4 7.png|Untitled 4 7.png]]
![[/Untitled 5 7.png|Untitled 5 7.png]]
![[/Untitled 6 6.png|Untitled 6 6.png]]
![[/Untitled 7 5.png|Untitled 7 5.png]]
![[/Untitled 8 5.png|Untitled 8 5.png]]
![[/Untitled 9 4.png|Untitled 9 4.png]]
![[/Untitled 10 4.png|Untitled 10 4.png]]
![[/Untitled 11 4.png|Untitled 11 4.png]]
![[/Untitled 12 4.png|Untitled 12 4.png]]
![[/Untitled 13 4.png|Untitled 13 4.png]]
![[/Untitled 14 4.png|Untitled 14 4.png]]
![[/Untitled 15 4.png|Untitled 15 4.png]]
![[/Untitled 16 4.png|Untitled 16 4.png]]
![[/Untitled 17 4.png|Untitled 17 4.png]]
![[/Untitled 18 4.png|Untitled 18 4.png]]
![[/Untitled 19 4.png|Untitled 19 4.png]]
![[/Untitled 20 4.png|Untitled 20 4.png]]
![[/Untitled 21 4.png|Untitled 21 4.png]]
![[/Untitled 22 4.png|Untitled 22 4.png]]
![[/Untitled 23 4.png|Untitled 23 4.png]]
![[/Untitled 24 4.png|Untitled 24 4.png]]
![[/Untitled 25 3.png|Untitled 25 3.png]]
![[/Untitled 26 3.png|Untitled 26 3.png]]
![[/Untitled 27 2.png|Untitled 27 2.png]]
![[/Untitled 28 2.png|Untitled 28 2.png]]
![[/Untitled 29 2.png|Untitled 29 2.png]]
![[/Untitled 30 2.png|Untitled 30 2.png]]
![[/Untitled 31 2.png|Untitled 31 2.png]]
![[/Untitled 32 2.png|Untitled 32 2.png]]
![[/Untitled 33 2.png|Untitled 33 2.png]]
![[/Untitled 34 2.png|Untitled 34 2.png]]
![[/Untitled 35 2.png|Untitled 35 2.png]]
![[Untitled 36.png]]
![[Untitled 37.png]]
![[Untitled 38.png]]
![[Untitled 39.png]]
![[Untitled 40.png]]
![[Untitled 41.png]]
![[Untitled 42.png]]
![[Untitled 43.png]]
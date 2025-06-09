---
Created: 2021-06-16T14:00
tags:
  - Backend
  - Software-Engineering
Last edited time: 2025-05-11T09:49
---
# Apa itu API?
Application programming interface, simplenya dalam konteks RestAPI buat kirim-kirim data.
## SOAP VS RESTful
pada SOAP format request dan responsenya sudah ditentukan
  
### GPRC
grpc using golang + java

> [!info] The complete gRPC course [Protobuf + Go + Java]  
> If you're building APIs for your microservices or mobile applications, you definitely want to try gRPC.  
> [https://dev.to/techschoolguru/the-complete-grpc-course-protobuf-go-java-2af6](https://dev.to/techschoolguru/the-complete-grpc-course-protobuf-go-java-2af6)  
## HTTP header, response code,
# HTTP Method
Get
Post
Put
Patch
Delete
  
# URL
http,://google.com:40/path/index.html?key1=val&key2=val2\#Acnhor
protocol, domain, port, path, parameter, anchor
  
# HTTP Message
start line (from requests and response)
http headers (isinya key dan value)
empty line
body (optional)
  
### Resource naming:
Gunakan kata benda  
Gunakan Hirarki  
Gunakan Action pada resource  
Gunakan - dan lowercase  
Gunakan query untuk filter  
  
### Versioning
Pada URL  
Menggunakan HTTP Header  
  
### JSON API
Data  
Relationships  
  
### Cache
Data sementara, dalam RESTful API cache biasanya disimpan di client.
Gunakan HTTP Header Response 'ETag' untuk caching.
Terus Header Response 'If-None-Match'
  
### Istilah
HATEOAS : Content yang menyisipkan url ke link yang berhubungan dengan API itu
Idempotent : Kalo nerima request yang sama berkali", harus dianggap satu request aja
Stateless : State disimpan di client, tidak ada yang disimpan di server
  
### Docummentation ex:
Swagger  
OpenAPI  
  
### Tahapan membuat RESTful API:
Business Flow  
UI/UX Screen  
API Documentation  
Develop RESTful API  
  
# Tips
space jadi '%20' di url
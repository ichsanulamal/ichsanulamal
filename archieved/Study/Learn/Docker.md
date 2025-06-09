---
Created: 2021-07-03T14:23
tags:
  - Tools
Last edited time: 2024-02-21T17:43
---
Client - Docker Host - Registry
### Docker Host
- Docker Daemon
    - Images
    - Containers : instance dari image
  
### Registry buat ngambil image
[hub.docker.com](http://hub.docker.com)
google, aws registry
  
### Images
docker images
docker pull <image:tag_version>
docker image rm <image:tag_version> # Buat remove image
  
### Container
\#list container
docker container ls --all
\#create container
docker container create --name <nama> <image:tag_version> -p <pLuar>:<pThisContainer>
docker container create --name <nama> <image:tag_version> -p 8080:27017
\#delete container
docker container rm <nama> *<nama>
\#start
docker container start <nama>
\#stop
docker container stop <nama> *<nama>
  
  
docker exec -it nama <$command lanjutan>
  
### Buat image sendiri
1. Buat Dockerfile
2. Isi ini
```Docker
FROM golang:1:11:4
COPY main.go /app/main/go
CMD ["go" "run" "/app/main.go"]
```
3. run $ docker build --tag app-golang:<tag>
4. Cek pake docker images
5. Buat push ke repo atau registry
run
$ docker tag nama-image:tag repo/nama-image:tag
$ docker login # kalo belum
$ docker push repo/nama-image:tag
  
### Logs
docker logs  
docker logs <ID>  
contoh:  
docker logs bash  
  
# MySQL Server Remote
[Start a Remote MySQL Server with Docker quickly | by Cun Yang | Medium](https://medium.com/@backslash112/start-a-remote-mysql-server-with-docker-quickly-9fdff22d23fd)
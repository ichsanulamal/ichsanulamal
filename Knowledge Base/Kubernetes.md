---
Created: 2022-01-15T16:59
tags:
  - Devops
Last edited time: 2025-05-11T09:47
---
Kubernetes
## **Alasan perlu Kubernetes:**
- Dari monolith ke microservices
- Dari VM ke container
- Scaling microservices dengan container
## **Arsitektur**
- Masters
    - kube-apiserver : untuk menghubungkan cluster
    - etcd : db
    - kube-scheduler
    - kube-controller
    - cloud controller : setting dengan cloud provider
- Workers
    - kubelet : memastikan aplikasi jalan
    - kube-proxy : load balancer
    - container-manager
  
Script
```Bash
minikube start
kubectl cluster-info
```
local kubernetes on vps
```Bash
# Docker
curl -fsSL https://get.docker.com -o get-docker.sh
chmod +x get-docker.sh
./get-docker.sh
## Post install
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
# Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start
# kubectl
snap install kubectl --classic
kubectl version --client
```
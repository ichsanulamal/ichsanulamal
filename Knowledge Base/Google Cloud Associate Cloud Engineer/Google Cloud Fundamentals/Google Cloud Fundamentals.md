  
![[/Untitled 3.png|Untitled 3.png]]
IaaS → CaaS → PaaS → FaaS
VM instance → GKE → App Engine → Cloud Functions → Cloud Run
  
# storage options
object storage vs block storage
  
cloud storage
storage classes
standard: no limit
nearline: accessed < 1/mo
coldline: accessed < 1/qtr
archieve: accessed < 1/yr
availability
region
dual-region
multi-region
  
filestore: nfs
  
persistent disk
standard
SSD
  
# database
sql
cloud sql
cloud spanner: scalable relational
nosql
bigtable: scalable, high throughput, low latency
datastore: nosql document, app, acid
firestore: realtime, optimized for offline
memorystore: redis, memcached
  
# networking services
vpc
firewall
routes
  
load balancing
https load balancing: across regions
network load balancing: server instances in same region
  
google cloud dns
  
cloud vpn: to VPC through IPsec connection
direct interconnect: to VPC with high quality network
  
direct peering
carrier peering
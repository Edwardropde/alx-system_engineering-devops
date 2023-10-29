#!/bin/bash

User: This is a client or user who wants to access the website www.foobar.com.
Domain (foobar.com): The domain name. It is the human-readable address for accessing the website. 
DNS: The Domain Name System that resolves the domain to the IP addresses of the servers.

HAproxy (Load Balancer): 
This is included to disseminate traffic across various servers enhancing scalability, redundancy, and fault tolerance.
Its distribution algorithm is it utilizes a round-robin distribution algorithm that directs requests to individual servers in a cyclic order

Server 1 (Nginx): It is a web server tasked with handling incoming web requests.
Server 2 (Application Server): An application server executing the website code and handling user requests.
Application Files (Code Base): The website's codebase. It has CSS, JavaScript, HTML, and server-side scripts. It is hosted on Server 2.
MySQL: Manages and stores the website's data, including user data and content. 

Specifics:
Load Balancer (HAProxy).
Helps distribute traffic, enhance fault tolerance, and provide redundancy.
Active-Active Setup: Both Server 1 and Server 2 actively manage user/ client requests. 



Database Primary-Replica Cluster.
MySQL is set as a Primary-Replica (Master-Slave) cluster. The Primary node manages write operations while the Replica node replicates data from the Primary and serves read operations

Difference Between Primary and Replica.
The Primary node handles write operations, ensures data consistency, and is the authoritative source for changes in the database.
The Replica node replicates data from the primary node, serving read operations to offload the Primary, enhancing read performance, and providing data redundancy. 


Issues with the infrastructure.
Single Point of Failure:
The load balancer can become a single point of failure. There is a need to add another load balancer for redundancy. 
Security issues.
The design lacks a firewall or HTTPS. Using security measures like firewalls is important. 
No monitoring.
The infrastructure lacks monitoring and logging which are vital in tracking performance, security, and probable problems. Using monitoring tools and practices for effective maintenance and troubleshooting is vital. 


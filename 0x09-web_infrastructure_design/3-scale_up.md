#!/bin/bash

1 Server: This is the primary machine that hosts the web infrastructure. It is the foundation for other components.
Load Balancer (HAproxy): This is configured to work as a cluster with another HAProxy instance. The primary function is to distribute incoming traffic across multiple backend servers, resulting in better load distribution and high availability. 
Web server: This runs software like Apache and Nginx. It handles incoming HTTP requests and serves static web content like JavaScript, HTML, and CSS. 
Application Server: This executes the website's code and processes dynamic content requests. It often runs server-side scripts and communicates with databases to generate and serve dynamic web pages.

Specifics:
Why a Load Balancer?
This is added to ensure fault tolerance, high availability, and efficient load distribution. It directs traffic to various backend servers optimizing resource utilization

Key considerations:
The difference between web servers and application servers is in the enhanced system performance and scalability. The web server manages static content and acts as a reverse proxy, offloading some of the work from the application server. The application server concentrates on executing code and managing dynamic content, resulting in more efficiency and specialization in the environment used in application processing
The infrastructure design results in improved resource utilization, response time, and scalability. It is common in web architecture to ensure optimal performance in managing static and dynamic content while maintaining high availability and redundancy with load balancing. 
In this scenario, all SPOFs are eliminated and each major component; application server, web server, and database servers, have been placed in separate GNU/Linux servers. The SSL protection is not terminated at the Load Balancer and each server's network is safeguarded by a firewall and they are also monitored. 
The addition of a firewall between each server protects each server from unauthorized and unwanted users instead of protecting one server. 

Issues with the infrastructure
High maintenance cost.
Moving each component to its server means that there is a need to purchase more servers and this would increase the electricity bill.


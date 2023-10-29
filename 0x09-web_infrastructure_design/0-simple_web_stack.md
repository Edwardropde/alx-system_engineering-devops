#!/bin/bash

Server
A Server is a physical or virtual computer dedicated to giving certain resources or services. It hosts the website (www.foobar.com) and its components.

Role of domain name
Domain in name "foobar.com" is the human-readable address used by clients or users to access web browsers, particularly the website the server hosts. It is a pointer to the server's IP address. 

Type of DNS record (www.foobar.com)
"www" in www.foobar.com corresponds to the Canonical Name (CNAME) DNS record. The record connects the "www" subdomain with the "foobar.com" which is the main domain thus pointing to the server's IP address. 

Role of web server.
The Nginx which is the web server is tasked with managing incoming web requests from clients. It is a request handler getting HTTP requests and directing them to the relevant resources on the server. It is the entry point for the user request. 

Role of application server
The application server processes client requests and then executes the website's code. It does application-specific tasks like interacting with the database, running server-side scripts, and generating dynamic content based on user interactions. 

Role of database
The database (MySQL) manages and stores website data. It entails user data, content, and other information needed for the application to work. It helps in data retrieval, storage, and maintenance. 

What server is used to communicate with the user's computer after they request the website? 
The server interacts with the user's computer using the HTTP (Hypertext Transfer Protocol). When a client requests a webpage by keying www.foobar.com on a browser, the server responds with the requested content over HTTP.


Issues with the infrastructure
Single Point of Failure (SPOF).
The server represents a single point of failure in the infrastructure since if it experiences software issues or hardware failure, the entire website will be inaccessible. This can be handled by using failover and redundancy mechanisms. 

Downtime during Maintenance
When there is a need for maintenance like deploying new code, the web server may have to be restarted resulting in downtime. Enforcing approaches like load balancing and redundancy can help mitigate downtime and maintain service availability. 

The infrastructure may experience difficulty handling a sudden increase in traffic. Scaling would be problematic since there is one server. To deal with scalability issues, one can add more server instances, and load balancing, or use cloud-based solutions that enable easy scaling based on demand. 


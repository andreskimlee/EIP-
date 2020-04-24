
# Design Basics 

## Key Characteristics of a distributed system

 1. Scalability - the capability of a system to grow and manage increased demand. (Any system that can evolve in order to support an increasing 
amount of work is considered a scalable system)
    
    Horizontal scaling refers to increasing the amount of servers into your pool of resources '
    
    Vertical scaling refers to increasing the capabilitites of your existing server (More ram, CPU, storage, etc)

Pros and Cons

Vertical scaling has an upper limit (You can only increase serve capabilities by so much) You also have increased down time while vertical scaling.

On the other hand horizontal scaling is more dynamic but in most cases is more expensive. 

Examples of systems that rely on Horizontal scaling : MongoDB, Cassandra (add more machines the more demand you get)
                                 Vertical scaling: MySQL (You can switch to bigger machines but increase downtime )

2. Reliability - a system is considered reliable if one more several of its software/hardware components fail and it is still able to deliver its service. (Generally you achieve this through redundancy. Imagine Amazon's one of their server goes down that contained your shopping cart info. Another server has the same information and with zero downtime is able to procure your cart information.)

3. Availaibility - A percentage of the time the system is up runnning (under normal conditions) IF a system is reliable it is considered available. However an available system is not necessarily reliable. 

4. Efficiency - is defined by the ability of a system to deliver given two metrics. Latency and Bandwidth. 
    Any operation to the distributed data structure will be a function of those two metrics. It is very difficult to calculate a precise cost model accounting all these performance factors (We can only estimate)

5. Serviceability or Manageability - How easy is it to manage the system? Ease of diagnosing an issue? How simple is it to operate? 


# Load Balancing 

A Load balancer helps distribute traffic across a cluster of servers to improve responsiveness and availability of applications/websites/db
It also keeps track of the status of all servers so it knows not to send traffic to a dead server etc.

A load balancer typically sits between the client and server. 

 ![alt-text](https://www.educative.io/api/collection/5668639101419520/5649050225344512/page/5747976207073280/image/5696459148099584.png)

However, it can be added into three places: 
 1. between user and server
 2. between web servers and internal platform layer (like application servers or cache servers)
 3. Between internal platform layer and database 


![alt-text](https://i.imgur.com/w4i1kxd.png)


 The main difference between Web server and application server is that web server is meant to serve static pages e.g. HTML and CSS, while Application Server is responsible for generating dynamic content by executing server side code.

Benefits of a load balancer is the user experiences less interuptions and faster load.

How it operates: 

    A load balancer sends a health check. Ensures servers are "listening" if server is not listening it is removed from its pool of healthy servers the load balancer can send the information to. 

## Algorithims to check back end servers: (Many different Use Case Scenarios )
        1. Least Connection Method - directs traffic to server with fewest connections
        2. Least Response Time - directs traffic to server with fewest connections + lowest average response time
        3. Least Bandwidth - directs traffic to a server with the least amount of traffic measured in mb
        4.Round Robin - Cycles through a list of servers and sends a new request to the next server. (Repeats if it reaches end of the list) Most useful for when the servers have same specifications and there are not many connections
        5. Weighted Round Robin - used for when the servers have different specifications. Larger servers are assigned a larger integer value. and servers with higher integers receive new connections before those with lower numbers.
        6. IP Hash - hash of the IP address of the client is calculated to redirect the request to a server. (Benefit: Network Adapter Redundancy)

## Redundant Load Balancer

    If only a single load balancer exists then it is a huge area for a single failure to disrupt the system. Hence multiple load balancers can exist. A second load balancer monitors the health of the first and any andditional load balancers simply monitors the health of the other load balancers. (Redundancy seems to a good thing and a great fail safe in a distributed system)

![alt-text](https://i.imgur.com/A3d5cuu.png)

# Caching 

Load balancing allows you to scale horizontally. Caching on the other hand allows you to scale by better utilizing the resources you already have. 

### Locality of reference principle: recently requested data is likely to be requested again. 

Caching exists in almost every layer of computing. The easiest way to think about a cache is that it is like a short term memory where it has a limited amount of information but is much faster than accessing 




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

Caching exists in almost every layer of computing. The easiest way to think about a cache is that it is like a short term memory where it has a limited amount of information but is much faster for accessing information (it contains most recently accessed data) Often found near the level closest to the front where they are implemented to return data quickly without taxing downstream levels. 

### Application Server Cache 
    
    A cache that exists directly on the request layer node. Each time a request is made, before querying into back end you can imagine that it checks the cahche if it is already contained. If so it will prematurely return. 

### Content Distribution Network

    CDN are a type of cache when there is a website with a lot of static media. Request is made it will check the CDN if it contains the media, if not it will query to fetch the file then cache it locally, and serve it to the user.

### Cache Invalidation

    Cache stores most recently used however that data SHOULD become invalidated if there is an update to the database modifying that data. Otherwise you can potentially have inconsistent behaviour in your application 

    To solve this issue, there are three different schemes

    1. Write-through-cache : You write to both the cache and the database when applying a change. That way your cache is also consistent. Benefit: your cache will not get loss in case of power loss, etc. Downside is you are writing twice. (More latency) 

    2. Write-around cache : Data is written directly to permanent storage, bypassing the cache. Disadvantage is a cache-miss (Where the data doesnt exist in the cache) and must be read from the slower backend

    3. Write-back cache: only written to the cache and it is not queried into the database until some time has passed

### Cache eviction policies

    FIFO - (First in First Out) simply removes the first block accessed 
    LIFO - (Last in First Out) removes the lost element
    LRU - (Least recently used) - least used gets tossed.
    MRU - (discards most recently) used items first
    LFU - (least frequently used) - Counts how often an item is needed. Those that are used least often are discarded first.
    RR - (random) - self explanatory 


### Data Partitioning

    Data partitioning is the process of breaking up big databases into many smaller parts. (Splitting up a db/table to multiple machines to improve manageability, performance, availability, and load balancing of an application). The justification for data partitioning is that, after a certain scale point, it is cheaper and more feasible to scale horizontally by adding more machines than to grow it vertically by adding beefier servers. 

#### Partitioning Methods

    Horizontal Partitioning: different rows into different tables. For example zipcodes > 10000 are stored in one table. and less than stored in another table. This method is also reffered to as range based partitioning. The flaw in this method comes potentially if you do not choose a data range that is balanced. For example your table stores users that listen to hip hop and rap partitioned by age. Your cut off line is less than 30 and greater than 30. You end up with a unbalanced and inefficient server because the < 30 age group far outweighs the > 30 age group who listen to rap. 

    Vertical Partitioning: Each db server houses its own information for a specific attribute of a schema. For example. A users schema with user info, posts, and photos. One db contains user Info, another a post and so on. The disadvantage is its not a highly scalable system. IF all of a sudden you experience massive growth, you would need to further implement more partitioning for a specific feature. across various servers. 

    Directory Based partitioning: work around issues mentioned in the above schemes is to create a lookup service which knows your current partitioning scheme and abstracts it away from the DB access code. So, to find out where a particular data entity resides, we query the directory server that holds the mapping between each tuple key to its DB server.

### Partitioning Critera 

    a. Key or Hash based partitioning: Under this scheme, we apply a hash function to some key attributes of the entity we are storing; that yields the partition number. For example, if we have 100 DB servers and our ID is a numeric value that gets incremented by one each time a new record is inserted. In this example, the hash function could be ‘ID % 100’, which will give us the server number where we can store/read that record. This approach should ensure a uniform allocation of data among servers. The fundamental problem with this approach is that it effectively fixes the total number of DB servers, since adding new servers means changing the hash function which would require redistribution of data and downtime for the service. A workaround for this problem is to use Consistent Hashing.


    b. List partitioning : each partition is assigned a value. You place into that partition if the value and key pair match.

    c. Round-robin partition: Ensures uniform data distribution. 


### Common Issues with Data partitioning

     Most of these constraints are due to the fact that operations across multiple tables or multiple rows in the same table will no longer run on the same server.

     a. Joins and Denormalization: Performing joins on a database which is running on one server is straightforward, but once a database is partitioned and spread across multiple machines it is often not feasible to perform joins that span database partitions. Such joins will not be performance efficient since data has to be compiled from multiple servers. A common workaround for this problem is to denormalize the database so that queries that previously required joins can be performed from a single table. Of course, the service now has to deal with all the perils of denormalization such as data inconsistency.

     b. Referential integrity : Enforicng foreign keys on a partitioned database can be extremely difficult. 

     c. Rebalancing: The data distribution is not uniform, e.g., there are a lot of places for a particular ZIP code that cannot fit into one database partition.There is a lot of load on a partition, e.g., there are too many requests being handled by the DB partition dedicated to user photos. In such cases, either we have to create more DB partitions or have to rebalance existing partitions, which means the partitioning scheme changed and all existing data moved to new locations. Doing this without incurring downtime is extremely difficult. 

# Indexes 

    An index is a data structure that can be perceived as a table of contents that points us to the location where actual data lives.
    Benefits: Faster look up time. Potential con: It can decrease write performance.(If you are inserting a new item to a database that exists within an index, you not only have to update your database but also your index)

    Case basis: To reiterate, adding indexes is about improving the performance of search queries. If the goal of the database is to provide a data store that is often written to and rarely read from, in that case, decreasing the performance of the more common operation, which is writing, is probably not worth the increase in performance we get from reading.

# Proxies 

    A proxy is an intermediate server between the client and the back end server. 
        Client ---> server --> web --> back-end 

    In essence a proxiy is a piece of software or hardware that acts as an intermediary for requests from clients seeking resources from other servers.

    Another advantage of a proxy server is that its cache can serve a lot of requests. If multiple clients access a particular resource, the proxy server can cache it and serve it to all the clients without going to the remote server.

        Types of proxies 
        1. Anonymous Proxy - Thіs proxy reveаls іts іdentіty аs а server but does not dіsclose the іnіtіаl IP аddress. Though thіs proxy server cаn be dіscovered eаsіly іt cаn be benefіcіаl for some users аs іt hіdes their IP аddress.
        2. Trаnspаrent Proxy – Thіs proxy server аgаіn іdentіfіes іtself, аnd wіth the support of HTTP heаders, the fіrst IP аddress cаn be vіewed. The mаіn benefіt of usіng thіs sort of server іs іts аbіlіty to cаche the websіtes.

    Reverse proxy -- client downloads something and that information seems like it was made by the proxy server instead of a real server. (Thinking about megaupload, etc that hosts pirated content and when you download it you are downloading it from proxy servers maybe?)

# Redundancy and Replication

    Redundancy is the act of duplicating critical components or functions of a system. with the intention of increasing reliability. (Usually you will have duplicate servers for files etc): 

    A rule of thumb. At any point there is ever a single point of failure you want to have redundancy introduced to mitigate that potential point. 


# SQL VS NoSQL
    Key Note: many companies use both relational and non-relational databases because there are case to case uses.

    When should we use SQL vs noSQL?

    When to use SQL :
        
        1. When ACID compliance is important, (When you need to protect the integrity of your database)    
        2. Your data is structured and unchanging (recall schemas are generally fixed in order to make any change to the schema you have to drop the whole database)

    When to use NoSQL: 

        1. Storing large volumes of data with little to no structure. A NoSQL database sets no limits on the types of data we can store together and allows us to add new types as the need changes. 

        2. Making the most of cloud computing and storage. Cloud-based storage is an excellent cost-saving solution but requires data to be easily spread across multiple servers to scale up.

        3. Rapid development! You dont have to drop your whole database every time you need to make a change to your schema


# Cap Theorem 

    CAP theorem states that it is impossible for a distributed software system to simultaneously provide more than two out of three of the following guarantees (CAP): Consistency, Availability, and Partition tolerance. When we design a distributed system, trading off among CAP is almost the first thing we want to consider. CAP theorem says while designing a distributed system we can pick only two of the following three options: 

    Consistency: All nodes see the same data at the same time. Consistency is achieved by updating several nodes before allowing further reads.

    Availability: Every request gets a response on success/failure. Availability is achieved by replicating the data across different servers.

    Partition tolerance: The system continues to work despite message loss or partial failure. A system that is partition-tolerant can sustain any amount of network failure that doesn’t result in a failure of the entire network. Data is sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages.  


# System Design Step By Step Guide.

### 1. Step 1: Clarify requirements. By clarifying early on and clearing up any ambiguity, you save the risk of not answering the question 
    incorrectly or having to make major adjustments to fit the requirement. 
        
        Some Example questions: Do I have to implement xyz features. What pages can we predict to have. 

### 2. Step 2: Estimate the scale of the system.
               * Approximately how many tweets in our twitter, number of users, etc
               * How Much Storage Will We Need? 
               * What network bandwidth usage are we expecting? This will be crucial in deciding how we will manage traffic and balance load between servers.

### 3. System Interface definition 
        Define what APIs are going to be needed for the system. Example of what that looks like: 
            postTweet(user_id, tweet_data, tweet_location, user_location, timestamp, …)  
        
### 4. Define the data model 
        Define your schema 
            User: UserID, Name, Email, DoB, CreationData, LastLogin, etc.
            Tweet: TweetID, Content, TweetLocation, NumberOfLikes, TimeStamp, etc.
            UserFollowow: UserdID1, UserID2
            FavoriteTweets: UserID, TweetID, TimeStamp
        
### 5. High Level design
        Draw 5 or 6 blocks to represent core elements in your system. (Implement all components that will be needed to solve all requirements before digging into the finer details)

        For Twitter you would need multiple application servers to serve all read/write requests. and have a load balancer to direct traffic to servers. 

        Back-end you'd need a highly efficient database.

        You would also need a distributed file storage system. for photos and videos

![alt-text](https://www.educative.io/api/collection/5668639101419520/5649050225344512/page/5684049913839616/image/5127881690710016.png)

### Step 6 Detailed Design 

        Dig deeper into two or three major components; interviewer’s feedback should always guide us to what parts of the system need further discussion. 

### Step 7: Identifying and resolving bottlenecks   

    Bottle necks are areas in our distributed system that can potentially have a major negative impact on our total output.

    Questions to answer:
        1. Is there any single point of failure in our system? What are we doing to mitigate it?
        2. Do we have enough replicas of the data so that if we lose a few servers, we can still serve our users?
        3. Similarly, do we have enough copies of different services running such that a few failures will not cause total system shutdown?
        4. How are we monitoring the performance of our service? Do we get alerts whenever critical components fail or their performance degrades?

 topics to review : Cap Theorem , NoSQL vs Sql, 


# Sys Design Extra 

    Questions to Think About For Sys Design Starting  

    1. Is this program read heavy or write heavy
    2. Given requirements use CAP theorem. 


    Questions to ask on schema

    1. constraints on length or size of an attribute?
    2. 

## Designing DropBox Key Points    

1 . Microservicing of Servers: 
    Servers if you expect high amounts of volume can abstract or do seperations of concerns where each server has a role. 
    Block Server : the role of getting the file uploading it to S3 and returnibng the src url.
    Metadata server: all metadata (filename, size, date created, etc ) posts to server.
    Synchronization server: beghaves like  a service where it compares information on the metadata server to the clients local storage if it is it will do a rewrite to keep data updated.

    Storage breaks down into two types 

    Metadata - stores a files name, etc all metadata

    cloud storage - stores the actual file 

2.  Chunks : files can be split into chunks where only the modified chunk will update the file. For example, lets say as a user you modify a file. Instead of replacing the whole file when you update it, it should only modify the chunk of the file that has been changed. 

3. Try to abstract as much as possible in terms of different tasks (For example, in the case of dropBox we need four different services from the clients end) 

    a. Internal metadata database - will keep track of all the files and their versions
    b. Chunker - splits files into chunks only updates modified chunks
    c. Watcher - will monitor local storage for changes for when user update create delete etc. 
    d. Indexer - update the internal metadata with information about the chunks modified files. 

4. Message queuing service 

    A middleware that exists to keep order. Ex: have 5 people sharing/editing a file. You do not want conflicts with edits so you should keep a queue system to keep order in place. 



## Designing Youtube
 
1. Schema

    Video : 
        id
        title,
        description
        uploader => userId
        likes
        dislikes
        views

    Comments: 
        belongs to video id => videoID
        commentId
        UserId
        actual comment

    User
        name email etc

2. High level overview. For videos specifically you want to use an encoder. Now what an encoder does is essentially takes whatever the user uploaded and encodes the video so that it becomes accessible in the browser. Common formats include mp4 WMV, etc. As with sites that have media files, you can use a object storage such as S3 and also in the database you can have a metadata database along with the user database. Also the use of a processing queue will be effective here, (order matters first come first start upload you dont want a user who started later having a faster upload etc) (Remember a processing queue is really essential for when order matters)


Metadata sharding -> sharding the metadata database you can shard by videoID

you can use a cache for more popular videos.

---- Questions you should ask in System design Interview --- 

1. what are the functional requirements  + non functional requirements 


3. Content Delivery Network (used for sites servign large amounts of static media) - CDN will store popular videos in the case of youtube for that specific region or geography and serve that content if it in that content. 


Availability is achieved by replicating the data across different servers.
Consistency is achieved by updating several nodes before allowing further reads.


reliability = the probability of a system going down will continue to operate even with a part that does not work. 

Master-slave relationship for the database, to ensure high reliability. availability can be accomplished by creating duplicate 


Availability --> Achieved through redundancy

Recall - Consistent hashing allows us to distribute data across a cluster in such a way that will minimize reorganization 

THEY WILL INTENTIONALLY BE AMBIGUOUS ASK AS MANY QUESTIONS AS POSSIBLE!





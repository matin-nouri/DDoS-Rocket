![DDoS Rocket](https://cyberhoot.com/wp-content/uploads/2022/02/DdoS-1024x768.jpeg)

# DDoS Rocket
What about a Rocket Launcher which attack machines using Socket?
This Program uses the DoS/DDoS technique and Socket Flood for harming servers.

 ## What is DoS/DDoS Attack?
 In computing, a denial-of-service attack (DoS attack) is a cyber-attack in which the perpetrator seeks to make a machine or network resource unavailable to its intended users by temporarily or indefinitely disrupting services of a host connected to a network. Denial of service is typically accomplished by flooding the targeted machine or resource with superfluous requests in an attempt to overload systems and prevent some or all legitimate requests from being fulfilled. The range of attacks varies widely, spanning from inundating a server with millions of requests to slow its performance, overwhelming a server with a substantial amount of invalid data, to submitting requests with an illegitimate IP address. 
In a distributed denial-of-service attack (DDoS attack), the incoming traffic flooding the victim originates from many different sources. More sophisticated strategies are required to mitigate this type of attack; simply attempting to block a single source is insufficient as there are multiple sources. A DoS or DDoS attack is analogous to a group of people crowding the entry door of a shop, making it hard for legitimate customers to enter, thus disrupting trade and losing the business money. Criminal perpetrators of DoS attacks often target sites or services hosted on high-profile web servers such as banks or credit card payment gateways. Revenge and blackmail, as well as hacktivism, can motivate these attacks. [1]

 ## What is Socket?
A network socket is a software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network. The structure and properties of a socket are defined by an application programming interface (API) for the networking architecture. Sockets are created only during the lifetime of a process of an application running in the node.
Because of the standardization of the TCP/IP protocols in the development of the Internet, the term network socket is most commonly used in the context of the Internet protocol suite, and is therefore often also referred to as Internet socket. In this context, a socket is externally identified to other hosts by its socket address, which is the triad of transport protocol, IP address, and port number.
The term socket is also used for the software endpoint of node-internal inter-process communication (IPC), which often uses the same API as a network socket. [2]

 ## Differences Between TCP/UDP:
![TCP vs UDP[3]](https://media.geeksforgeeks.org/wp-content/uploads/20230406112559/TCP-3.png)

 ## Installing
 For Posix systems:
 ```
 git clone https://github.com/matin-nouri/DDoS-Rocket
 cd DDoS-Rocket-master
 sudo chmod +777 *
 ./installer.sh
 ```
 For NT systems:
1. Download ZIP File and extract it
2. install python from python.org
3. run installer.bat



# Refrences
1. Wikipedia, DDoS https://en.wikipedia.org/wiki/Denial-of-service_attack
2. Wikipedia, Network Socket https://en.wikipedia.org/wiki/Network_socket
3. GFG Solution


![Screenshot (208)](https://github.com/maramilod/alx-system_engineering-devops/assets/63783592/b9cd5e02-2c2f-4c2f-900f-66709c08e292)

<h3>This web infrarchitecture relies on distributing the traffic or the users that coming from another network
across the primary and replica servers, and this is achieved through a load balancer device.</h3>

<h2>  What distribution algorithm your load balancer is configured with and how it works </h2>

Round Robin algorithm evenly distributes incoming requests from an external network among multiple servers.
It ensures fair and organized workload distribution, optimizing resource utilization and improving system performance.
 It is a simple and effective load balancing technique commonly used in network environments.

<h2> Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both </h2>

In this architecture, an active-passive strategy is employed, the difference is,
In an active-active setup, multiple active devices are utilized, so when one device fails, the others continue to provide the service. 
On the other hand, in an active-passive configuration, there are two servers, one being active and the other in a standby mode,
ready to take over in case of a failure of the active server.

<h2> How a database Primary-Replica (Master-Slave) cluster works </h2>

When a write operation is performed on the primary node (the main server), the data is synchronized between the primary node and the replica server.
This means that the newly written data on the primary node will also be transferred to the replica server and made available for read operations.
In summary, the replica server is responsible for read operations only, while the primary server handles write operations.

<h2> What is the difference between the Primary node and the Replica node in regard to the application </h2>

The primary node is responsible for handling all the write operations required by the system, while the replica server is capable of processing read operations.
This distribution of tasks helps reduce the traffic load on the primary node, as the replica server can handle the read requests,allowing the primary node to focus on write-intensive tasks.
This architecture improves the overall performance and scalability of the system,
ensuring efficient data access and minimizing bottlenecks.

<h1>The Issues</h1>

<h2>- Where are SPOF </h2>

 if the database server fails, the network will collapse, including the load balancer device that is connected to two networks. If the load balancer fails, the network will also collapse.
Additionally, the application itself is considered a Single Point of Failure (SPOF).

<h2>- Security Issues (no firewall, no HTTPS)</h2>
the network becomes directly vulnerable to hacking, data theft, or network disruption. It becomes extremely easy for any attacker to exploit the network and gain unauthorized access to sensitive data or simply disrupt the network's functionality.

<h2>- No monitoring </h2>

Without monitoring, we will not be able to detect faults, identify the status of servers, or gather information about their performance and health. Monitoring plays a crucial role in providing real-time visibility into the network infrastructure, allowing us to proactively identify issues,
troubleshoot problems, and ensure the overall reliability and availability of the system.

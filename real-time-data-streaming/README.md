![1715143246055](image/README/1715143246055.png)

# Real time Data Streaming Pipeline.

A real time streaming pipeline using Apache spark, Kafka, Cassandra, Airflow and PostgreSQL.

[Kafka](https://kafka.apache.org/documentation/ "Kafka Documentation"), [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html "Airflow Documentation"), [Cassandra](https://cassandra.apache.org/doc/latest/ "Cassandra Documentation"), [Spark](https://spark.apache.org/docs/latest/api/python/getting_started/index.html "Spark Documentation")

### How kafka and Zookeeper work together?
* Zookeeper is used to manage and coordinate kafka's broker nodes, handle leader elections for partitions, and maintain configuraion information.
  * **Broker Management**:
    * **Broker Registration**: When a kafka broker starts, it registers itself with the ZooKeeper. Zookeeper maintains a list of all the live kafka brokers in the cluster.
    * **Leader Election**: 
      * **Partition Leadership**: Each partition in kafka has a designated leader that handles all read and write requests for that partition. Zookeeper manages the election of partition leaders.
    * **Configuration Management**: 
      * **Topic configuration**: Zookeeper stores metadata about kafka topics, including the number of partitions, replication factor, and configuration overrides.
    * **Controller Election**: 
      * **Cluster controller**: One of the kafka brokers act as the controller, which is resposibile for administrative tasks such as managaing partition reassignments and monitoring broker failures.
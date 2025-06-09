6.0.1-Introduction
- Introduction to stream processing and Kafka
- Role of Kafka in stream processing
- Specific configuration parameters for Kafka
- Understanding Kafka producers and consumers
- Programmatic data consumption and production in Kafka
- Partitioning in stream processing
- Working examples with Kafka streams in Java
- Setting up Spark streaming with Python examples
- Importance of schema in stream processing
- Overview of Kafka Connect and case equal DB
  
6.0.2-What is stream processing
- Before diving into steam processing, let's understand what data Exchange is.
- In computer communication, we often refer to APIs like REST, GraphQL, and webhooks for data sharing.
- In the real world, a notice board serves as a simple form of data Exchange.
- Consumers passing by a notice board can read, react, or ignore the information posted by producers.
- Consumers interested in specific topics, like Kafka, Spark, Stream Processing, and Big Data, can target their data exchanges accordingly.
- Let's explore data Exchange in stream processing, a more dynamic form of information sharing.
- Unlike batch processing, stream processing enables real-time data exchanges.
- In this scenario, data is shared and received almost instantly.
- Real-time doesn't mean instantaneously, but it involves only a few seconds of delay, significantly faster than batch processing.
- It's not at the speed of light, but it's a vast improvement in data exchange speed compared to traditional batch processing.
  
6.3-What is kafka?
- We've covered data exchange and its significance in student processing.
- Exploring Kafka streaming and its role in our notice board example.
- Introducing ABC and XYZ topics along with their producers and consumers.
- Understanding the critical concept of a 'topic' in Kafka architecture.
- Understanding Kafka's message structure: key, value, and timestamp.
- Key attributes that make Kafka popular: robustness, flexibility, and scalability.
- As microservices grow, a consistent message pass or streaming service becomes essential.
- Kafka facilitates communication between microservices and central databases.
- Kafka's Change Data Capture (CDC) enables seamless interaction between databases and microservices.
  
6.4-Confluent cloud
- Setting up Conflict Cloud free trial for Kafka cluster.
- Free for 30 days, no need for credit or debit card.
- Easy setup without financial information.
- Signing up grants a 30-day free trial.
- Choosing Google Cloud Frankfurt for proximity.
- Demonstrating message production in Kafka.
- Observing message processing in real-time.
- Reviewing message keys and values in Kafka.
- Creating a dummy connector for generating data.
- Monitoring auto connector and data production in Kafka.
  
6.5-Kafka producer consumer
- Creating a Topic for Rights Data
- Topic Created Without Messages or Schema
- Configuring Java Client for Kafka Connection
- Setting up Java Constructor and Properties for Kafka Connection
- Configuring Kafka Producer with Serialization for Rights Data
- Using the Created Topic for Publishing Rights Data
- Successfully Producing Messages to Kafka
- Creating a Java Consumer for Consuming Messages
- Troubleshooting the Consumer Configuration
- Successfully Consuming Messages from Kafka
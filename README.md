# Kafka Example using Python

## Quick Start

### Initial menu

| Options | Description |
|--|--|
| 1 | Producer |
| 2 | Consumer |
| 3 | Exit |

### Kafka Producer

A producer is the one which publishes or writes data to the topics within different partitions.

### Kafka Consumer

Kafka consumers are typically part of a consumer group . When multiple consumers are subscribed to a topic and belong to the same consumer group, each consumer in the group will receive messages from a different subset of the partitions in the topic.

### Requirements

* Kafka
* Zookeeper

### Run

```console
$ cd kafka/
$ bin/kafka-console-producer.sh --broker-list 172.18.0.3:9092 --topic test-docker
$ bin/kafka-console-consumer.sh --bootstrap-server 172.18.0.3:9092 --topic test-docker --from-beginning
```

### Contributing

* [Blog: marceloweb.info](https://marceloweb.info)

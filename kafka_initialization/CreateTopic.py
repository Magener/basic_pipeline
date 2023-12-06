from confluent_kafka.admin import AdminClient, NewTopic

from kafka.consts import KAFKA_BROKER_URL

admin_client = AdminClient({
    "bootstrap.servers": KAFKA_BROKER_URL
})

topic_list = []
topic_list.append(NewTopic("test", 1, 1))
admin_client.create_topics(topic_list)
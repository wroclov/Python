"""
E-commerce Order Processing with Apache Kafka
Demonstrates producer and consumer patterns for order events
"""

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
import json
import time
from datetime import datetime
import random

# Configuration
KAFKA_BROKER = 'localhost:9092'
ORDERS_TOPIC = 'orders'
NOTIFICATIONS_TOPIC = 'notifications'


class OrderProducer:
    """Produces order events to Kafka"""

    def __init__(self, bootstrap_servers):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            acks='all',  # Wait for all replicas to acknowledge
            retries=3
        )

    def send_order(self, order_data):
        """Send an order event to the orders topic"""
        try:
            future = self.producer.send(ORDERS_TOPIC, value=order_data)
            record_metadata = future.get(timeout=10)
            print(f"✓ Order sent: {order_data['order_id']}")
            print(f"  Topic: {record_metadata.topic}")
            print(f"  Partition: {record_metadata.partition}")
            print(f"  Offset: {record_metadata.offset}")
            return True
        except KafkaError as e:
            print(f"✗ Failed to send order: {e}")
            return False

    def close(self):
        self.producer.close()


class OrderProcessor:
    """Consumes orders and processes them"""

    def __init__(self, bootstrap_servers, group_id):
        self.consumer = KafkaConsumer(
            ORDERS_TOPIC,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',  # Start from beginning if no offset
            enable_auto_commit=True
        )

        self.notification_producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def process_orders(self):
        """Process incoming orders"""
        print(f"\n🔄 Starting order processor (Group: {self.consumer.config['group_id']})")
        print("Waiting for orders...\n")

        try:
            for message in self.consumer:
                order = message.value
                print(f"📦 Processing order: {order['order_id']}")
                print(f"   Customer: {order['customer_name']}")
                print(f"   Items: {order['items']}")
                print(f"   Total: ${order['total']:.2f}")

                # Simulate processing
                time.sleep(1)

                # Send notification
                notification = {
                    'order_id': order['order_id'],
                    'customer_name': order['customer_name'],
                    'status': 'confirmed',
                    'timestamp': datetime.now().isoformat()
                }

                self.notification_producer.send(NOTIFICATIONS_TOPIC, value=notification)
                print(f"   ✓ Notification sent\n")

        except KeyboardInterrupt:
            print("\n⏹ Stopping processor...")
        finally:
            self.close()

    def close(self):
        self.consumer.close()
        self.notification_producer.close()


def generate_sample_order():
    """Generate a sample order for demonstration"""
    products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']
    names = ['Alice Smith', 'Bob Jones', 'Carol White', 'David Brown']

    order_id = f"ORD-{random.randint(1000, 9999)}"
    items = random.sample(products, random.randint(1, 3))

    return {
        'order_id': order_id,
        'customer_name': random.choice(names),
        'items': items,
        'total': round(sum(random.uniform(20, 500) for _ in items), 2),
        'timestamp': datetime.now().isoformat()
    }


def demo_producer():
    """Demo: Send sample orders"""
    print("=" * 60)
    print("KAFKA PRODUCER DEMO - Sending Orders")
    print("=" * 60 + "\n")

    producer = OrderProducer(KAFKA_BROKER)

    try:
        # Send 5 sample orders
        for i in range(5):
            order = generate_sample_order()
            producer.send_order(order)
            time.sleep(0.5)
    finally:
        producer.close()


def demo_consumer():
    """Demo: Process orders"""
    print("=" * 60)
    print("KAFKA CONSUMER DEMO - Processing Orders")
    print("=" * 60)

    processor = OrderProcessor(KAFKA_BROKER, group_id='order-processors')
    processor.process_orders()


if __name__ == "__main__":
    import sys

    print("\n🚀 Kafka Order Processing System\n")
    print("Make sure Kafka is running on localhost:9092")
    print("\nOptions:")
    print("  python script_kafka.py producer  - Send sample orders")
    print("  python script_kafka.py consumer  - Process orders")

    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode == 'producer':
            demo_producer()
        elif mode == 'consumer':
            demo_consumer()
        else:
            print(f"\n❌ Unknown mode: {mode}")
    else:
        print("\n⚠️  Please specify mode (producer or consumer)")

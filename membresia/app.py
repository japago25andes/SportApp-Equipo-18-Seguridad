from datetime import datetime
from flask import Flask
import redis
import random
import json

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, db=0)


@app.route('/health', methods=['GET'])
def health_check():
    if random.randint(1, 100) <= 10:
        status = 'down'
    else:
        status = 'up'
    
    message = json.dumps({'service': 'membresia', 'status': status})
    redis_client.publish('health_checks', message)
    return "Health status updated"


def handle_membresia(message):
    data = json.loads(message['data'])
    service_name = 'membresia'
    uuid = data['uuid']
    start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = json.dumps({'service': service_name, 'uuid': uuid,
                          'start_date': start_date})
    redis_client.publish('deportista_menbresia', message)


def listen_for_membresia():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'membresia': handle_membresia})
    print("Starting to listen on 'membresia' channel...")
    pubsub.run_in_thread(sleep_time=0.001)



if __name__ == '__main__':
    print("Llegue aqui")
    listen_for_membresia()
    app.run(debug=True, host='0.0.0.0', port=5004)
    
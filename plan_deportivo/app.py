from flask import Flask
import redis
import random
import json
from datetime import datetime
app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.route('/health', methods=['GET'])
def health_check():
    if random.randint(1, 100) <= 10:
        status = 'down'
    else:
        status = 'up'
    
    message = json.dumps({'service': 'plan_deportivo', 'status': status})
    redis_client.publish('health_checks', message)
    return "Health status updated"

def handle_plan_deportivo(message):
    data = json.loads(message['data'])
    service_name = 'plan_deportivo'
    uuid = data['uuid']
    start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = json.dumps({'service': service_name, 'uuid': uuid,
                          'start_date': start_date})
    redis_client.publish('deportista_plan_deportivo', message)


def listen_for_plan_deportivo():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'plan_deportivo': handle_plan_deportivo})
    print("Starting to listen on 'plan_deportivo' channel...")
    pubsub.run_in_thread(sleep_time=0.001)


if __name__ == '__main__':
    listen_for_plan_deportivo()
    app.run(debug=True, host='0.0.0.0', port=5000)

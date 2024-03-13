from flask import Flask
import redis
import random
import json
import uuid
from datetime import datetime

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, db=0)
cont = 0


@app.route('/health', methods=['POST'])
def health_check():
    if random.randint(1, 100) <= 10:
        status = 'down'
    else:
        status = 'up'

    message = json.dumps({'service': 'deportistas', 'status': status})
    #redis_client.publish('health_checks', message)
    return "Health deportistas status updated"


@app.route('/crear_deportistas', methods=['post'])
def crear_deportistas():
    message = json.dumps({'service': "deportistas",
                          'uuid': str(uuid.uuid4()),
                          'start_date':
                          datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    redis_client.publish('create', message)
    redis_client.publish('membresia', message)
    redis_client.publish('plan_deportivo', message)
    redis_client.publish('servicios', message)

    return {"status": "en proceso", "id": message}


def handle_deportista_membresia(message):
    global cont
    data = json.loads(message['data'])
    service_name = 'membresia'
    uuid = data['uuid']
    start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = json.dumps({'service': service_name, 'uuid': uuid,
                          'start_date': start_date})
    cont += 1
    redis_client.publish('deportista_menbresia_db', message)
    print(str(cont))


def listen_for_deportista_membresia():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'deportista_menbresia': handle_deportista_membresia})
    print("Starting to listen on 'deportista_menbresia' channel...")
    pubsub.run_in_thread(sleep_time=0.001)


def handle_deportista_plan_deportivo(message):
    global cont
    data = json.loads(message['data'])
    service_name = 'plan_deportivo'
    uuid = data['uuid']
    start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = json.dumps({'service': service_name, 'uuid': uuid,
                          'start_date': start_date})
    cont += 1
    redis_client.publish('deportista_plan_deportivo_db', message)
    print(str(cont))


def listen_for_deportista_plan_deportivo():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'deportista_plan_deportivo':
                        handle_deportista_plan_deportivo})
    print("Starting to listen on 'deportista_plan_deportivo' channel...")
    pubsub.run_in_thread(sleep_time=0.001)


def handle_deportista_servicios(message):
    global cont
    data = json.loads(message['data'])
    service_name = 'servicios'
    uuid = data['uuid']
    start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = json.dumps({'service': service_name, 'uuid': uuid,
                          'start_date': start_date})
    cont += 1
    redis_client.publish('deportista_servicios_db', message)
    print(str(cont))


def listen_for_deportista_servicios():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'deportista_servicios': handle_deportista_servicios})
    print("Starting to listen on 'deportista_servicios' channel...")
    pubsub.run_in_thread(sleep_time=0.001)


if __name__ == '__main__':
    #listen_for_deportista_membresia()
    #listen_for_deportista_plan_deportivo()
    #listen_for_deportista_servicios()
    app.run(debug=True, host='0.0.0.0', port=5002)

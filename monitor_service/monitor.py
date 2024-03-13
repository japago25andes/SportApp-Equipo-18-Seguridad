import redis
import sqlite3
import json

redis_client = redis.Redis(host='redis', port=6379, db=0)

conn = sqlite3.connect('monitoring.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS service_status
             (service_name TEXT, status TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()
c.close()

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS monitoring
             (service_name TEXT, uuid TEXT,
          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
              PRIMARY KEY (service_name, uuid, timestamp))''')             

conn.commit()
c.close()



def handle_message(message):
    data = json.loads(message['data'])
    service_name = data['service']
    status = data['status']
    c = conn.cursor()
    c.execute("INSERT INTO service_status (service_name, status) VALUES (?, ?)", (service_name, status))
    conn.commit()
    c.close()
    

def listen_for_health_checks():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'health_checks': handle_message})
    print("Starting to listen on 'health_checks' channel...")
    pubsub.run_in_thread(sleep_time=0.001)


def handle_create(message):
    data = json.loads(message['data'])
    service_name = data['service']
    uuid = data['uuid']
    start_date = data['start_date']
    try:
        c = conn.cursor()
        c.execute("INSERT INTO monitoring (service_name, uuid, timestamp) VALUES (?, ?, ?)", (service_name, uuid, start_date))
        conn.commit()
    except sqlite3.Error as e:
        #conn.rollback()  # Si hay algún error, hacemos rollback para deshacer la transacción.
        print("Error en la inserción:", e)
    finally:
        c.close()


def listen_for_create():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'create': handle_create})
    print("Starting to listen on 'create' channel...")
    pubsub.run_in_thread(sleep_time=0.001)



def handle_deportista_menbresia_db(message):
    print('{}'.format(message['data']))
    data = json.loads(message['data'])
    service_name = data['service']
    uuid = data['uuid']
    start_date = data['start_date']
    
    try:
        c = conn.cursor()
        c.execute("INSERT INTO monitoring (service_name, uuid, timestamp) VALUES (?, ?, ?)", (service_name, uuid, start_date))
        conn.commit()
    except sqlite3.Error as e:
        #conn.rollback()  # Si hay algún error, hacemos rollback para deshacer la transacción.
        print("Error en la inserción:", e)
    finally:
        c.close()
    

def listen_for_deportista_menbresia_db():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'deportista_menbresia_db': handle_deportista_menbresia_db})
    print("Starting to listen on 'deportista_menbresia_db' channel...")
    pubsub.run_in_thread(sleep_time=0.001)


def handle_deportista_plan_deportivo_db(message):
    print('{}'.format(message['data']))
    data = json.loads(message['data'])
    service_name = data['service']
    uuid = data['uuid']
    start_date = data['start_date']
    
    try:
        c = conn.cursor()
        c.execute("INSERT INTO monitoring (service_name, uuid, timestamp) VALUES (?, ?, ?)", (service_name, uuid, start_date))
        conn.commit()
    except sqlite3.Error as e:
        print("Error en la inserción:", e)
      #  conn.rollback()  # Deshacer la transacción en caso de error
    finally:
        c.close()
    

def listen_for_deportista_plan_deportivo_db():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'deportista_plan_deportivo_db': handle_deportista_plan_deportivo_db})
    print("Starting to listen on 'deportista_plan_deportivo_db' channel...")
    pubsub.run_in_thread(sleep_time=0.001)


def handle_deportista_servicios_db(message):
    print('{}'.format(message['data']))
    data = json.loads(message['data'])
    service_name = data['service']
    uuid = data['uuid']
    start_date = data['start_date']
    try:
        c = conn.cursor()
        c.execute("INSERT INTO monitoring (service_name, uuid, timestamp) VALUES (?, ?, ?)", (service_name, uuid, start_date))
        conn.commit()
    except sqlite3.Error as e:
        #conn.rollback()  # Si hay algún error, hacemos rollback para deshacer la transacción.
        print("Error en la inserción:", e)
    finally:
        c.close()
    

def listen_for_deportista_servicios_db():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(**{'deportista_servicios_db': handle_deportista_servicios_db})
    print("Starting to listen on 'deportista_servicios_db' channel...")
    pubsub.run_in_thread(sleep_time=0.001)

if __name__ == '__main__':
    listen_for_health_checks()
    listen_for_create()
    listen_for_deportista_menbresia_db()
    listen_for_deportista_plan_deportivo_db()
    listen_for_deportista_servicios_db()
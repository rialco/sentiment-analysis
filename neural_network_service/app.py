import time
from redis import Redis
from os import environ

stream_key = 'events'


def waitForServices():
    time.sleep(5)
    print('(INFO) Neural network service starting...')
    connection = connect_to_redis()
    get_data(connection)


def connect_to_redis():
    hostname = environ.get('REDIS_HOST', 'redis')
    port = environ.get('REDIS_PORT', 6379)
    r = Redis(host=hostname, port=port, retry_on_timeout=True, db=0)
    return r


def get_data(redis_connection):
    last_id = 0
    sleep_ms = 5000
    while True:
        try:
            resp = redis_connection.xread(
                {stream_key: b"$"}, count=1, block=sleep_ms)
            if resp:
                key, messages = resp[0]
                last_id, data = messages[0]
                print('REDIS ID: ', last_id)
                print('            --> ', data)
        except ConnectionError as e:
            print('(ERROR)Error redis connection: {}'.format(e))
        except:
            print('What happened')


if __name__ == '__main__':
    waitForServices()

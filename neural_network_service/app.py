import time
from redis import Redis
from os import environ
import sqlalchemy as db

from model import Model

stream_key = 'events'


def waitForServices():
    model = Model()
    print('(INFO) ==> Neural network service starting...')
    redisConnection = connect_to_redis()
    postgreConnection, table, aTable = connect_to_postgres()

    listen_to_redis_stream(
        redisConnection, postgreConnection, table, aTable, model)


def connect_to_redis():
    hostname = environ.get('REDIS_HOST', 'redis')
    port = environ.get('REDIS_PORT', 6379)
    r = Redis(host=hostname, port=port, retry_on_timeout=True, db=0)
    return r


def connect_to_postgres():
    engine = db.create_engine(
        'postgresql+psycopg2://pf:pf@postgres:5432/sentiments')
    connection = engine.connect()
    metadata = db.MetaData()
    tweetsTable = db.Table(
        'tweets', metadata, autoload=True, autoload_with=engine)
    tweetsAnalysis = db.Table('tweets_analysis', metadata,
                              autoload=True, autoload_with=engine)
    return connection, tweetsTable, tweetsAnalysis


def listen_to_redis_stream(redis_connection, postgre_connection, tweets_table, analysis_table, nn):
    last_id = 0
    sleep_ms = 5000
    while True:
        try:
            resp = redis_connection.xread(
                {stream_key: "$"}, count=1, block=sleep_ms)
            if resp:
                key, messages = resp[0]
                last_id, data = messages[0]
                print('REDIS ID: ', last_id)
                print('            --> ', data)
                for k, v in data.items():
                    print('Mencion: ', v.decode())
                    query = db.select([tweets_table.columns.id, tweets_table.columns.cleaned_content]).where(
                        tweets_table.columns.mention == v.decode())
                    resultProxy = postgre_connection.execute(query)
                    num_results = resultProxy.rowcount
                    if int(num_results) > 0:
                        resultSet = resultProxy.fetchall()
                        analysis_result = nn.analyze_results(resultSet)
                        upsert_query = db.insert(analysis_table)
                        postgre_connection.execute(
                            upsert_query, analysis_result)
        except ConnectionError as e:
            print('(ERROR) ==> Failed to connec to redis: ', format(e))
        except:
            print('(ERROR) ==> internal error...')


if __name__ == '__main__':
    waitForServices()

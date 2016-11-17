from influxdb import InfluxDBClient
import random
import time

host='localhost'
port=8086
#user = 'root'
#password = 'root'
dbname = 'testDB'


client = InfluxDBClient(host=host,port=port,database=dbname)

def writeInflux():
    i=0 
    n=15
    tokenList= ['abcd','bcde', 'cdef']
    hostList = ['kafka', 'fluentd', 'storm']
    while i<n:
        json_body = [
            {
                "measurement": "testing",
                "tags": {
                    "host": hostList[random.randrange(0,3,1)],
                    "token": tokenList[random.randrange(0,3,1)]
                    },
      #             "time": int(time.time()),
                   "fields": {
                   "byte": 2*random.randint(10,100),
                   "byte_rate": 0.1*random.randint(2,10),
                   "count": random.randint(1,10),
                   "count_rate":0.01*random.randint(3,8)
                   }
            }
        ]
        i=i+1
        client.write_points(json_body)
        time.sleep(5)            
    
writeInflux()

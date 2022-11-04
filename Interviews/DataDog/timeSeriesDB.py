"""
1. You are given the list of logs of HTTP requests in the given format:
[IP, HTTP Verb, status, response time, size, request time]
Write the code to answer the various queries. For example, list all HTTP requests for the last 2 months or show all requests with 200 status, etc.
Interviewer changes the query structure frequently and you should answer how you are going to attack that particular query.
In the end, after the discussion of the pros and cons of different approaches you need to code that.
"""

import sqlite3
queryCreateTable = """CREATE TABLE IF NOT EXISTS HTTPLOGS(request_id  INTEGER PRIMARY KEY, ip  VARCHAR(100), verb   VARCHAR(10), uri     VARCHAR(100), response_code    VARCHAR(4), time_taken VARCHAR(6),  response_size VARCHAR(5), response_time text)"""
queryGetHttpVerbs = """SELECT verb from HTTPLOGS"""
queryInsertRecord = """INSERT INTO HTTPLOGS(ip, verb, uri, response_code, time_taken,  response_size, response_time)) VALUES(?, ?, ?, ?, ?, ?, ?)"""
    
class HttpLog:
    def __init__(self) -> None:
        pass

    def parseRecords(self, file):
        pass
                
    def insert_record(httpLog):
        pass

dbName = "httplogs.db"
conn = sqlite3.connect(dbName, timeout=10)
cursor = conn.cursor()
print(f"Connected to DB: {dbName}")

cursor.execute(queryCreateTable)
print(f"Successfully created tables")
cursor.execute(queryGetHttpVerbs)
response = cursor.fetchall()
print(f"Succesfully query: {response}")

# Parse and Insert records in Table
filePath = "http_requests.log"
with open(filePath) as f:
        lines = f.readlines()
        for line in lines:
            records = line.split(" ")
            ip = records[0]
            httpVerb = records[2]
            httpURI = records[3]
            responseCode = records[4]
            responseTimeTaken = records[5]
            responseSize = records[6]
            responseTime = records[7]
            conn.execute(queryInsertRecord, (ip, httpVerb, httpURI, responseCode, responseTimeTaken, responseSize, responseTime))
            try:
                conn.commit()
            except Exception as e:
                print(f"Error inserting record: {e}")
    

response = cursor.execute(queryGetHttpVerbs)
print(f"Successfully got records: {response}")


conn.close()
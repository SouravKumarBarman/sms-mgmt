import pymysql
from app.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
import json
import time

def connect_db():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB
    )

def get_sms_metrics(country, operator):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute("SELECT sent, success_rate, attempts FROM sms_metrics WHERE country=%s AND operator=%s", (country, operator))
        result = cursor.fetchone()
    conn.close()
    return {"sms_sent": result[0], "success_rate": result[1], "attempts": result[2]} if result else None

def sse_stream(country, operator):
    previous_data = ''
    
    while True:
        # Fetch data from the database
        current_data =get_sms_metrics(country,operator)
        current_data_json = json.dumps(current_data)
        
        # Check if the data has changed
        if current_data_json != previous_data:
            # If changed, send the new data
            yield f"data: {current_data_json}\n\n"
            previous_data = current_data_json
        
        # Sleep for 1 second before checking again
        time.sleep(1)
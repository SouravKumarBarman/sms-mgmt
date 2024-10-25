import pymysql
from app.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

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

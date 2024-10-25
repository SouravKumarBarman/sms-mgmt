import time
import json
from app.models.sms_model import get_sms_metrics

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
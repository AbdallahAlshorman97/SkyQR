from datetime import datetime
import json

def log_qr_data(parsed):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if parsed["type"] == "json":
        content = json.dumps(parsed["data"], indent=2)
    else:
        content = parsed["data"]
    
    print(f"[{timestamp}] QR Code Detected:\n{content}\n")

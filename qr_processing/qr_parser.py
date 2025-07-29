import json

def parse_qr_content(content):
    try:
        data = json.loads(content)
        return {"type": "json", "data": data}
    except json.JSONDecodeError:
        return {"type": "text", "data": content}

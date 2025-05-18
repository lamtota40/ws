import websocket
import json

last_server_seed = None

def on_message(ws, message):
    global last_server_seed

    try:
        data = json.loads(message)
        if 'server_seed' in data:
            if data['server_seed'] != last_server_seed:
                last_server_seed = data['server_seed']
                print(f"Value: {data.get('value')}")
    except Exception as e:
        print(f"Error parsing message: {e}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://socket.faucetpay.io/crash/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

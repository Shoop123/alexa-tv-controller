import constants, tv_controls, secret, websocket, json, signal
from threading import Thread

websocket.enableTrace(False)

def exit_gracefully(signum, frame):
    tv_controls.cleanup()

signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)

def on_message(ws, message):
    print(message)
    message_json = json.loads(message)

    if message_json['action'] == 'toggle_power':
        tv_controls.toggle_power()
    elif message_json['action'] == 'volume_step':
        tv_controls.adjust_volume(message_json['volume_steps'])
    # Chromecase controls not working atm
    # elif message_json['action'] == 'playback_controller':
    #     if message_json['playback_action'] == 'Play':
    #         chromecast_controls.play_chromecast()
    #     elif message_json['playback_action'] == 'Pause':
    #         chromecast_controls.pause_chromecast()
    #     elif message_json['playback_action'] == 'Stop':
    #         chromecast_controls.stop_chromecast()

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###", close_status_code, close_msg)

def on_open(ws):
    print('Opened connection')

def on_ping(wsapp, message):
    print('Got a ping! A pong reply has already been automatically sent.')

def on_pong(wsapp, message):
    print('Got a pong! No need to respond')

def start_connection():
    print('Starting new connection')

    ws = websocket.WebSocketApp(secret.WEBSOCKET_ENDPOINT,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_ping=on_ping,
                                on_pong=on_pong
                            )

    ws.run_forever(reconnect=2,
                   ping_interval=constants.WEBSOCKET_PING_INTERVAL_SECONDS,
                   ping_timeout=10,
                   ping_payload='Ping'
                )

while True:
    print('Creating new thread for connection')

    thread = Thread(target=start_connection, daemon=True)

    thread.start()

    print('Thread started')

    thread.join()

    print('Thread closed')
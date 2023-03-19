import constants, tv_controls, secret, websocket, rel, json, chromecast_controls

def on_message(ws, message):
    print(message)
    message_json = json.loads(message)

    if message_json['action'] == 'toggle_power':
        tv_controls.toggle_power()
    elif message_json['action'] == 'volume_step':
        tv_controls.adjust_volume(message_json['volume_steps'])
    elif message_json['action'] == 'playback_controller':
        if message_json['playback_action'] == 'Play':
            chromecast_controls.play_chromecast()
        elif message_json['playback_action'] == 'Pause':
            chromecast_controls.pause_chromecast()
        elif message_json['playback_action'] == 'Stop':
            chromecast_controls.stop_chromecast()

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###", close_status_code, close_msg)
    rel.abort()
    ws.run_forever(dispatcher=rel,
               reconnect=2,
               ping_interval=constants.WEBSOCKET_PING_INTERVAL_SECONDS,
               ping_timeout=10,
               ping_payload='Ping'
            )
    rel.signal(2, rel.abort)
    rel.dispatch()

def on_open(ws):
    print('Opened connection')

def on_ping(wsapp, message):
    print('Got a ping! A pong reply has already been automatically sent.')

def on_pong(wsapp, message):
    print('Got a pong! No need to respond')

websocket.enableTrace(True)

ws = websocket.WebSocketApp(secret.WEBSOCKET_ENDPOINT,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close,
                            on_ping=on_ping,
                            on_pong=on_pong
                        )

ws.run_forever(dispatcher=rel,
               reconnect=2,
               ping_interval=constants.WEBSOCKET_PING_INTERVAL_SECONDS,
               ping_timeout=10,
               ping_payload='Ping'
            )
rel.signal(2, rel.abort) # Keyboard Interrupt
rel.dispatch()
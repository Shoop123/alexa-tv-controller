from flask import Flask, request
import tv_controls, chromecast_controls
from threading import Thread

app = Flask(__name__)

@app.route('/toggle-power', methods=['POST'])
def toggle_power():
	if request.json and 'powerState' in request.json:
		power_state = request.json['powerState']

		thread = Thread(target=tv_controls.toggle_power)
		thread.start()

		return 'Turning {}'.format('on' if power_state == 'ON' else 'off')

	return 'Invalid request, please supply string power state'

@app.route('/adjust-volume', methods=['POST'])
def adjust_volume():
	if request.json and 'volumeSteps' in request.json:
		volume_steps = request.json['volumeSteps']

		thread = Thread(target=tv_controls.adjust_volume, args=(volume_steps,))
		thread.start()

		return 'Turning {}'.format('down' if volume_steps < 0 else 'up')

	return 'Invalid request, please supply integer volume steps'

@app.route('/play-pause-stop-chromecast-youtube', methods=['POST'])
def play_pause_chromecast_youtube():
	if request.json and 'action' in request.json:
		action = request.json['action'].lower()

		thread = None
		response = ''

		if action == 'play':
			thread = Thread(target=chromecast_controls.play_chromecast)
			response = 'Playing Chromecast'
		elif action == 'pause':
			thread = Thread(target=chromecast_controls.pause_chromecast)
			response = 'Pausing Chromecast'
		elif action == 'stop':
			thread = Thread(target=chromecast_controls.stop_chromecast)
			response = 'Stopping Chromecast'

		if thread:
			thread.start()

		return response

	return 'Invalid request, please supply a valid action'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
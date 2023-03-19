import pychromecast
from secret import CHROMECAST_NAME

def _get_chromecast():
	chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[CHROMECAST_NAME])

	chromecast = None

	if not chromecasts:
		print('No chromecast with name "{}" discovered'.format(CHROMECAST_NAME))
	else:
		chromecast = chromecasts[0]

		chromecast.wait()

	pychromecast.discovery.stop_discovery(browser)

	return chromecast

def stop_chromecast():
	chromecast = _get_chromecast()

	if chromecast is not None:
		chromecast.quit_app()

def pause_chromecast():
	chromecast = _get_chromecast()

	if chromecast is not None:
		chromecast.media_controller.block_until_active()
		chromecast.media_controller.pause()
		
def play_chromecast():
	chromecast = _get_chromecast()

	if chromecast is not None:
		chromecast.media_controller.block_until_active()
		chromecast.media_controller.play()
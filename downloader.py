import logging
import subprocess
logging.basicConfig(level=logging.INFO)


COUNTER = 1
MAX_WORKERS = 8
CLIENT_ID = 'd6c42edbee814d6bbf9d3921b9928f79'
CLIENT_SECRET = '8417470e2f6b4dac8b7641b120c28f18'



def set_credentials():
	subprocess.run(f'export SPOTIPY_CLIENT_ID={CLIENT_ID}')
	subprocess.run(f'export SPOTIPY_CLIENT_SECRET={your-spotify-client-secret}')
	return True

def read_links_to_list():
	url_text_file = open("spotify-urls.txt", 'r')
	url_list = url_text_file.readlines()
	return url_list


def execute_dl_command(url, COUNTER):
	if not url.strip():
		logging.info('Url link blank')
		return False
	cmd = f'spotdl {url}'
	logging.info(f'Url link {COUNTER} downloading...')
	logging.info(cmd)
	subprocess.run(cmd.split(), cwd=r'/tmp')	
	return True


if __name__ == "__main__":
	logging.info('Starting downloader')
	url_list = read_links_to_list()
	for url in url_list:
		execute_dl_command(url, COUNTER)
		COUNTER = COUNTER + 1
	logging.info('Program finished')
	quit()



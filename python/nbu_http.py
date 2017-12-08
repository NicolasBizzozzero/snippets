import urllib
import urllib.request


def get_html_content(url: str) -> bytes:
	with urllib.request.urlopen(url) as response:
		return response.read()


if __name__ == '__main__':
	pass

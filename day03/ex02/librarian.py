import os


def main():

	try:
		venv = os.environ['VIRTUAL_ENV']
	except KeyError:
		venv = None
		print("wrong environment variable")
	if venv:
		if venv.endswith('ex02/sdarr'):
			os.system("pip3 install beautifulsoup4 PyTest > /dev/null; pip freeze; pip freeze  > requirements.txt")
			os.system("rm archive.tar 2> /dev/null;tar -c -f archive.tar sdarr ")
		else:
			raise ValueError("wrong environment variable")


if __name__ == "__main__":
	main()
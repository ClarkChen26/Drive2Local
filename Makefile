install:
	pip3 install apiclient google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client python-crontab PyQt5
	if [ ! -d /etc/Drive2Local/ ]; then mkdir /etc/Drive2Local/; fi
	cp client_id.json /etc/Drive2Local
	cp src/*.py /usr/local/bin
	ln -s /usr/local/bin/Drive2Local.py /usr/local/bin/Drive2Local

clean :
	if [ -d /etc/Drive2Local/ ]; then rm -rf /etc/Drive2Local/; fi
	if [ -d ~/.Drive2Local ]; then rm -rf ~/.Drive2Local; fi
	rm /usr/local/bin/Drive2Local*

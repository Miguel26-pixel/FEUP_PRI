all: database

database: analyze
	./.venv/bin/python3 database.py
	sqlite3 database.db .dump | gzip -c > database.dump.gz

analyze: process
	./.venv/bin/python3 plot.py

process: requirements.txt 
	virtualenv .venv
	./.venv/bin/pip install -r requirements.txt
	./.venv/bin/python3 cleaner.py 
	./.venv/bin/python3 API.py

install: 
	sudo pacman -S pyhton3 python3-virtualenv sqlite3

clean_all: clean
	rm -rf .venv

clean:
	rm -rf __pycache__
	rm -f final_ds2_*.csv *.png database.dump.gz database.db

.PHONY: clean clean_all analyze process install database 


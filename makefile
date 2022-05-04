PORT=8000

run:
	set -a; source .env; set +a; \
	python3 main.py
freeze:
	pip freeze > requirement.txt 
APP_PORT := 8000
APP_HOST := localhost

.PHONY: *

install:
	pip install -r requirements.txt

run_server:
	uvicorn app:application --host $(APP_HOST) --port $(APP_PORT)

run_test:
	pytest tests/test_homework_1.py
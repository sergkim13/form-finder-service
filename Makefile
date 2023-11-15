compose:
	docker compose up -d

stop:
	docker compose down

compose-test:
	docker compose -f docker-compose.test.yaml -p testing run --rm test_app

stop-test:
	docker compose -f docker-compose.test.yaml -p testing down

lint:
	isort form_app
	flake8 form_app
	mypy form_app

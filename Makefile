compose:
	docker compose up -d

stop:
	docker compose down

lint:
	isort form_app
	flake8 form_app
	mypy form_app
